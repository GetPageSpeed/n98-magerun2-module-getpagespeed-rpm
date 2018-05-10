#!/bin/bash

rm -rf *.rpm
spectool -g n98-magerun2-module-getpagespeed.spec 
mock -r epel-7-x86_64-gps --spec=n98-magerun2-module-getpagespeed.spec --sources=. --resultdir=. --buildsrpm
mock -r epel-7-x86_64-gps --rebuild --resultdir=. *.src.rpm
