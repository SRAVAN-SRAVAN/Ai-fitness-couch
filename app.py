#!/usr/bin/env python3
"""
AI Fitness Coach - Hugging Face Spaces Entry Point
Main application file for Hugging Face Spaces deployment
"""

import os
import sys
import streamlit as st

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the main Streamlit app
from app.streamlit_app import main

if __name__ == "__main__":
    main()
