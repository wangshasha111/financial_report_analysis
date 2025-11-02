"""
Email Utility for sending analysis reports
This version sends emails FROM the application's configured email account
TO the recipient specified by the user.
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
from typing import Optional, List
import os
import re


class EmailSender:
    """Handle email sending functionality from the application."""
    
    def __init__(self, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587):
        """
        Initialize Email Sender.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        
        # Application's email credentials (from environment variables or config)
        # For production, set these as environment variables:
        # export APP_EMAIL="your-app-email@gmail.com"
        # export APP_EMAIL_PASSWORD="your-app-password"
        self.app_email = os.getenv('APP_EMAIL', '')
        self.app_email_password = os.getenv('APP_EMAIL_PASSWORD', '')
    
    def send_analysis_email(
        self,
        recipient_emails: List[str],
        analysis_data: dict,
        pdf_bytes: Optional[bytes] = None,
        sender_email: str = None,
        sender_password: str = None
    ) -> tuple[bool, str]:
        """
        Send analysis results via email FROM the application TO recipient(s).
        
        Args:
            recipient_emails: List of recipient email addresses
            analysis_data: Dictionary containing analysis results
            pdf_bytes: Optional PDF attachment bytes
            sender_email: Optional override for app email (for testing/custom setup)
            sender_password: Optional override for app password (for testing/custom setup)
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        # Use provided credentials or fall back to app defaults
        from_email = sender_email or self.app_email
        from_password = sender_password or self.app_email_password
        
        # Validate we have credentials
        if not from_email or not from_password:
            return False, """Email credentials not configured. 
            
Please set up the application's email credentials:
1. Create a Gmail account for the application
2. Enable 2-factor authentication
3. Create an App Password (Google Account > Security > App Passwords)
4. Set environment variables:
   export APP_EMAIL="your-app-email@gmail.com"
   export APP_EMAIL_PASSWORD="your-16-char-app-password"

Or provide credentials in the email form for testing."""
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = f"Financial Analysis AI <{from_email}>"
            msg['To'] = ", ".join(recipient_emails)
            msg['Subject'] = f"Financial Report Analysis - {datetime.now().strftime('%Y-%m-%d')}"
            
            # Email body
            body = self._create_email_body(analysis_data)
            msg.attach(MIMEText(body, 'html'))
            
            # Attach PDF if provided
            if pdf_bytes:
                pdf_attachment = MIMEApplication(pdf_bytes, _subtype='pdf')
                pdf_attachment.add_header(
                    'Content-Disposition', 
                    'attachment', 
                    filename=f'Financial_Analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
                )
                msg.attach(pdf_attachment)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(from_email, from_password)
                server.send_message(msg)
            
            recipients_str = ", ".join(recipient_emails)
            return True, f"Email sent successfully to {recipients_str}!"
            
        except smtplib.SMTPAuthenticationError:
            return False, "Authentication failed. Please check email credentials. For Gmail, use an App Password."
        except smtplib.SMTPException as e:
            return False, f"SMTP error: {str(e)}"
        except Exception as e:
            return False, f"Failed to send email: {str(e)}"
    
    def _create_email_body(self, analysis_data: dict) -> str:
        """
        Create HTML email body from analysis data.
        
        Args:
            analysis_data: Dictionary containing analysis results
            
        Returns:
            HTML formatted email body
        """
        analysis_text = analysis_data.get('analysis', 'No analysis available.')
        provider = analysis_data.get('provider', 'N/A').upper()
        model = analysis_data.get('model', 'N/A')
        role = analysis_data.get('role', 'N/A')
        image_count = analysis_data.get('image_count', 0)
        
        # Convert markdown-style formatting to HTML
        analysis_html = self._markdown_to_html(analysis_text)
        
        html = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background-color: #1f4788;
                    color: white;
                    padding: 20px;
                    text-align: center;
                    border-radius: 5px;
                }}
                .metadata {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    margin: 20px 0;
                    border-left: 4px solid #1f4788;
                }}
                .metadata-item {{
                    margin: 5px 0;
                }}
                .analysis {{
                    margin-top: 20px;
                    padding: 20px;
                    background-color: white;
                }}
                h2 {{
                    color: #1f4788;
                    border-bottom: 2px solid #1f4788;
                    padding-bottom: 10px;
                }}
                h3 {{
                    color: #2c5f99;
                    margin-top: 20px;
                }}
                .footer {{
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #ddd;
                    font-size: 12px;
                    color: #666;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>📊 Financial Report Analysis</h1>
            </div>
            
            <div class="metadata">
                <div class="metadata-item"><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>
                <div class="metadata-item"><strong>AI Provider:</strong> {provider}</div>
                <div class="metadata-item"><strong>Model:</strong> {model}</div>
                <div class="metadata-item"><strong>User Role:</strong> {role}</div>
                <div class="metadata-item"><strong>Images Analyzed:</strong> {image_count}</div>
            </div>
            
            <div class="analysis">
                <h2>Analysis Results</h2>
                {analysis_html}
            </div>
            
            <div class="footer">
                <p>This analysis was generated using AI and should be reviewed by qualified professionals.</p>
                <p>Generated by Financial Report Analysis AI Tool</p>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def _markdown_to_html(self, text: str) -> str:
        """
        Convert simple markdown to HTML with proper formatting.
        
        Args:
            text: Markdown formatted text
            
        Returns:
            HTML formatted text
        """
        lines = text.split('\n')
        formatted_lines = []
        in_list = False
        
        for line in lines:
            stripped = line.strip()
            
            if not stripped:
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                formatted_lines.append('<br>')
                continue
            
            # Handle headers
            if stripped.startswith('### '):
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                formatted_lines.append(f'<h3>{stripped[4:]}</h3>')
            elif stripped.startswith('## '):
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                formatted_lines.append(f'<h3>{stripped[3:]}</h3>')
            elif stripped.startswith('# '):
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                formatted_lines.append(f'<h2>{stripped[2:]}</h2>')
            # Handle bullet points
            elif stripped.startswith('• ') or stripped.startswith('- ') or stripped.startswith('* '):
                bullet_text = stripped.lstrip('•-* ').strip()
                # Remove ** bold markers
                bullet_text = bullet_text.replace('**', '<strong>').replace('**', '</strong>')
                # Fix any unpaired tags
                if bullet_text.count('<strong>') != bullet_text.count('</strong>'):
                    bullet_text = bullet_text.replace('<strong>', '').replace('</strong>', '')
                
                if not in_list:
                    formatted_lines.append('<ul style="margin-left: 20px; margin-bottom: 10px;">')
                    in_list = True
                formatted_lines.append(f'<li style="margin-bottom: 5px;">{bullet_text}</li>')
            # Handle numbered lists
            elif re.match(r'^\d+\.', stripped):
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                formatted_lines.append(f'<p>{stripped}</p>')
            # Handle bold text (lines that are fully wrapped in **)
            elif stripped.startswith('**') and stripped.endswith('**') and len(stripped) > 4:
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                formatted_lines.append(f'<h4 style="color: #2c5f99; margin-top: 15px;">{stripped[2:-2]}</h4>')
            else:
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                # Handle inline bold
                para = stripped.replace('**', '<strong>').replace('**', '</strong>')
                # Fix any unpaired tags
                if para.count('<strong>') != para.count('</strong>'):
                    para = para.replace('<strong>', '').replace('</strong>', '')
                formatted_lines.append(f'<p style="margin-bottom: 8px;">{para}</p>')
        
        # Close list if still open
        if in_list:
            formatted_lines.append('</ul>')
        
        return '\n'.join(formatted_lines)
