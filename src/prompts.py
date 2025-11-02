"""
Default prompts for different analysis types

OUTPUT QUALITY GUIDELINES:
When analyzing financial documents (annual reports, balance sheets, earnings reports), ensure:

1. COMPLETENESS: Cover all key financial statements (Income Statement, Balance Sheet, Cash Flow)
2. SPECIFICITY: Use actual numbers from documents with proper units (EUR/USD million, %, basis points)
3. COMPARISONS: Include period-over-period analysis (YoY, QoQ) wherever data is available
4. STRUCTURE: Follow clear sections with headers and bullet points
5. CONTEXT: Explain what metrics mean and why they matter
6. VISUAL ANALYSIS: Interpret all charts, graphs, and tables thoroughly
7. RATIOS: Calculate and present relevant financial ratios with formulas
8. TRENDS: Identify patterns, growth rates, and significant changes
9. RISKS: Address challenges, risks, and mitigation strategies
10. OUTLOOK: Include management commentary and forward-looking statements

REFERENCE EXAMPLE OUTPUT FORMAT:
- Use headers with clear section titles
- Present metrics with comparisons: "EUR 690 million, down from EUR 759 million in Q3 2023"
- Include percentages and basis points for precision
- Cite specific figures, not estimates
- Structure information hierarchically
- Highlight significant variances (>5% changes)
"""

