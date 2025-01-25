from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, ListFlowable, ListItem

# Create a PDF document
pdf_filename = "bullet_paragraph.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Get default styles and customize one for bullets
styles = getSampleStyleSheet()
bullet_style = ParagraphStyle(
    'BulletStyle',
    parent=styles['Normal'],
    bulletIndent=10,  # Indentation for bullets
    bulletFontSize=12,
    bulletFontName='Helvetica-Bold',
    spaceAfter=10
)

# Define the bullet points content
bullet_points = [
    Paragraph("First bullet point text goes here.", bullet_style),
    Paragraph("Second bullet point with more details.", bullet_style),
    Paragraph("Third bullet point, explaining further.", bullet_style),
]

# Using ListFlowable to manage bullet formatting
bullet_list = ListFlowable(
    [ListItem(item, bulletText='•') for item in bullet_points],
    bulletType='bullet'
)

# Build the PDF with the bullet list
doc.build([bullet_list])

print(f"PDF '{pdf_filename}' created successfully.")
