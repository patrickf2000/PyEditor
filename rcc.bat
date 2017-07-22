@echo off
echo Generating resources script...
pyrcc5 icons.qrc -o src/resources.py
echo Done