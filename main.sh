#!/bin/bash

echo "=== Lua Script Decompiler ==="

read -p "Enter the path to the .luac file: " luac_file
if [ ! -f "$luac_file" ]; then
    echo "File not found!"
    exit 1
fi

read -p "Choose a tool (unluac/luadec): " tool
if [[ "$tool" != "unluac" && "$tool" != "luadec" ]]; then
    echo "Invalid tool choice!"
    exit 1
fi

read -p "Enter the path to save the result: " output_file

if [ "$tool" == "unluac" ]; then
    java -jar tools/unluac.jar "$luac_file" > "$output_file"
elif [ "$tool" == "luadec" ]; then
    tools/luadec "$luac_file" > "$output_file"
fi

echo "Decompilation complete. Result saved to $output_file"
