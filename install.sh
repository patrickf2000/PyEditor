#!/bin/bash
if [ ! -d /usr/local/lib/pyeditor ] ; then
	mkdir -p /usr/local/lib/pyeditor
fi 

cd src
cp *.py /usr/local/lib/pyeditor
cd ..
cp ./pyeditor /usr/local/bin
cp ./pyeditor.desktop /usr/share/applications
update-desktop-database
