"""
Financial Report Analysis AI - Source Package
"""

__version__ = "1.0.0"
__author__ = "Financial Report Analysis AI Team"
__description__ = "AI-powered financial document analysis tool"

from .config import *
from .prompts import get_prompt, get_analysis_types
from .ai_handler import AIHandler

__all__ = [
    'AIHandler',
    'get_prompt',
    'get_analysis_types',
]
