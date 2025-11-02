# Changelog

All notable changes to the Financial Report Analysis AI project will be documented in this file.

## [1.0.3] - 2025-11-01

### Fixed
- **PDF Formatting Issues:**
  - Fixed bullet points appearing as one continuous paragraph
  - Removed markdown markers (`**`, `###`, etc.) from PDF output
  - Implemented proper line breaks between bullet points
  - Added appropriate spacing between sections
  - Correctly formatted headers and subheadings
  
- **Gemini API Compatibility:**
  - Fixed 404 errors with Gemini models
  - Added automatic model name correction (e.g., `gemini-1.5-pro` → `models/gemini-1.5-pro`)
  - Implemented model name mapping for all Gemini models
  
### Changed
- **Email Functionality Redesign:**
  - Changed email sending to work FROM the application TO recipients
  - Removed requirement for users to provide their email credentials
  - Added support for environment variables (`APP_EMAIL`, `APP_EMAIL_PASSWORD`)
  - Implemented multiple recipient support (one or more emails)
  - Improved HTML email formatting with proper bullet list rendering
  - Updated UI to make email flow clearer
  - Added optional credential override for testing/custom setups

### Documentation
- Added `FIXES_v1.0.3.md` with detailed fix documentation in English and Chinese
- Updated app "About" section with new email setup instructions

## [1.0.2] - 2025-11-01

### 🧪 Added - Debug Mode Feature

#### Debug Mode Implementation
- **Mock Data System**: Complete pre-generated sample analysis for testing
- **UI Toggle**: Checkbox in sidebar to enable/disable debug mode
- **Cost-Free Testing**: Test application features without API credits
- **Comprehensive Mock Data**: 
  - Investor analysis: TechCorp Inc. Q3 2024 comprehensive report
  - Analyst analysis: Detailed financial ratios and metrics
  - Auditor analysis: Compliance review and red flag identification
  - All mock data follows enhanced output format standards

#### Features in Debug Mode
- ✅ No API key required
- ✅ No API costs incurred
- ✅ Instant analysis generation (2-second simulation)
- ✅ Full UI testing capability
- ✅ PDF export testing
- ✅ Email functionality testing
- ✅ All analysis types supported
- ✅ Role-specific mock data

#### Technical Implementation
- **New Module**: `src/mock_data.py` with comprehensive mock analyses
- **UI Updates**: Debug mode toggle and conditional API key validation
- **Session State**: Debug mode preference preserved during session
- **Visual Indicators**: Clear labeling when debug mode is active

#### Use Cases
- Testing application without API costs
- Demonstrating features to stakeholders
- UI/UX development and testing
- PDF and email feature validation
- Training and onboarding users
- Development and debugging

#### Documentation
- README.md updated with debug mode instructions
- Testing guide updated with debug mode usage
- User guide includes debug mode workflow

### Files Modified
- `app.py`: Added debug mode toggle and conditional logic
- `src/mock_data.py`: Created with comprehensive mock analyses
- `README.md`: Added debug mode documentation
- `CHANGELOG.md`: This entry

## [1.0.1] - 2025-11-01

### 🎯 Enhanced - Improved Output Quality

#### Prompt Engineering Enhancements
- **Comprehensive Output Guidelines**: Added detailed output format specifications to all prompts
- **Structured Templates**: Enhanced all 16 prompt templates (4 analysis types × 4 roles) with:
  - Clear section headers and hierarchical structure
  - Specific metric requirements with units (EUR/USD million, %, basis points)
  - Period-over-period comparison requirements (YoY, QoQ)
  - Financial ratio calculations with formulas
  - Visual data analysis requirements
  - Risk assessment frameworks
  - Strategic initiative coverage
  - Market outlook and forward-looking statements

#### Role-Specific Improvements

**Investor Prompts**:
- 12-section comprehensive framework
- Key metrics with comparative data
- Income/expenses analysis structure
- Balance sheet highlights format
- Credit quality metrics
- Shareholder information requirements
- Investment perspective synthesis

**Analyst Prompts**:
- 10-section detailed analytical framework
- Complete financial statements summary (Income, Balance Sheet, Cash Flow)
- Comprehensive ratio analysis (4 categories: Profitability, Liquidity, Efficiency, Leverage)
- Segment performance breakdowns
- Cost structure and margin analysis
- Benchmark and comparative analysis
- Calculation requirements for key ratios

**Auditor Prompts**:
- 15-section audit framework
- Compliance and standards review structure
- Red flags identification checklist
- Asset quality assessment by category
- Revenue recognition analysis (ASC 606/IFRS 15)
- Internal controls assessment
- Risk management disclosure review
- Regulatory compliance verification
- Severity flagging system (High/Medium/Low)

**General/Other Prompts**:
- 12-section business-friendly framework
- Simplified language requirements
- Context and explanation emphasis
- Visual interpretation guidelines
- Bottom-line assessment structure

