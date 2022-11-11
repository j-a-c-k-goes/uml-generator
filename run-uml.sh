#!/usr/bin/env bash

# Setup args from command-line (future-work)
# while getopts p: flag
# do
#    case "${flag}" in
#        p) project=${OPTARG};;
#    esac
# done

function uml(){
    echo "Running UML Builder"
    python3 ./src/app/uml.py
}
