#!/bin/bash

#Required
echo "/!\\ The script need than your connection internet is operationnel /!\\"

function setlanguage
{
    echo "-- Select language --"
    echo "1 - French"
    echo "2 - English"
    echo "E - Exit"

    while true; do
        read -p "What language want you ? " language
        case $language in 
            [1]* ) loadkeys fr; break;;
            [2]* ) loadkeys us; break;;
            [Ee]* ) exit;;
        esac
    done
}

