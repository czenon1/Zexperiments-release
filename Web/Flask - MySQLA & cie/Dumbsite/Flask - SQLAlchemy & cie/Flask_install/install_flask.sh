#!/bin/bash

# Check if pip is installed
pip --version
if [ $? -ne 0 ]; then
    # Install pip
    echo "pip not found, installing pip..."
    apt-get update
    apt-get install python3-pip
fi

# Install Flask, SQLAlchemy and Flask-WTF
pip3 install Flask
pip3 install SQLAlchemy
pip3 install Flask-WTF

echo ""
echo "############### Done ! ###############"
echo ""