# DTXSMARTS
Straightforward command-line SMARTS substructure search for DSSTOX

## HELP
```
usage: dtxsmarts.py [-h] [-s [SUBS ...]] [-m MODE] -u USER -p PWD -l LOC -t TOFILE

desc: a command-line utility that identifies structures from DSSTOX using a given set of substructures

options:
  -h, --help            show this help message and exit
  -s, --subs [SUBS ...]
                        SMARTS substructure query strings
  -m, --mode MODE       ALL (default, match all substructures) or ANY (match any substructure)
  -u, --user USER       DSSTOX database username
  -p, --pwd PWD         DSSTOX database password
  -l, --loc LOC         DSSTOX database location/hostname
  -t, --tofile TOFILE   XLSX filename to write output
```

## POWERSHELL
```
.\dtxsmarts -u YOUR_DSSTOX_USERNAME -p YOUR_DSSTOX_PASSWORD -l mysql-ip-m.epa.gov -s "B(F)(F)(F)F" "C1CCCCC1" -t tetrafluoroborate_and_cyclohexyl.xlsx -m ALL
.\dtxsmarts -u YOUR_DSSTOX_USERNAME -p YOUR_DSSTOX_PASSWORD -l mysql-ip-m.epa.gov -s "B(F)(F)(F)F" "C1CCCCC1" -t tetrafluoroborate_or_cyclohexyl.xlsx -m ANY
```

## CMD
```
dtxsmarts -u YOUR_DSSTOX_USERNAME -p YOUR_DSSTOX_PASSWORD -l mysql-ip-m.epa.gov -s B(F)(F)(F)F C1CCCCC1 -t tetrafluoroborate_and_cyclohexyl.xlsx -m ALL
dtxsmarts -u YOUR_DSSTOX_USERNAME -p YOUR_DSSTOX_PASSWORD -l mysql-ip-m.epa.gov -s B(F)(F)(F)F C1CCCCC1 -t tetrafluoroborate_or_cyclohexyl.xlsx -m ANY
```

## PYTHON
```
py dtxsmarts.py -u YOUR_DSSTOX_USERNAME -p YOUR_DSSTOX_PASSWORD -l mysql-ip-m.epa.gov -s B(F)(F)(F)F C1CCCCC1 -t tetrafluoroborate_and_cyclohexyl.xlsx -m ALL
py dtxsmarts.py -u YOUR_DSSTOX_USERNAME -p YOUR_DSSTOX_PASSWORD -l mysql-ip-m.epa.gov -s B(F)(F)(F)F C1CCCCC1 -t tetrafluoroborate_or_cyclohexyl.xlsx -m ANY
```