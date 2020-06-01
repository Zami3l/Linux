#!/bin/bash

#Required
echo "/!\\ The script need than your connection internet is operationnel /!\\"

function setlanguage
{
    echo "-- Select language --"
    echo "1 - French"
    echo "2 - English"
    echo "E - Exit"
    echo "---------------------"

    while true; do
        read -p "What language want you ? " language
        case $language in 
            [1]* ) loadkeys fr; break;;
            [2]* ) loadkeys us; break;;
            [Ee]* ) exit;;
        esac
    done
}

function disk
{
    echo "-- Disk select --"
    lsblk
    read -p "What language want you ? " disk
    echo "---------------------"

    echo "-- Partionnement type --"
    echo "1 - Boot, Root, no Home, no Swap"
    echo "2 - Boot, Root, Home, no Swap"
    echo "3 - Boot, Root, Home, Swap"
    echo "E - Exit"

    echo "--------------------"
}