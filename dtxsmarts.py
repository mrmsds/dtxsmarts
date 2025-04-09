from argparse import ArgumentParser
from contextlib import closing
from rdkit.Chem import MolFromSmiles, MolFromSmarts
from mysql.connector import connect
from pandas import read_sql_query
from warnings import filterwarnings

# Parse CLA
parser = ArgumentParser(description='desc: a command-line utility that identifies structures from DSSTOX using a given set of substructures')
parser.add_argument('-s', '--subs', nargs='*', help='SMARTS substructure query strings')
parser.add_argument('-m', '--mode', help='ALL (default, match all substructures) or ANY (match any substructure)', default='ALL')
parser.add_argument('-u', '--user', help='DSSTOX database username', required=True)
parser.add_argument('-p', '--pwd', help='DSSTOX database password', required=True)
parser.add_argument('-l', '--loc', help='DSSTOX database location/hostname', required=True)
parser.add_argument('-t', '--tofile', help='XLSX filename to write output', required=True)
args = parser.parse_args()

# Configure database connection with CLA
config = {
    'host': args.loc,
    'database': 'prod_dsstox',
    'user': args.user,
    'password': args.pwd,
    'charset': 'utf8',
    'collation': 'utf8_general_ci',
    'use_unicode': True
}

# Define initial filtering SQL query for compounds
query = ('SELECT gs.dsstox_substance_id AS DTXSID, c.dsstox_compound_id AS DTXCID, gs.casrn AS CASRN, gs.preferred_name AS PREF_NAME, c.smiles AS SMILES '
         'FROM compounds c JOIN generic_substance_compounds gsc ON gsc.fk_compound_id = c.id '
         'JOIN generic_substances gs ON gs.id = gsc.fk_generic_substance_id '
         'WHERE c.smiles IS NOT NULL AND c.smiles != \'NULL\' AND c.smiles != \'\'')

# Ignore MySQL/pandas warnings
filterwarnings('ignore', category=UserWarning)
# Open the connection and execute the query with pandas
with closing(connect(**config)) as conn:
    cmpds = read_sql_query(query, conn)

# Convert input substructure SMARTS to query molecules
qmols = [MolFromSmarts(sma) for sma in args.subs]
# Match a molecule against input query molecule substructures
def subs(mol):
    matches = [mol.HasSubstructMatch(q) for q in qmols]
    return any(matches) if args.mode.lower() == 'any' else all(matches)

# Test a molecule against substructures
def test(smi):
    match = False
    try:
        mol = MolFromSmiles(smi, sanitize=False)
        mol.UpdatePropertyCache(strict=False)
        try:
            match = subs(mol)
        except:
            pass
    except:
        pass

    return match

cmpds['MATCH'] = cmpds['SMILES'].apply(test)
matches = cmpds[cmpds['MATCH']]
print(f'Identified {len(matches)} matching compounds')
matches.to_excel(args.tofile, index=False)
print(f'Saved to file {args.tofile}')