#### Documentation
- **SAMPLE_OUTPUT.md**: Created comprehensive reference document with:
  - Real-world example (ABN AMRO Q3 2024 format)
  - Formatting best practices
  - Good vs. bad output examples
  - Role-specific output characteristics
  - Quality evaluation checklist

#### Output Quality Standards
All prompts now enforce:
- Specific numbers with proper units
- Period-over-period comparisons
- Structured sections with headers
- Visual data interpretation
- Risk and outlook coverage
- Professional financial terminology
- Formula citations for calculated ratios
- Significance thresholds (>5% changes noted)

### Technical
- Updated `src/prompts.py` with enhanced templates (500+ lines)
- Added output quality guidelines documentation
- Maintained backward compatibility

## [1.0.0] - 2025-11-01

### 🎉 Initial Release

#### Features
- **Dual AI Provider Support**
  - OpenAI integration (GPT-4 Vision, GPT-4o, GPT-4o Mini)
  - Google Gemini integration (Gemini 1.5 Pro, Gemini 1.5 Flash, Gemini Pro Vision)
  - User-selectable models with in-app API key management

- **Role-Based Analysis**
  - Predefined roles: Investor, Analyst, Auditor
  - Custom role support
  - Tailored prompts for each role

- **Multiple Analysis Types**
  - Overall Analysis: Comprehensive financial review
  - Risk Analysis: Focus on financial risks and red flags
  - Growth Analysis: Evaluate growth potential and opportunities
  - Profitability Analysis: Deep dive into margins and returns

- **User Interface**
  - Streamlit-based web interface
  - Drag and drop file upload
  - Multiple image support (PNG, JPG, JPEG)
  - Live image preview
  - Customizable prompt editor
  - Quick template switching buttons

- **Export Capabilities**
  - PDF generation with professional formatting
  - Email delivery with HTML formatting
  - Optional PDF attachments for emails

- **Image Processing**
  - Support for PNG, JPG, JPEG formats
  - Maximum file size: 10MB per image
  - Automatic image validation
  - Image information display (optional)
  - Auto-resize for large images (optional)

- **Security & Privacy**
  - API keys not stored (session-only)
  - Images processed in memory only
  - Secure email transmission
  - Gmail App Password support

#### Technical Implementation
- Python 3.8+ support
- Virtual environment setup (wind)
- Modular code structure
- Comprehensive error handling
- Type hints and documentation
- Professional PDF generation using ReportLab
- Email functionality using SMTP

#### Documentation
- English README (README.md)
- Chinese README (README_CN.md)
- Quick Start Guide (QUICKSTART.md)
- Testing Instructions (TESTING.md)
- Environment variable template (.env.example)
- MIT License

#### Scripts & Tools
- macOS launcher script (run.command)
- Requirements file for easy setup
- Git ignore configuration
- Organized project structure

### Included Prompt Templates

#### Overall Analysis Prompts
- Investor-focused: Investment potential, risks, returns
- Analyst-focused: Comprehensive ratios and metrics
- Auditor-focused: Compliance, red flags, audit considerations
- General purpose: Accessible business understanding

#### Specialized Analysis Prompts
- Risk Analysis: Financial, market, operational risks
- Growth Analysis: Revenue growth, market opportunities
- Profitability Analysis: Margins, returns, earnings quality

### Dependencies
- streamlit >= 1.28.0
- openai >= 1.3.0
- google-generativeai >= 0.3.0
- Pillow >= 10.0.0
- reportlab >= 4.0.0
- python-dotenv >= 1.0.0
- python-dateutil >= 2.8.2

### Platform Support
- macOS (fully tested)
- Linux (compatible)
- Windows (compatible)

---

## Future Enhancements (Planned)

### Version 1.1.0 (Future)
- [ ] Claude AI integration
- [ ] Batch processing for multiple reports
- [ ] Historical analysis comparison
- [ ] Data visualization of extracted metrics
- [ ] CSV export of financial metrics
- [ ] Save and load analysis history
- [ ] Custom prompt library
- [ ] Multi-language UI support

### Version 1.2.0 (Future)
- [ ] OCR for scanned documents
- [ ] Direct PDF upload support
- [ ] Enhanced chart/graph recognition
- [ ] Comparative analysis mode
- [ ] API rate limiting and queuing
- [ ] User authentication system
- [ ] Analysis templates marketplace

### Version 2.0.0 (Future)
- [ ] Web deployment version
- [ ] Database integration for history
- [ ] Team collaboration features
- [ ] Advanced analytics dashboard
- [ ] Real-time collaboration
- [ ] Mobile app version

---

## Contributing

We welcome contributions! Potential areas:
- New AI provider integrations
- Additional analysis templates
- Enhanced visualization
- Bug fixes and optimizations
- Documentation improvements
- Localization and translations

---

**Version Numbering**: We follow [Semantic Versioning](https://semver.org/)
- MAJOR.MINOR.PATCH
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)
