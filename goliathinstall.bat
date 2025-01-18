@echo off
echo Installing required modules.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

python3 -m pip install -r dependencies.txt
pip install -r dependencies.txt

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Installation complete.
pause
cls
python goliathv2.py