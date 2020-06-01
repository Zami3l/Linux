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
        read -p "What language ? " language
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
    read -p "What disk ? " disk
    echo "-----------------"

    echo "-- Partionnement type --"
    echo "1 - Boot, Root, no Home, no Swap"
    echo "2 - Boot, Root, Home, no Swap"
    echo "3 - Boot, Root, Home, Swap"
    echo "E - Exit"

    while true; do
        read -p "What partionnement type ? " language
        case $language in 
            [1]* )
                read -p "Size Root : " $size_root;
                break;;
            [2]* )
                read -p "Size Root : " $size_root;
                read -p "Size Home : " $size_home;
                break;;
            [3]* )
                read -p "Size Swap : " $size_home;
                read -p "Size Root : " $size_root;
                read -p "Size Home : " $size_home;
                break;;
            [Ee]* ) exit;;
        esac
    done

    echo "--------------------"
}