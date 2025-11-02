"""
PDF Export Utility
"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from datetime import datetime
import io
import re


class PDFGenerator:
    """Generate PDF reports from analysis results."""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1f4788'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#2c5f99'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Section heading
        self.styles.add(ParagraphStyle(
            name='SectionHeading',
            parent=self.styles['Heading3'],
            fontSize=14,
            textColor=colors.HexColor('#1f4788'),
            spaceAfter=8,
            spaceBefore=16,
            fontName='Helvetica-Bold'
        ))
        
        # Body text
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontSize=11,
            alignment=TA_JUSTIFY,
            spaceAfter=10,
            leading=14
        ))
        
        # Metadata style
        self.styles.add(ParagraphStyle(
            name='Metadata',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=colors.gray,
            spaceAfter=6
        ))
    
    def _clean_text(self, text: str) -> str:
        """Clean and prepare text for PDF."""
        # Replace special characters that might cause issues
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        return text
    
    def _format_analysis_text(self, text: str) -> list:
        """Format analysis text into reportlab flowables."""
        flowables = []
        
        # Split text into lines
        lines = text.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines
            if not line:
                i += 1
                continue
            
            # Handle headings (### or ## or # or **bold**)
            if line.startswith('###'):
                heading_text = line.replace('###', '').strip()
                flowables.append(Paragraph(self._clean_text(heading_text), self.styles['SectionHeading']))
                flowables.append(Spacer(1, 0.1*inch))
                i += 1
                continue
            elif line.startswith('##'):
                heading_text = line.replace('##', '').strip()
                flowables.append(Paragraph(self._clean_text(heading_text), self.styles['CustomSubtitle']))
                flowables.append(Spacer(1, 0.1*inch))
                i += 1
                continue
            elif line.startswith('#'):
                heading_text = line.replace('#', '').strip()
                flowables.append(Paragraph(self._clean_text(heading_text), self.styles['CustomSubtitle']))
                flowables.append(Spacer(1, 0.1*inch))
                i += 1
                continue
            
            # Handle bold text as subheadings (lines that start and end with **)
            if line.startswith('**') and line.endswith('**') and len(line) > 4:
                heading_text = line.replace('**', '').strip()
                flowables.append(Paragraph(self._clean_text(heading_text), self.styles['SectionHeading']))
                flowables.append(Spacer(1, 0.05*inch))
                i += 1
                continue
            
            # Handle bullet points (• or - or * at start)
            if line.startswith('•') or line.startswith('- ') or line.startswith('* '):
                # Collect consecutive bullet points
                bullet_items = []
                while i < len(lines):
                    curr_line = lines[i].strip()
                    if not curr_line:
                        i += 1
                        break
                    if curr_line.startswith('•') or curr_line.startswith('- ') or curr_line.startswith('* '):
                        # Remove bullet marker and clean
                        bullet_text = curr_line.lstrip('•-* ').strip()
                        # Remove any ** bold markers
                        bullet_text = bullet_text.replace('**', '')
                        bullet_items.append(bullet_text)
                        i += 1
                    else:
                        break
                
                # Add bullets with proper spacing
                for bullet_text in bullet_items:
                    para = Paragraph(f"• {self._clean_text(bullet_text)}", self.styles['CustomBody'])
                    flowables.append(para)
                    flowables.append(Spacer(1, 0.05*inch))
                
                flowables.append(Spacer(1, 0.1*inch))
                continue
            
            # Handle numbered lists
            if re.match(r'^\d+\.', line):
                # Collect consecutive numbered items
                numbered_items = []
                while i < len(lines):
                    curr_line = lines[i].strip()
                    if not curr_line:
                        i += 1
                        break
                    if re.match(r'^\d+\.', curr_line):
                        # Clean numbered text
                        numbered_text = re.sub(r'^\d+\.\s*', '', curr_line)
                        numbered_text = numbered_text.replace('**', '')
                        numbered_items.append((len(numbered_items) + 1, numbered_text))
                        i += 1
                    else:
                        break
                
                # Add numbered items
                for num, text in numbered_items:
                    para = Paragraph(f"{num}. {self._clean_text(text)}", self.styles['CustomBody'])
                    flowables.append(para)
                    flowables.append(Spacer(1, 0.05*inch))
                
                flowables.append(Spacer(1, 0.1*inch))
                continue
            
            # Regular paragraph - clean and add
            # Remove inline ** bold markers
            clean_line = line.replace('**', '')
            flowables.append(Paragraph(self._clean_text(clean_line), self.styles['CustomBody']))
            flowables.append(Spacer(1, 0.1*inch))
            i += 1
        
        return flowables
    
    def generate_pdf(self, analysis_data: dict, filename: str = None) -> bytes:
        """
        Generate PDF from analysis data.
        
        Args:
            analysis_data: Dictionary containing analysis results
            filename: Optional filename for the PDF
            
        Returns:
            PDF as bytes
        """
        buffer = io.BytesIO()
        
        # Create PDF document
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=1*inch,
            bottomMargin=0.75*inch
        )
        
        # Container for the 'Flowable' objects
        elements = []
        
        # Title
        title = Paragraph("Financial Report Analysis", self.styles['CustomTitle'])
        elements.append(title)
        elements.append(Spacer(1, 0.3*inch))
        
        # Metadata table
        metadata = [
            ['Generated:', datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            ['AI Provider:', analysis_data.get('provider', 'N/A').upper()],
            ['Model:', analysis_data.get('model', 'N/A')],
            ['User Role:', analysis_data.get('role', 'N/A')],
            ['Images Analyzed:', str(analysis_data.get('image_count', 0))]
        ]
        
        metadata_table = Table(metadata, colWidths=[1.5*inch, 4.5*inch])
        metadata_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.grey),
            ('TEXTCOLOR', (1, 0), (1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        
        elements.append(metadata_table)
        elements.append(Spacer(1, 0.4*inch))
        
        # Analysis section
        elements.append(Paragraph("Analysis Results", self.styles['CustomSubtitle']))
        elements.append(Spacer(1, 0.2*inch))
        
        # Add formatted analysis text
        analysis_text = analysis_data.get('analysis', 'No analysis available.')
        analysis_elements = self._format_analysis_text(analysis_text)
        elements.extend(analysis_elements)
        
        # Build PDF
        doc.build(elements)
        
        # Get PDF bytes
        pdf_bytes = buffer.getvalue()
        buffer.close()
        
        return pdf_bytes
