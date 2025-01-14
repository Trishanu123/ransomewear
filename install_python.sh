#!/bin/bash

# Check if Python is already installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed."
else
    echo "Installing Python..."
    # Update package manager and install Python
    sudo apt update
    sudo apt install -y python3 python3-pip
fi

# Check if pip is installed
if command -v pip3 &>/dev/null; then
    echo "pip is already installed."
else
    echo "Installing pip..."
    sudo apt install -y python3-pip
fi

echo "Python and pip installation completed."