PROMPTS = {
    "Overall Analysis": {
        "Investor": """As an AI assistant for investors, analyze these financial documents and provide a comprehensive summary following this structure:

**SUMMARY HEADER**
Provide a brief title with company name, document type, and period (e.g., "Q3 2024 Quarterly Report")

**1. KEY FINANCIAL METRICS**
Extract and present critical performance indicators with comparative data:
   • Net Profit/Income (with YoY or QoQ comparison)
   • Earnings Per Share (EPS)
   • Revenue (total and growth %)
   • Return on Equity (ROE)
   • Profit Margins (gross, operating, net)
   • Debt-to-Equity Ratio
   • Any other key ratios mentioned

**2. INCOME AND EXPENSES ANALYSIS**
   • Net Interest Income (if applicable)
   • Revenue breakdown by segments/sources
   • Operating expenses and trends
   • Fee and commission income
   • Cost structure and efficiency ratios
   • Year-over-year or quarter-over-quarter comparisons

**3. BALANCE SHEET HIGHLIGHTS**
   • Total Assets and changes
   • Loans and Advances to Customers
   • Client Deposits and trends
   • Shareholders' Equity
   • Working Capital position
   • Notable changes from previous periods

**4. CASH FLOW AND LIQUIDITY**
   • Operating cash flow
   • Free cash flow
   • Capital expenditures
   • Liquidity ratios
   • Cash position and trends

**5. CREDIT QUALITY & RISK METRICS** (if applicable)
   • Cost of Risk
   • Non-performing loans ratio
   • Loan loss provisions
   • Credit quality indicators

**6. OPERATIONAL PERFORMANCE**
   • Business segment performance
   • Market share and competitive position
   • Customer metrics and growth
   • Operational efficiency indicators
   • Notable achievements or recognitions

**7. STRATEGIC INITIATIVES & UPDATES**
   • Major strategic priorities
   • New products/services launched
   • Technology and innovation investments
   • Sustainability initiatives
   • Acquisitions, partnerships, or expansions

**8. MARKET CONDITIONS & OUTLOOK**
   • Current market environment
   • Management's commentary on outlook
   • Future guidance or projections
   • Industry trends affecting the business
   • Macroeconomic factors (inflation, interest rates, employment)

**9. RISKS AND CHALLENGES**
   • Identified risks (regulatory, market, operational)
   • External factors impacting business
   • Management's risk mitigation strategies
   • Potential headwinds or uncertainties

**10. SHAREHOLDER INFORMATION** (if available)
   • Dividend declarations or payments
   • Stock performance
   • Share buyback programs
   • Capital allocation strategy

**11. VISUAL DATA INTERPRETATION**
Analyze all charts, graphs, and tables, explaining:
   • Trends shown in visualizations
   • Comparisons and benchmarks
   • Significant patterns or anomalies

**12. INVESTMENT PERSPECTIVE**
   • Overall financial health assessment
   • Strengths and competitive advantages
   • Weaknesses and concerns
   • Investment attractiveness summary

**OUTPUT FORMAT**: Use clear headers, bullet points, and specific numbers with units (EUR million, %, basis points). Include actual figures from the documents, not estimates. Compare current vs. previous periods wherever data is available.""",

        "Analyst": """As a financial analyst, conduct a comprehensive analysis of these financial documents following this detailed structure:

**EXECUTIVE SUMMARY**
Company name, report type, period, and brief overview of financial position

**1. KEY FINANCIAL STATEMENTS SUMMARY**

A. **Income Statement Highlights**
   • Total Revenue (with % change YoY/QoQ)
   • Gross Profit and Gross Margin %
   • Operating Income and Operating Margin %
   • Net Income and Net Margin %
   • Earnings Per Share (EPS) - basic and diluted
   • EBITDA and EBITDA margin

B. **Balance Sheet Analysis**
   • Total Assets (breakdown: current vs. non-current)
   • Total Liabilities (short-term vs. long-term)
   • Shareholders' Equity
   • Working Capital (current assets - current liabilities)
   • Notable changes from previous period

C. **Cash Flow Statement Review**
   • Operating Cash Flow
   • Investing Cash Flow (capex, acquisitions)
   • Financing Cash Flow (debt, dividends, buybacks)
   • Free Cash Flow (OCF - Capex)
   • Cash and cash equivalents position

**2. COMPREHENSIVE FINANCIAL RATIOS**

A. **Profitability Ratios**
   • Return on Assets (ROA) = Net Income / Total Assets
   • Return on Equity (ROE) = Net Income / Shareholders' Equity
   • Return on Invested Capital (ROIC)
   • Gross Profit Margin = Gross Profit / Revenue
   • Operating Profit Margin = Operating Income / Revenue
   • Net Profit Margin = Net Income / Revenue

B. **Liquidity Ratios**
   • Current Ratio = Current Assets / Current Liabilities
   • Quick Ratio = (Current Assets - Inventory) / Current Liabilities
   • Cash Ratio = Cash / Current Liabilities
   • Operating Cash Flow Ratio

C. **Efficiency Ratios**
   • Asset Turnover = Revenue / Total Assets
   • Inventory Turnover (if applicable)
   • Receivables Turnover
   • Days Sales Outstanding (DSO)
   • Cash Conversion Cycle

D. **Leverage Ratios**
   • Debt-to-Equity = Total Debt / Shareholders' Equity
   • Debt-to-Assets = Total Debt / Total Assets
   • Interest Coverage = EBIT / Interest Expense
   • Debt Service Coverage Ratio

**3. REVENUE & EARNINGS DEEP DIVE**
   • Revenue by business segment/product line
   • Geographic revenue distribution
   • Revenue growth drivers
   • Revenue quality assessment
   • Earnings sustainability analysis
   • Non-recurring items identification
   • Core vs. one-time earnings

**4. COST STRUCTURE & MARGIN ANALYSIS**
   • Fixed vs. variable costs breakdown
   • Operating leverage analysis
   • Cost efficiency trends
   • R&D and marketing expenses as % of revenue
   • Administrative costs analysis
   • Margin improvement/deterioration drivers

**5. CREDIT QUALITY & RISK ASSESSMENT** (if applicable)
   • Non-performing loans (NPL) ratio
   • Loan loss provisions
   • Credit risk indicators
   • Risk-weighted assets
   • Capital adequacy ratios (CET1, Tier 1)

**6. SEGMENT PERFORMANCE ANALYSIS**
   • Revenue and profit by segment
   • Segment margins and trends
   • Growth rates by division
   • Cross-segment comparisons

**7. VISUAL DATA ANALYSIS**
For all charts, graphs, and tables:
   • Trend analysis and direction
   • Rate of change calculations
   • Inflection points or anomalies
   • Year-over-year and sequential comparisons
   • Visual benchmarks against targets

**8. COMPARATIVE & BENCHMARK ANALYSIS**
   • Industry average comparisons (if data available)
   • Peer group analysis
   • Historical trend analysis (3-5 year view if data exists)
   • Best-in-class benchmarking

**9. OPERATIONAL METRICS**
   • Customer acquisition/retention metrics
   • Market share data
   • Productivity indicators
   • Capacity utilization
   • Unit economics

**10. FORWARD-LOOKING INDICATORS**
   • Guidance provided by management
   • Growth projections
   • Capital expenditure plans
   • Expected market conditions

**OUTPUT REQUIREMENTS**:
- Use specific numbers with proper units (million, billion, %, basis points)
- Show calculations for key ratios
- Include period-over-period comparisons
- Highlight significant variances (>5% change)
- Use tables for ratio summaries where appropriate
- Cite specific page references if visible in documents""",

        "Auditor": """As an auditor, review these financial documents with focus on compliance, accuracy, and risk identification:

**AUDIT SUMMARY HEADER**
Document type, period, and scope of review

**1. COMPLIANCE & ACCOUNTING STANDARDS**
   • Accounting framework used (GAAP/IFRS/other)
   • Compliance with applicable standards
   • Disclosure completeness assessment
   • Consistency with prior period presentations
   • Changes in accounting policies or estimates
   • Adoption of new accounting standards

**2. FINANCIAL STATEMENT ACCURACY**

A. **Income Statement Review**
   • Revenue recognition policies and compliance
   • Expense classification and matching principle
   • Unusual or non-recurring items identification
   • Period cutoff accuracy
   • Related party transactions

B. **Balance Sheet Verification**
   • Asset valuation methods and appropriateness
   • Liability completeness and accuracy
   • Equity transactions and disclosures
   • Off-balance sheet items
   • Contingent liabilities

C. **Cash Flow Statement**
   • Reconciliation with income statement
   • Non-cash adjustments accuracy
   • Cash classification (operating/investing/financing)

**3. RED FLAGS & ANOMALIES IDENTIFICATION**
   • Unusual transaction patterns
   • Aggressive accounting treatments
   • Revenue recognition timing issues
   • Expense deferrals or capitalizations
   • Related party transactions without proper disclosure
   • Inconsistencies between statements
   • Unexplained variances or trends
   • Significant one-time adjustments

**4. ASSET QUALITY ASSESSMENT**

A. **Tangible Assets**
   • Property, plant, and equipment valuation
   • Depreciation methods and rates
   • Impairment testing indicators

B. **Intangible Assets**
   • Goodwill valuation and impairment testing
   • Intangible asset recognition criteria
   • Amortization policies
   • Fair value estimates

C. **Financial Assets**
   • Investment classification and valuation
   • Allowance for credit losses adequacy
   • Impairment provisions

**5. LIABILITY & CONTINGENCY REVIEW**
   • Completeness of liability recording
   • Debt covenants compliance
   • Warranty and guarantee provisions
   • Litigation and claims disclosures
   • Contingent liabilities adequacy
   • Lease obligations (ASC 842/IFRS 16 compliance)

**6. REVENUE RECOGNITION ANALYSIS**
   • Revenue recognition policy description
   • Five-step model compliance (ASC 606/IFRS 15)
   • Performance obligations identification
   • Transaction price allocation
   • Timing of revenue recognition
   • Deferred revenue appropriateness
   • Contract asset/liability presentation

**7. INTERNAL CONTROLS ASSESSMENT**
   • Financial reporting quality indicators
   • Segregation of duties evidence
   • Authorization and approval processes
   • Reconciliation procedures
   • IT controls and system reliability
   • Management override risks

**8. RISK MANAGEMENT DISCLOSURES**
   • Financial risk exposures (market, credit, liquidity)
   • Risk management framework description
   • Hedging activities and effectiveness
   • Sensitivity analysis disclosures
   • Concentration risks

**9. NOTES & FOOTNOTES ANALYSIS**
   • Significant accounting policies disclosure
   • Critical accounting estimates and judgments
   • Segment reporting adequacy
   • Fair value measurements disclosure
   • Financial instrument disclosures
   • Subsequent events
   • Going concern assessment

**10. GOVERNANCE & RELATED PARTIES**
   • Related party identification and disclosure
   • Key management personnel compensation
   • Board and committee structure
   • Audit committee oversight indicators
   • External auditor information

**11. CREDIT QUALITY METRICS** (for financial institutions)
   • Non-performing loan ratios and trends
   • Provision coverage ratios
   • Expected credit loss (ECL) model compliance
   • Stage classification appropriateness
   • Forbearance and modification policies

**12. REGULATORY COMPLIANCE** (if applicable)
   • Capital adequacy requirements (Basel III/IV)
   • Regulatory reporting consistency
   • Compliance with banking regulations
   • Solvency requirements
   • Pending regulatory changes impact

**13. DATA INTEGRITY VERIFICATION**
   • Cross-statement reconciliation
   • Mathematical accuracy check
   • Consistency of numbers across sections
   • Footnote cross-references validation
   • Chart and table data accuracy

**14. AREAS REQUIRING ATTENTION**
Prioritized list of:
   • High-risk areas needing further investigation
   • Material misstatement risks
   • Disclosure deficiencies
   • Control weaknesses observed
   • Recommendations for improvement

**15. VISUAL DATA AUDIT**
   • Verify chart data matches tabular data
   • Assess presentation fairness
   • Check for misleading visualizations
   • Validate trend line accuracy

**OUTPUT FORMAT**:
- Flag issues with severity levels (High/Medium/Low)
- Cite specific disclosure references
- Note deviations from standards
- Provide specific page/section references
- Use audit terminology appropriately
- Maintain professional skepticism throughout analysis""",

        "Other": """Analyze these financial documents and provide a comprehensive business-friendly summary:

**DOCUMENT OVERVIEW**
Company name, report type (Annual Report/Quarterly Report/Earnings Report), and period covered

**1. EXECUTIVE SUMMARY**
Brief 2-3 sentence overview of the company's financial position and key highlights

**2. KEY FINANCIAL METRICS**
Present the most important numbers in an easy-to-understand format:

A. **Performance Indicators**
   • Total Revenue: [Amount] (Change from previous period: +/- X%)
   • Net Income/Profit: [Amount] (Change: +/- X%)
   • Earnings Per Share (EPS): [Amount]
   • Profit Margin: X% (how much profit per dollar of sales)

B. **Financial Position**
   • Total Assets: [Amount]
   • Total Liabilities: [Amount]
   • Shareholders' Equity: [Amount]
   • Debt-to-Equity Ratio: X (how much debt vs. equity)

C. **Returns & Efficiency**
   • Return on Equity (ROE): X% (how well company uses shareholder money)
   • Return on Assets (ROA): X% (how efficiently assets generate profit)
   • Operating Margin: X%

**3. INCOME & EXPENSES BREAKDOWN**
   • Where money came from (revenue sources):
     - Product/service line revenues
     - Geographic breakdown if available
   • Where money went (major expenses):
     - Cost of goods/services
     - Operating expenses
     - Interest and taxes
   • Comparison with previous period (better/worse and by how much)

**4. BALANCE SHEET SNAPSHOT**
Explain the company's financial position in simple terms:
   • What the company owns (Assets):
     - Cash and investments: [Amount]
     - Property and equipment: [Amount]
     - Other significant assets
   • What the company owes (Liabilities):
     - Short-term obligations: [Amount]
     - Long-term debt: [Amount]
   • Net worth (Equity): [Amount]
   • Changes from last period

**5. CASH FLOW SUMMARY**
Where cash came from and where it went:
   • Cash from operations: [Amount] (day-to-day business)
   • Cash from investing: [Amount] (buying/selling assets)
   • Cash from financing: [Amount] (debt, dividends, stock)
   • Net change in cash: [Amount]
   • Ending cash position: [Amount]

**6. BUSINESS PERFORMANCE**
   • Market position and competitive standing
   • Customer growth or retention metrics
   • Product/service performance highlights
   • Operational achievements
   • Awards, recognitions, or milestones

**7. STRATEGIC INITIATIVES**
What the company is working on:
   • Major projects or investments
   • New products or services launched
   • Technology improvements
   • Expansion plans (new markets, acquisitions)
   • Sustainability and social responsibility efforts

**8. MARKET CONDITIONS & OUTLOOK**
   • Current business environment
   • Industry trends affecting the company
   • Management's view of the future
   • Opportunities ahead
   • Economic factors (inflation, interest rates, employment)

**9. RISKS & CHALLENGES**
What could impact the business:
   • Identified risk factors
   • External challenges (regulation, competition, economy)
   • How management plans to address these risks
   • Potential obstacles to growth

**10. SHAREHOLDER INFORMATION**
   • Dividend payments (if any): [Amount per share]
   • Stock performance mention
   • Share buyback programs
   • How the company plans to use its profits

**11. CHARTS & GRAPHS EXPLAINED**
For each visual element in the documents:
   • What it shows (in plain language)
   • Key trends or patterns
   • What it means for the business
   • Notable changes or highlights

**12. BOTTOM LINE ASSESSMENT**
   • Financial Health: Strong/Moderate/Weak (with explanation)
   • Key Strengths: What's going well
   • Key Concerns: What needs attention
   • Overall Outlook: Positive/Neutral/Cautious

**OUTPUT STYLE**:
- Use clear, jargon-free language
- Explain technical terms when used
- Include specific numbers with context
- Use comparisons to previous periods
- Highlight significant changes (note if >5% change)
- Present information in bullet points and short paragraphs
- Make it accessible to non-financial professionals"""
    },

    "Risk Analysis": {
        "Investor": """Focus on investment risks in these financial documents:

1. **Financial Risks**: Analyze liquidity, solvency, and profitability risks
2. **Market Risks**: Identify exposure to market volatility, competition, and economic cycles
3. **Operational Risks**: Examine operational efficiency and potential disruptions
4. **Regulatory Risks**: Note any compliance or regulatory concerns
5. **Risk Mitigation**: Assess management's risk mitigation strategies

Provide a risk score and specific risk factors affecting investment decisions.""",

        "Analyst": """Conduct detailed risk assessment:

1. **Quantitative Risk Metrics**: Calculate risk ratios and statistical measures
2. **Credit Risk**: Debt sustainability and default probability
3. **Market Risk**: Beta, volatility, and market correlation
4. **Operational Risk**: Business model vulnerabilities
5. **Scenario Analysis**: Best/worst case financial scenarios

Include mathematical risk models where applicable.""",

        "Auditor": """Audit-focused risk review:

1. **Material Misstatement Risks**: Areas prone to errors or fraud
2. **Going Concern Issues**: Liquidity and solvency risks
3. **Internal Control Risks**: Weaknesses in financial controls
4. **Compliance Risks**: Regulatory and legal exposure
5. **Audit Recommendations**: Risk mitigation priorities

Focus on risks requiring audit attention or disclosure.""",

        "Other": """Identify and explain key risks:

1. **Major Risk Categories**: Financial, operational, market, and regulatory risks
2. **Risk Impact**: Potential consequences of each risk
3. **Warning Signs**: Current indicators of risk materialization
4. **Risk Trends**: Whether risks are increasing or decreasing

Present in simple, understandable terms."""
    },

    "Growth Analysis": {
        "Investor": """Analyze growth potential and opportunities:

1. **Historical Growth**: Revenue, profit, and market share growth trends
2. **Growth Drivers**: Key factors driving company growth
3. **Market Opportunities**: Expansion possibilities and new markets
4. **Competitive Position**: Market position and advantages
5. **Investment in Growth**: R&D, capex, and strategic investments
6. **Growth Sustainability**: Assessment of long-term growth prospects

Evaluate if the company presents a strong growth investment opportunity.""",

        "Analyst": """Comprehensive growth analysis:

1. **Growth Metrics**: CAGR, growth rates across all financial metrics
2. **Segment Performance**: Growth by business unit/product line
3. **Market Share Analysis**: Competitive positioning and trends
4. **Growth Quality**: Organic vs. inorganic growth
5. **Investment Efficiency**: ROIC, payback periods, growth ROI
6. **Forward Projections**: Growth sustainability and forecasting

Provide detailed quantitative growth assessment.""",

        "Auditor": """Review growth-related disclosures:

1. **Revenue Growth Verification**: Legitimacy of reported growth
2. **Acquisition Accounting**: Impact of M&A on growth figures
3. **Organic Growth Analysis**: True business performance
4. **Growth Investment Audit**: Capex and R&D effectiveness
5. **Future Commitments**: Obligations related to growth initiatives

Ensure growth figures are accurate and properly disclosed.""",

        "Other": """Evaluate growth prospects:

1. **Growth Story**: Overall growth trajectory and trends
2. **Success Factors**: What's driving growth
3. **Growth Challenges**: Obstacles to sustained growth
4. **Future Outlook**: Growth expectations and potential

Explain growth prospects in accessible terms."""
    },

    "Profitability Analysis": {
        "Investor": """Analyze profitability and returns:

1. **Profit Margins**: Gross, operating, and net profit margins
2. **Return Metrics**: ROE, ROA, ROIC trends
3. **Earnings Quality**: Sustainability and composition of earnings
4. **Dividend Capacity**: Ability to generate shareholder returns
5. **Profitability Trends**: Historical and projected profitability
6. **Peer Comparison**: How profitability compares to competitors

Assess if the company generates attractive returns for investors.""",

        "Analyst": """Deep-dive profitability analysis:

1. **Margin Analysis**: Detailed breakdown of all margin levels
2. **Cost Structure**: Fixed vs. variable costs, operating leverage
3. **Profitability by Segment**: Which units drive profits
4. **DuPont Analysis**: ROE decomposition
5. **Earnings Quality Metrics**: Accruals, cash conversion
6. **Pricing Power**: Ability to maintain/improve margins

Provide comprehensive profitability assessment with calculations.""",

        "Auditor": """Audit profitability reporting:

1. **Revenue Recognition**: Accuracy of revenue timing
2. **Cost Allocation**: Proper expense matching
3. **Extraordinary Items**: One-time impacts on profitability
4. **Profit Quality Indicators**: Sustainability of reported profits
5. **Consistency**: Profitability accounting consistency

Verify accuracy of profitability disclosures.""",

        "Other": """Understand profit generation:

1. **Basic Profitability**: Is the company making money?
2. **Profit Trends**: Improving or declining profitability
3. **Profit Sources**: Where profits come from
4. **Profit Margin Health**: How margins compare
5. **Sustainability**: Can current profitability continue?

Explain profitability in simple terms."""
    }
}


def get_prompt(analysis_type: str, user_role: str) -> str:
    """
    Get the appropriate prompt based on analysis type and user role.
    
    Args:
        analysis_type: Type of analysis to perform
        user_role: User's role (Investor, Analyst, Auditor, Other)
        
    Returns:
        The appropriate prompt text
    """
    if analysis_type in PROMPTS and user_role in PROMPTS[analysis_type]:
        return PROMPTS[analysis_type][user_role]
    else:
        # Default to Overall Analysis for the given role
        return PROMPTS["Overall Analysis"].get(user_role, PROMPTS["Overall Analysis"]["Other"])


def get_analysis_types() -> list:
    """Get list of available analysis types."""
    return list(PROMPTS.keys())
