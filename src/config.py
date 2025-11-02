"""
Configuration file for Financial Report Analysis App
"""

# OpenAI Models
OPENAI_MODELS = {
    "GPT-4o": "gpt-4o",
    "GPT-4o Mini": "gpt-4o-mini",
}

# Gemini Models
# Using Gemini 2.0 series experimental models (as of Nov 2025)
# Note: Gemini 2.5 may not be released yet, using available 2.0 models
GEMINI_MODELS = {
    "Gemini 2.0 Flash (Experimental)": "gemini-2.0-flash-exp",
    "Gemini 2.5 Pro": "gemini-2.5-pro",
}

# User Roles
USER_ROLES = [
    "Investor",
    "Analyst", 
    "Auditor",
    "Other"
]

# Supported Image Formats
SUPPORTED_FORMATS = ["png", "jpg", "jpeg"]

# Maximum file size (in MB)
MAX_FILE_SIZE_MB = 10

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# App Configuration
APP_TITLE = "📊 Financial Report Analysis AI"
APP_ICON = "📊"
PAGE_CONFIG = {
    "page_title": "Financial Report Analysis",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}
