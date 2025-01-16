#!/usr/bin/env bash

#Version v1.0

if [ "$1" == "-h" ]; then # CALL THE HELP TO EXPLAIN HOW TO USE THE SCRIPT
    echo "This script will add the models to the admin view"
    echo "Example:"
    echo "          bash .addmodels.sh project_name app_name"
fi
if [ "$1" == "" ]; then
    echo "USE THE PARAMETER -h TO DISPLAY HELP"

else 
    if [ -d $1 ]; then #CHECK IF THE PROJECT EXIST
        cd $1
        
        if [ -d "apps/$2" ]; then # CHECK IF THE APP EXISTS
            echo "Adding models from $2 to the admin view"

            echo 'from django.contrib import admin' > apps/$2/admin.py # CREATE OR CLEAN THE ADMIN.PY FILE with the import of admin
            cat apps/$2/models.py | grep '^class .*(models.Model):' | cut -d ' ' -f 2 |cut -d '(' -f 1 | # GET THE MODELS NAMES
            while read line; do # LOOP THE MODELS NAMES TO ADD THE IMPORTS TO THE ADMIN.PY
                echo "$line imported" # PRINT THE MODEL NAME
                echo "from .models import $line" >> apps/$2/admin.py;
            done

            echo "" >> apps/$2/admin.py # ADD A BLANK LINE
            echo "# Register your models here." >> apps/$2/admin.py # ADD A COMMENT
            echo "" >> apps/$2/admin.py # ADD A BLANK LINE

            # CREATE THE ADMIN MODELS 

            cat apps/$2/models.py | grep '^class .*(models.Model):' | cut -d ' ' -f 2 |cut -d '(' -f 1 | # GET THE MODELS NAMES
            while read line; do # LOOP THE MODELS NAMES TO CREATE THE ADMIN MODEL
                
                echo "class ${line}Admin(admin.ModelAdmin):" >> apps/$2/admin.py; # CREATE THE ADMIN MODEL
                echo "    pass" >> apps/$2/admin.py; # Make the pass
                echo "" >> apps/$2/admin.py; # ADD A BLANK LINE
            done

            cat apps/$2/admin.py | grep '^from .models import' | cut -d ' ' -f 4 | # GET THE MODELS NAMES AGAIN
            while read line; do # LOOP THE MODELS NAMES TO ADD THE REGISTER TO THE ADMIN.PY
                echo "$line registered" # PRINT THE MODEL NAME
                echo "admin.site.register($line, ${line}Admin)" >> apps/$2/admin.py;
            done
        fi
    fi
fi