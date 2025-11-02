"""
Financial Report Analysis AI - Streamlit Application
Main application file
"""

import streamlit as st
import sys
import os
from pathlib import Path
from datetime import datetime
import io

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from src.config import (
    OPENAI_MODELS, GEMINI_MODELS, USER_ROLES, 
    SUPPORTED_FORMATS, MAX_FILE_SIZE_MB, PAGE_CONFIG
)
from src.prompts import get_prompt, get_analysis_types, PROMPTS
from src.ai_handler import AIHandler
from src.utils import PDFGenerator, validate_image, get_image_info
from src.mock_data import get_mock_analysis


# Page configuration
st.set_page_config(**PAGE_CONFIG)

# Initialize session state
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None
if 'uploaded_images' not in st.session_state:
    st.session_state.uploaded_images = []
if 'current_prompt' not in st.session_state:
    st.session_state.current_prompt = ""
if 'debug_mode' not in st.session_state:
    st.session_state.debug_mode = False
if 'selected_analysis' not in st.session_state:
    st.session_state.selected_analysis = "Overall Analysis"


def main():
    """Main application function."""
    
    # Header
    st.title("📊 Financial Report Analysis AI")
    st.markdown("""
    ### Intelligent Analysis of Financial Documents
    Upload financial reports, balance sheets, or earnings documents as images, 
    and get AI-powered insights tailored to your role.
    """)
    
    st.divider()
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Debug Mode Toggle
        st.subheader("🔧 Debug Mode")
        debug_mode = st.checkbox(
            "Enable Debug Mode (Use Mock Data)",
            value=st.session_state.debug_mode,
            help="Enable to test without using API credits. Uses pre-generated sample analysis."
        )
        st.session_state.debug_mode = debug_mode
        
        if debug_mode:
            st.info("🧪 **Debug Mode Active**: Mock data will be used. No API calls will be made.")
        
        st.divider()
        
        # AI Provider Selection
        st.subheader("1. AI Provider")
        provider = st.selectbox(
            "Choose AI Provider",
            ["OpenAI", "Gemini"],
            help="Select the AI provider for analysis" + (" (Disabled in Debug Mode)" if debug_mode else ""),
            disabled=debug_mode
        )
        
        # Model Selection
        if provider == "OpenAI":
            models = OPENAI_MODELS
        else:
            models = GEMINI_MODELS
        
        model_name = st.selectbox(
            "Choose Model",
            list(models.keys()),
            help="Select the specific model to use" + (" (Disabled in Debug Mode)" if debug_mode else ""),
            disabled=debug_mode
        )
        model_id = models[model_name]
        
        # API Key Input
        # Try to get API key from Streamlit secrets or environment variables
        default_api_key = ""
        if not debug_mode:
            if provider == "OpenAI":
                # Try st.secrets first, then environment variable
                try:
                    default_api_key = st.secrets.get("OPENAI_API_KEY", "")
                except:
                    default_api_key = os.getenv("OPENAI_API_KEY", "")
            else:  # Gemini
                try:
                    default_api_key = st.secrets.get("GEMINI_API_KEY", "")
                except:
                    default_api_key = os.getenv("GEMINI_API_KEY", "")
        
        # Show API key input field
        api_key = st.text_input(
            f"{provider} API Key",
            type="password",
            value=default_api_key,
            help=f"Enter your {provider} API key" + (" (Not needed in Debug Mode)" if debug_mode else ""),
            placeholder="sk-..." if provider == "OpenAI" else "AIza...",
            disabled=debug_mode
        )
        
        # Show status message
        if debug_mode:
            st.success("✅ API key not required in Debug Mode")
        elif default_api_key:
            st.success("✅ API key loaded from secrets/environment")
        
        st.divider()
        
        # User Role Selection
        st.subheader("2. Your Role")
        user_role = st.selectbox(
            "Select your role",
            USER_ROLES,
            help="Choose your role for customized analysis"
        )
        
        # Custom role input if "Other" selected
        if user_role == "Other":
            custom_role = st.text_input(
                "Specify your role",
                placeholder="e.g., CFO, Consultant, Student"
            )
            if custom_role:
                user_role = custom_role
        
        st.divider()
        
        # Advanced Options
        with st.expander("🔧 Advanced Options"):
            auto_resize = st.checkbox(
                "Auto-resize large images",
                value=True,
                help="Automatically resize images larger than 2048px"
            )
            show_image_info = st.checkbox(
                "Show image information",
                value=False,
                help="Display technical details about uploaded images"
            )
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 Upload Financial Documents")
        
        # File uploader
        uploaded_files = st.file_uploader(
            "Drag and drop images here",
            type=SUPPORTED_FORMATS,
            accept_multiple_files=True,
            help=f"Supported formats: {', '.join(SUPPORTED_FORMATS).upper()} (Max {MAX_FILE_SIZE_MB}MB per file)"
        )
        
        # Display uploaded images
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} file(s) uploaded")
            
            # Validate and store images
            valid_images = []
            for i, uploaded_file in enumerate(uploaded_files):
                img_bytes = uploaded_file.read()
                is_valid, msg = validate_image(img_bytes, MAX_FILE_SIZE_MB)
                
                if is_valid:
                    valid_images.append(img_bytes)
                    
                    # Show thumbnail
                    with st.expander(f"📄 {uploaded_file.name}"):
                        st.image(img_bytes, use_container_width=True)
                        
                        if show_image_info:
                            info = get_image_info(img_bytes)
                            st.json(info)
                else:
                    st.error(f"❌ {uploaded_file.name}: {msg}")
            
            st.session_state.uploaded_images = valid_images
        else:
            st.info("👆 Upload one or more images to begin analysis")
            st.session_state.uploaded_images = []
    
    with col2:
        st.subheader("✍️ Analysis Prompt")
        
        # Get analysis types for prompt templates
        analysis_types = get_analysis_types()
        
        # Prompt selection buttons
        st.markdown("**Quick Prompt Templates:**")
        button_cols = st.columns(len(analysis_types))
        
        selected_analysis = st.session_state.selected_analysis
        
        for idx, analysis_type in enumerate(analysis_types):
            with button_cols[idx]:
                if st.button(
                    analysis_type.replace(' Analysis', ''),
                    use_container_width=True,
                    type="secondary" if selected_analysis != analysis_type else "primary"
                ):
                    st.session_state.selected_analysis = analysis_type
                    st.session_state.current_prompt = get_prompt(analysis_type, user_role)
                    st.rerun()
        
        # Initialize prompt if empty
        if not st.session_state.current_prompt:
            st.session_state.current_prompt = get_prompt(st.session_state.selected_analysis, user_role)
        
        # Editable prompt text area
        prompt_text = st.text_area(
            "Edit or customize your prompt",
            value=st.session_state.current_prompt,
            height=300,
            help="Customize the analysis prompt to your specific needs"
        )
        
        st.session_state.current_prompt = prompt_text
        
        # Reset prompt button
        if st.button("🔄 Reset to Default Prompt"):
            st.session_state.current_prompt = get_prompt(st.session_state.selected_analysis, user_role)
            st.rerun()
    
    st.divider()
    
    # Analyze button
    col_analyze, col_space = st.columns([1, 2])
    with col_analyze:
        # In debug mode, don't require API key
        if debug_mode:
            analyze_disabled = not (st.session_state.uploaded_images and prompt_text)
            button_label = "🧪 Analyze (Debug Mode)"
        else:
            analyze_disabled = not (api_key and st.session_state.uploaded_images and prompt_text)
            button_label = "🚀 Analyze Documents"
        
        analyze_button = st.button(
            button_label,
            type="primary",
            use_container_width=True,
            disabled=analyze_disabled
        )
    
    # Check prerequisites
    if analyze_button:
        # In debug mode, skip API key check
        if not debug_mode and not api_key:
            st.error("❌ Please enter your API key in the sidebar")
        elif not st.session_state.uploaded_images:
            st.error("❌ Please upload at least one image")
        elif not prompt_text:
            st.error("❌ Please enter a prompt")
        else:
            # Perform analysis
            if debug_mode:
                # Use mock data
                with st.spinner(f"🧪 Generating mock analysis for {user_role}..."):
                    try:
                        import time
                        time.sleep(2)  # Simulate processing time
                        
                        result = get_mock_analysis(user_role, st.session_state.selected_analysis)
                        st.session_state.analysis_result = result
                        st.success("✅ Mock analysis complete! (No API credits used)")
                        st.info("💡 **Debug Mode**: This is sample data. Enable real analysis by unchecking Debug Mode and providing an API key.")
                    except Exception as e:
                        st.error(f"❌ Error generating mock analysis: {str(e)}")
                        st.session_state.analysis_result = None
            else:
                # Use real API
                with st.spinner(f"🔍 Analyzing with {provider} {model_name}..."):
                    try:
                        # Initialize AI handler
                        ai_handler = AIHandler(
                            provider=provider.lower(),
                            model=model_id,
                            api_key=api_key
                        )
                        
                        # Perform analysis
                        result = ai_handler.analyze(
                            images=st.session_state.uploaded_images,
                            prompt=prompt_text,
                            role=user_role
                        )
                        
                        st.session_state.analysis_result = result
                        st.success("✅ Analysis complete!")
                        
                    except Exception as e:
                        st.error(f"❌ Error during analysis: {str(e)}")
                        st.session_state.analysis_result = None
    
    # Display analysis results
    if st.session_state.analysis_result:
        st.divider()
        
        # Header with PDF download button
        col_title, col_button = st.columns([3, 1])
        with col_title:
            st.header("📋 Analysis Results")
        with col_button:
            result = st.session_state.analysis_result
            try:
                pdf_generator = PDFGenerator()
                pdf_bytes = pdf_generator.generate_pdf(result)
                
                st.download_button(
                    label="📄 Download PDF",
                    data=pdf_bytes,
                    file_name=f"Financial_Analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    type="primary"
                )
            except Exception as e:
                st.error(f"PDF Error: {str(e)}")
        
        # Metadata
        result = st.session_state.analysis_result
        meta_cols = st.columns(4)
        with meta_cols[0]:
            provider_display = result['provider'].upper()
            if result['provider'] == 'mock':
                provider_display = "🧪 MOCK"
            st.metric("Provider", provider_display)
        with meta_cols[1]:
            model_display = result['model']
            if result['provider'] == 'mock':
                model_display = "Debug Mode"
            st.metric("Model", model_display)
        with meta_cols[2]:
            st.metric("Role", result['role'])
        with meta_cols[3]:
            st.metric("Images", result['image_count'])
        
        st.markdown("---")
        
        # Analysis text
        st.markdown(result['analysis'])
    
    # Footer
    st.divider()
    with st.expander("ℹ️ About This Application"):
        st.markdown("""
        ### Financial Report Analysis AI
        
        This application uses advanced AI models to analyze financial documents and provide 
        insights tailored to your specific role and requirements.
        
        **Key Features:**
        - 🤖 Support for OpenAI and Google Gemini models
        - 👥 Role-based analysis (Investor, Analyst, Auditor, etc.)
        - 📊 Multiple analysis types (Overall, Risk, Growth, Profitability)
        - 📄 PDF export with proper formatting
        - ✏️ Customizable prompts
        - 🧪 Debug mode for cost-free testing
        
        **Tips for Best Results:**
        1. 🧪 **Start with Debug Mode** to test the interface without API costs
        2. Upload clear, high-quality images of financial documents
        3. Select the role that best matches your needs
        4. Use the quick prompt templates to get started
        5. Review and customize the prompt if needed
        6. Use a powerful model (GPT-4o or Gemini 1.5 Pro) for complex analysis
        
        **Security Note:**
        - API keys are not stored and are only used for the current session
        - Uploaded images are processed in memory and not saved
        """)


if __name__ == "__main__":
    main()
