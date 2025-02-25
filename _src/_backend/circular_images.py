from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import C4

# Create a PDF canvas
pdf_file = "output.pdf"
c = canvas.Canvas(pdf_file, pagesize=C4)
page_width, page_height = C4
print(page_width, page_height)

# Define the circular image file path
image_path = "circular_ranjana_image.png"  # Ensure this is a circular PNG with transparency

# Position and size of the circular image
x_position = 520  # X coordinate
y_position = 810  # Y coordinate
image_width = 100  # Desired width
image_height = 100  # Desired height

# Draw the circular PNG image at the specified position
c.drawImage(image_path, x_position, y_position, width=image_width, height=image_height, mask='auto')

# Save the PDF
c.save()

print(f"PDF with circular image created: {pdf_file}")
