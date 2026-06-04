from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from services.analytics import calculate_dashboard_metrics
from models.user import User
import io
from datetime import datetime

def generate_portfolio_pdf(user_id):
    user = User.get(user_id)
    metrics = calculate_dashboard_metrics(user_id)
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    
    elements = []
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    title_style.alignment = 1 # Center
    normal_style = styles['Normal']
    
    # Title
    elements.append(Paragraph(f"StockWise Portfolio Report", title_style))
    elements.append(Spacer(1, 12))
    
    # User Info
    elements.append(Paragraph(f"<b>User:</b> {user.name} ({user.email})", normal_style))
    elements.append(Paragraph(f"<b>Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}", normal_style))
    elements.append(Spacer(1, 20))
    
    # Summary
    elements.append(Paragraph("<b>Portfolio Summary</b>", styles['Heading2']))
    summary_data = [
        ['Total Investment', f"${metrics['total_investment']:.2f}"],
        ['Current Value', f"${metrics['current_value']:.2f}"],
        ['Total Profit/Loss', f"${metrics['total_profit']:.2f}"],
        ['Number of Stocks', str(metrics['num_stocks'])],
        ['Best Performer', metrics['best_stock']]
    ]
    
    summary_table = Table(summary_data, colWidths=[200, 200])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 20))
    
    # Details
    elements.append(Paragraph("<b>Portfolio Details</b>", styles['Heading2']))
    
    if metrics['portfolio_data']:
        headers = ['Symbol', 'Quantity', 'Buy Price', 'Current Price', 'Profit/Loss']
        details_data = [headers]
        
        for item in metrics['portfolio_data']:
            details_data.append([
                item['symbol'],
                str(item['quantity']),
                f"${item['buy_price']:.2f}",
                f"${item['current_price']:.2f}",
                f"${item['profit']:.2f} ({item['profit_pct']:.1f}%)"
            ])
            
        details_table = Table(details_data, colWidths=[80, 70, 90, 90, 150])
        details_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0d6efd')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),
        ]))
        elements.append(details_table)
    else:
        elements.append(Paragraph("No stocks in portfolio.", normal_style))
        
    doc.build(elements)
    buffer.seek(0)
    return buffer
