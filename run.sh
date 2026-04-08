#!/bin/bash
# AI Fitness Coach Project - Final Version - 01-01-2022
echo "Starting AI Fitness Coach..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo "Starting Streamlit application..."
streamlit run app/streamlit_app.py
