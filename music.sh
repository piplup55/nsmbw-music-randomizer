#!/bin/bash

# Change directory to the script's directory and navigate to CopyOfFiles
cd "$(dirname "$0")/Sound"

# Create the OutputFolder if it doesn't exist
mkdir -p "../OutputFolder"

# Generate a 'random number' that won't be used
m=$RANDOM

loop=0
while [ $loop -lt 1000 ]; do
    ((loop++))

    # Count the number of files and store their names in an array
    files=(*)
    n=${#files[@]}

    # Generate two random numbers
    rand1=$((RANDOM % n))
    rand2=$((RANDOM % n))

    if [ $rand1 -eq $rand2 ]; then
        continue
    fi

    #echo $rand1
    #echo $rand2

    # Copy files to the OutputFolder and swap their names in the output
    cp -v "${files[$rand1]}" "../OutputFolder/${files[$rand2]}"
    cp -v "${files[$rand2]}" "../OutputFolder/${files[$rand1]}"

    #cp "${files[$rand1]}" "../OutputFolder/${files[$rand2]}"
    #cp "${files[$rand2]}" "../OutputFolder/${files[$rand1]}"
done
