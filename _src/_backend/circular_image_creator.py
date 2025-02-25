from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image


# Function to create a circular mask for an image
def create_circular_mask(image_path):
    img = Image.open(image_path).convert("RGBA")
    size = min(img.size)
    mask = Image.new("L", img.size, 0)
    draw = Image.new("L", img.size, 255)

    # Create circular mask
    from PIL import ImageDraw
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    img.putalpha(mask)

    circular_img_path = "circular_ranjana_image.png"
    img.save(circular_img_path)
    return circular_img_path


# Create the PDF
c = canvas.Canvas("output_ranjana.pdf", pagesize=letter)
image_path = "ranjana_pic.jpg"

# Create a circular version of the image
circular_image = create_circular_mask(image_path)

# Add the circular image to the PDF
c.drawImage(circular_image, 200, 500, width=100, height=100)

c.save()
print("PDF with circular image created successfully.")
