# 📊 Financial Report Analysis AI

An intelligent web application that uses AI to analyze financial documents and provide actionable insights tailored to your professional role.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌐 Deploy to Streamlit Cloud

Want to deploy this app online? Follow the comprehensive guide:

👉 **[Deployment Guide](DEPLOYMENT_GUIDE.md)** - Step-by-step instructions to deploy on Streamlit Cloud

Quick deploy steps:
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Add API keys in Secrets
4. Deploy! 🚀

## ✨ Features

- 🤖 **Dual AI Support**: OpenAI (GPT-4o, GPT-4o Mini) & Google Gemini (1.5 Pro, 1.5 Flash)
- 👥 **Role-Based Analysis**: Investor, Analyst, Auditor, or Custom roles
- 📊 **Analysis Types**: Overall, Risk, Growth, Profitability
- 📄 **PDF Export**: Professional formatted reports
- 🧪 **Debug Mode**: Test without API costs
- ✏️ **Customizable Prompts**: Edit or create your own

## 🚀 Quick Start

### 1. Setup

```bash
# Create virtual environment (first time only)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Get API Keys

Choose one or both:
- **OpenAI**: https://platform.openai.com/api-keys
- **Gemini**: https://makersuite.google.com/app/apikey

### 3. Run

```bash
# Easy way (macOS)
./run.command

# Or manually
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 Usage

### Basic Workflow

1. **Enable Debug Mode** (optional, for testing)
   - Check "Enable Debug Mode" in sidebar
   - No API key needed, uses sample data

2. **Configure AI** (for real analysis)
   - Select AI Provider (OpenAI or Gemini)
   - Choose Model
   - Enter API Key

3. **Select Your Role**
   - Investor, Analyst, Auditor, or Custom

4. **Upload Documents**
   - Drag & drop financial report images (PNG, JPG, JPEG)
   - Max 10MB per file

5. **Choose Analysis Type**
   - Click: Overall, Risk, Growth, or Profitability
   - Customize prompt if needed

6. **Analyze & Export**
   - Click "Analyze Documents"
   - Download PDF from results header

## 💡 Tips

### Best Practices
- Start with **Debug Mode** to test the interface
- Use **GPT-4o** or **Gemini 1.5 Pro** for complex analysis
- Upload clear, high-resolution images
- Customize prompts for specific needs

### Cost Optimization
- Use **Debug Mode** for testing (free)
- **GPT-4o Mini** or **Gemini 1.5 Flash** for faster, cheaper analysis
- Combine multiple pages in one analysis

### Common Issues

**Gemini 404 Error**
- The app uses Gemini 1.5 Pro/Flash models
- Ensure your API key has Gemini API enabled
- Try different model if one doesn't work

**PDF Formatting**
- Bullet points are properly formatted
- Markdown is converted to clean text
- Headers have proper styling

## 🔧 Configuration

### Supported Models

**OpenAI:**
- GPT-4 Vision (legacy)
- GPT-4o (recommended)
- GPT-4o Mini (fast & cheap)

**Gemini:**
- Gemini 1.5 Pro (powerful)
- Gemini 1.5 Flash (fast)
- Gemini Pro (basic)

### File Support
- Formats: PNG, JPG, JPEG
- Max size: 10MB per file
- Multiple files: Yes

## 📁 Project Structure

```
project_financial_report_analysis/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── run.command           # macOS launcher script
├── src/
│   ├── config.py         # Configuration constants
│   ├── prompts.py        # Analysis prompt templates (16 templates)
│   ├── ai_handler.py     # OpenAI & Gemini integration
│   ├── mock_data.py      # Debug mode sample data
│   └── utils/
│       ├── pdf_generator.py    # PDF export
│       └── image_utils.py      # Image processing
├── test_image/           # Sample test images
└── .gitignore            # Git ignore rules
```

**Note**: Create your own virtual environment (`venv/`) - it's not included in the project.

## 🎯 Analysis Types Explained

### Overall Analysis
Comprehensive review covering:
- Key financial metrics with YoY/QoQ comparisons
- Income statement, balance sheet, cash flow
- Strategic initiatives and market outlook
- Investment recommendations

### Risk Analysis
Focuses on:
- Financial risks and red flags
- Market and operational risks
- Risk mitigation strategies
- Compliance issues

### Growth Analysis
Evaluates:
- Revenue growth trends
- Market opportunities
- Competitive positioning
- Expansion strategies

### Profitability Analysis
Deep dive into:
- Profit margins (gross, operating, net)
- Return metrics (ROE, ROA, ROIC)
- Earnings quality
- Cost structure efficiency

## 🔐 Security

- ✅ API keys: Session-only, never stored
- ✅ Images: Processed in memory, not saved
- ✅ No data collection or tracking
- ✅ Open source, inspect the code

## 🛠️ Development

### Adding Custom Prompts

Edit `src/prompts.py` to add or modify analysis templates:

```python
PROMPTS = {
    "Overall Analysis": {
        "Your Role": "Your custom prompt here...",
    }
}
```

### Extending AI Providers

Add new providers in `src/ai_handler.py`:

```python
class AIHandler:
    def __init__(self, provider, model, api_key):
        if provider == 'your_provider':
            # Initialize your provider
            pass
```

## 📜 Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

**Current Version: 1.0.3**
- ✅ Fixed PDF formatting (proper bullets, no markdown)
- ✅ Simplified UI (removed email, streamlined export)
- ✅ Updated Gemini models (1.5 Pro/Flash)
- ✅ Debug mode for cost-free testing

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional AI providers (Claude, etc.)
- Enhanced chart/graph recognition
- Batch processing
- More export formats
- Additional analysis templates

## 💬 Support

For issues or questions:
1. Check this README
2. Review CHANGELOG.md
3. Inspect the code (it's well-documented)

---

**Built with ❤️ for financial professionals**

*Streamline your financial document analysis workflow*
