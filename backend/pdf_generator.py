from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from io import BytesIO
import requests
import base64
import re




def generate_topic_pdf(topic_data):
    """Generate a comprehensive PDF with topic info, diagram, and equations."""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch, rightMargin=0.5*inch, leftMargin=0.5*inch)
    elements = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor('#6366f1'),
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#4f46e5'),
        spaceBefore=16,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    subsection_style = ParagraphStyle(
        'Subsection',
        parent=styles['Heading3'],
        fontSize=13,
        textColor=colors.HexColor('#333333'),
        spaceBefore=10,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=8
    )
    
    math_style = ParagraphStyle(
        'Math',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        leftIndent=20,
        spaceBefore=8,
        spaceAfter=8,
        textColor=colors.HexColor('#1e40af'),
        fontName='Courier'
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Normal'],
        fontSize=8,
        leading=10,
        leftIndent=15,
        spaceBefore=6,
        spaceAfter=6,
        fontName='Courier',
        textColor=colors.HexColor('#374151'),
        backColor=colors.HexColor('#f3f4f6')
    )
    
    # Title Page
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph(f"📚 {topic_data.get('title', 'Topic')}", title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Summary
    if topic_data.get('summary'):
        elements.append(Paragraph("Executive Summary", section_style))
        elements.append(Paragraph(topic_data['summary'], body_style))
        elements.append(Spacer(1, 0.1*inch))
    
    # Page break after summary
    elements.append(PageBreak())
    
    # Beginner Explanation
    if topic_data.get('beginner_explanation'):
        elements.append(Paragraph("🌱 Beginner Explanation", section_style))
        # Clean up markdown
        beginner_text = clean_markdown(topic_data['beginner_explanation'])
        elements.append(Paragraph(beginner_text, body_style))
        elements.append(Spacer(1, 0.15*inch))
    
    # Key Takeaways
    if topic_data.get('key_takeaways'):
        elements.append(Paragraph("💡 Key Takeaways", subsection_style))
        for takeaway in topic_data['key_takeaways']:
            elements.append(Paragraph(f"• {takeaway}", body_style))
        elements.append(Spacer(1, 0.1*inch))
    
    # Core Mechanics
    if topic_data.get('core_mechanics'):
        elements.append(Paragraph("⚙️ Core Mechanics", section_style))
        mechanics_text = clean_markdown(topic_data['core_mechanics'])
        elements.append(Paragraph(mechanics_text, body_style))
        elements.append(Spacer(1, 0.15*inch))
    
    # Advanced Concepts
    if topic_data.get('advanced_concepts'):
        elements.append(Paragraph("🚀 Advanced Concepts", section_style))
        advanced_text = clean_markdown(topic_data['advanced_concepts'])
        elements.append(Paragraph(advanced_text, body_style))
        elements.append(Spacer(1, 0.15*inch))
    
    # Page break before equations
    elements.append(PageBreak())
    
    # Mathematical Equations
    elements.append(Paragraph("📐 Mathematical Foundation", section_style))
    elements.append(Paragraph("The following equations and formulas are fundamental to understanding this topic:", body_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Extract or generate equations
    equations = extract_equations(topic_data)
    if equations:
        for i, eq in enumerate(equations, 1):
            elements.append(Paragraph(f"<b>Equation {i}:</b> {eq['name']}", subsection_style))
            elements.append(Paragraph(eq['formula'], math_style))
            if eq.get('description'):
                elements.append(Paragraph(eq['description'], body_style))
            elements.append(Spacer(1, 0.1*inch))
    else:
        # Default equations placeholder
        elements.append(Paragraph("• Mathematical formulations are derived from the core principles discussed above.", body_style))
        elements.append(Paragraph("• Refer to academic papers for detailed derivations.", body_style))
    
    # Page break before diagram
    elements.append(PageBreak())
    
    # Architecture Diagram
    elements.append(Paragraph("📊 Architecture Diagram", section_style))
    elements.append(Paragraph("The following diagram illustrates the key components and relationships:", body_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Only show rendered diagram image, not D2 code
    if topic_data.get('d2_code'):
        try:
            diagram_img = fetch_diagram_image(topic_data['d2_code'])
            if diagram_img:
                elements.append(diagram_img)
                elements.append(Spacer(1, 0.2*inch))
            else:
                elements.append(Paragraph("Diagram could not be rendered. Please check the web interface for the interactive diagram.", body_style))
        except Exception as e:
            print(f"Could not fetch diagram: {e}")
            elements.append(Paragraph("Diagram rendering failed. Please check the web interface for the interactive diagram.", body_style))
    
    # Real-World Applications
    if topic_data.get('real_world_applications'):
        elements.append(Paragraph("🌍 Real-World Applications", section_style))
        for app in topic_data['real_world_applications']:
            elements.append(Paragraph(f"• {app}", body_style))
        elements.append(Spacer(1, 0.15*inch))
    
    # Code Example
    if topic_data.get('code_example'):
        elements.append(PageBreak())
        elements.append(Paragraph("💻 Implementation Example", section_style))
        elements.append(Paragraph("The following code demonstrates key concepts:", body_style))
        elements.append(Spacer(1, 0.1*inch))
        code = topic_data['code_example'][:3000]  # Limit length
        elements.append(Paragraph(code.replace('\n', '<br/>'), code_style))
    
    # Sources
    if topic_data.get('sources'):
        elements.append(PageBreak())
        elements.append(Paragraph("🔗 References", section_style))
        for i, src in enumerate(topic_data['sources'][:10], 1):  # Limit to 10 sources
            title = src.get('title', 'Unknown')
            url = src.get('url', '')
            elements.append(Paragraph(f"{i}. {title}", body_style))
            if url:
                elements.append(Paragraph(f"   <i>{url}</i>", ParagraphStyle('Url', parent=body_style, fontSize=8, textColor=colors.blue)))
    
    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Paragraph("Generated by AI Research Explainer Engine | Comprehensive Topic Report", footer_style))
    
    doc.build(elements)
    buffer.seek(0)
    return buffer


def clean_markdown(text):
    """Remove markdown formatting for PDF."""
    if not text:
        return ""
    # Remove code blocks
    text = re.sub(r'```[\w]*\n', '', text)
    text = re.sub(r'```', '', text)
    # Remove inline code markers
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Convert bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    # Convert italic
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
    # Convert bullet points
    text = re.sub(r'^\s*[-*]\s+', '• ', text, flags=re.MULTILINE)
    # Remove math block markers but keep content
    text = re.sub(r'\$\$', '', text)
    text = re.sub(r'\$', '', text)
    return text


def extract_equations(topic_data):
    """Extract or generate equations from topic data."""
    equations = []
    
    # Try to extract from text
    all_text = ""
    for key in ['beginner_explanation', 'core_mechanics', 'advanced_concepts']:
        if topic_data.get(key):
            all_text += " " + topic_data[key]
    
    # Look for math patterns
    math_patterns = [
        (r'\$\$([^$]+)\$\$', 'LaTeX equation'),
        (r'([A-Z][a-z]+\s*=\s*[^\n]+)', 'Formula'),
        (r'(\w+\s*=\s*\w+\s*[\+\-\*/]\s*\w+)', 'Calculation'),
    ]
    
    found_equations = set()
    for pattern, eq_type in math_patterns:
        matches = re.findall(pattern, all_text)
        for match in matches[:3]:  # Limit to 3
            if match not in found_equations:
                found_equations.add(match)
                equations.append({
                    'name': eq_type,
                    'formula': match.strip(),
                    'description': f'Mathematical relationship found in the topic discussion.'
                })
    
    # Add generic topic-specific equations if none found
    if not equations:
        title = topic_data.get('title', 'Topic').lower()
        if 'learning' in title or 'neural' in title or 'ai' in title:
            equations = [
                {'name': 'Loss Function', 'formula': 'L(θ) = Σ(y_pred - y_true)²', 'description': 'Measures prediction error'},
                {'name': 'Gradient Descent', 'formula': 'θ_new = θ_old - α ∇L(θ)', 'description': 'Parameter update rule'},
                {'name': 'Activation', 'formula': 'σ(x) = 1 / (1 + e^(-x))', 'description': 'Sigmoid activation function'}
            ]
        elif 'blockchain' in title or 'crypto' in title:
            equations = [
                {'name': 'Hash Function', 'formula': 'h = H(block_data + nonce)', 'description': 'Proof of work hash'},
                {'name': 'Consensus', 'formula': 'valid if: h < target_difficulty', 'description': 'Block validation condition'}
            ]
        else:
            equations = [
                {'name': 'Core Relationship', 'formula': 'Output = f(Input, Parameters)', 'description': 'Fundamental transformation'},
                {'name': 'Efficiency', 'formula': 'η = (Useful Output / Total Input) × 100%', 'description': 'Performance metric'}
            ]
    
    return equations


def fetch_diagram_image(d2_code):
    """Fetch rendered D2 diagram from Kroki."""
    if not d2_code or not d2_code.strip():
        print("⚠️ No valid D2 code provided for diagram fetching.")
        return None
        
    try:
        print(f"📡 Fetching diagram from Kroki (D2 code length: {len(d2_code)})")
        response = requests.post(
            'https://kroki.io/d2/png',
            data=d2_code.encode('utf-8'),
            headers={'Content-Type': 'text/plain'},
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ Successfully fetched diagram PNG from Kroki.")
            from io import BytesIO
            from reportlab.platypus import Image
            from reportlab.lib.units import inch
            
            img_buffer = BytesIO(response.content)
            img = Image(img_buffer, width=6*inch, height=4*inch, kind='proportional')
            return img
        else:
            print(f"❌ Kroki error (status {response.status_code}): {response.text[:200]}")
            
    except Exception as e:
        import traceback
        print(f"❌ Exception in fetch_diagram_image: {e}")
        traceback.print_exc()
        
    return None
