#!/bin/bash

# Financial Report Analysis AI - Launch Script
# This script activates the virtual environment and runs the Streamlit app

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate to the project directory
cd "$DIR"

# Activate virtual environment
source wind/bin/activate

# Run Streamlit app
streamlit run app.py

# Keep terminal open if there's an error
read -p "Press any key to exit..."
