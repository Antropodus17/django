#!/usr/bin/env bash

#Version v1.0

if [ "$1" == "-h" ]; then # CALL THE HELP TO EXPLAIN HOW TO USE THE SCRIPT
    echo "This script will add the models to the admin view"
fi
if [ -d $1 ]; then #CHECK IF THE PROJECT EXIST
    cd $1
    if [ -d $2 ]; then # CHECK IF THE APP EXISTS
        echo 'from django.contrib import admin' > apps/$2/admin.py
        cat apps/$2/models.py | grep '^class .*(models.Model):' | cut -d ' ' -f 2 |cut -d '(' -f 1 | 
        while read line; do
            echo "from .models import $line" >> apps/$2/admin.py;
        done

        cat apps/$2/admin.py | grep '^from .models import' | cut -d ' ' -f 4 |
        while read line; do
            echo "admin.site.register($line)" >> apps/$2/admin.py;
        done
    fi
fi