# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit
# from fpdf import FPDF
#
#
# class PDFGeneratorApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("PDF Generator")
#         self.setGeometry(100, 100, 400, 300)
#
#         # Layout
#         layout = QVBoxLayout()
#
#         # Input field
#         self.label = QLabel("Enter text to generate PDF:")
#         layout.addWidget(self.label)
#
#         self.text_input = QTextEdit(self)
#         layout.addWidget(self.text_input)
#
#         # Submit button
#         self.submit_button = QPushButton("Submit", self)
#         self.submit_button.clicked.connect(self.generate_pdf)
#         layout.addWidget(self.submit_button)
#
#         # Set layout
#         self.setLayout(layout)
#
#     def generate_pdf(self):
#         text = self.text_input.toPlainText()
#
#         if not text.strip():
#             QMessageBox.warning(self, "Input Error", "Please enter some text!")
#             return
#
#         # Generate PDF
#         try:
#             pdf = FPDF()
#             pdf.add_page()
#             pdf.set_font("Arial", size=12)
#             pdf.multi_cell(0, 10, text)
#             pdf.output("generated_document.pdf")
#             QMessageBox.information(self, "Success", "PDF generated successfully as 'generated_document.pdf'.")
#         except Exception as e:
#             QMessageBox.critical(self, "Error", f"Failed to generate PDF: {str(e)}")
#
#
# # Main application
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PDFGeneratorApp()
#     window.show()
#     sys.exit(app.exec())
#
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PyQt6.uic import loadUi
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
#
#
# class ResumeGeneratorApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # Load the UI file
#         loadUi("resume_generator.ui", self)
#
#         # Connect the button
#         self.submit_button.clicked.connect(self.generate_resume)
#
#     def generate_resume(self):
#         # Get user input
#         name = self.input_name.text()
#         email = self.input_email.text()
#         phone = self.input_phone.text()
#         summary = self.input_summary.toPlainText()
#         education = self.input_education.toPlainText()
#         experience = self.input_experience.toPlainText()
#         skills = self.input_skills.toPlainText()
#
#         if not name or not email or not phone:
#             QMessageBox.warning(self, "Input Error", "Name, Email, and Phone are required fields!")
#             return
#
#         # Generate the PDF
#         try:
#             filename = "resume.pdf"
#             pdf = canvas.Canvas(filename, pagesize=letter)
#             width, height = letter
#
#             # Title
#             pdf.setFont("Helvetica-Bold", 16)
#             pdf.drawCentredString(width / 2.0, height - 50, "Resume")
#
#             pdf.setFont("Helvetica", 12)
#             y_position = height - 100
#
#             # Personal Information
#             pdf.setFont("Helvetica-Bold", 14)
#             pdf.drawString(50, y_position, "Personal Information")
#             y_position -= 20
#             pdf.setFont("Helvetica", 12)
#             pdf.drawString(50, y_position, f"Name: {name}")
#             y_position -= 15
#             pdf.drawString(50, y_position, f"Email: {email}")
#             y_position -= 15
#             pdf.drawString(50, y_position, f"Phone: {phone}")
#             y_position -= 30
#
#             # Professional Summary
#             pdf.setFont("Helvetica-Bold", 14)
#             pdf.drawString(50, y_position, "Professional Summary")
#             y_position -= 20
#             pdf.setFont("Helvetica", 12)
#             for line in summary.split("\n"):
#                 pdf.drawString(50, y_position, line)
#                 y_position -= 15
#             y_position -= 15
#
#             # Education
#             pdf.setFont("Helvetica-Bold", 14)
#             pdf.drawString(50, y_position, "Education")
#             y_position -= 20
#             pdf.setFont("Helvetica", 12)
#             for line in education.split("\n"):
#                 pdf.drawString(50, y_position, line)
#                 y_position -= 15
#             y_position -= 15
#
#             # Work Experience
#             pdf.setFont("Helvetica-Bold", 14)
#             pdf.drawString(50, y_position, "Work Experience")
#             y_position -= 20
#             pdf.setFont("Helvetica", 12)
#             for line in experience.split("\n"):
#                 pdf.drawString(50, y_position, line)
#                 y_position -= 15
#             y_position -= 15
#
#             # Skills
#             pdf.setFont("Helvetica-Bold", 14)
#             pdf.drawString(50, y_position, "Skills")
#             y_position -= 20
#             pdf.setFont("Helvetica", 12)
#             for line in skills.split("\n"):
#                 pdf.drawString(50, y_position, line)
#                 y_position -= 15
#             y_position -= 15
#
#             # Save PDF
#             pdf.save()
#             QMessageBox.information(self, "Success", f"Resume generated successfully as '{filename}'.")
#         except Exception as e:
#             QMessageBox.critical(self, "Error", f"Failed to generate resume: {str(e)}")
#
#
# # Main application
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ResumeGeneratorApp()
#     window.show()
#     sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QSplitter,
    QTextBrowser,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class ResumeGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resume Generator")
        self.setGeometry(100, 100, 800, 600)

        # Main Layout
        splitter = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(splitter)

        # Left side: Input fields
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout(self.left_widget)

        self.add_input_field("Full Name", "input_name")
        self.add_input_field("Email", "input_email")
        self.add_input_field("Phone", "input_phone")
        self.add_text_area("Professional Summary", "input_summary")
        self.add_text_area("Education", "input_education")
        self.add_text_area("Work Experience", "input_experience")
        self.add_text_area("Skills", "input_skills")

        self.generate_button = QPushButton("Generate PDF")
        self.generate_button.clicked.connect(self.generate_pdf)
        self.left_layout.addWidget(self.generate_button)

        splitter.addWidget(self.left_widget)

        # Right side: Resume preview
        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout(self.right_widget)

        self.preview_label = QLabel("Resume Preview")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_layout.addWidget(self.preview_label)

        self.preview_browser = QTextBrowser()
        self.right_layout.addWidget(self.preview_browser)

        splitter.addWidget(self.right_widget)

        # Live updates
        self.inputs = {}
        for widget_name in [
            "input_name",
            "input_email",
            "input_phone",
            "input_summary",
            "input_education",
            "input_experience",
            "input_skills",
        ]:
            widget = getattr(self, widget_name)
            widget.textChanged.connect(self.update_preview)

    def add_input_field(self, label_text, attr_name):
        label = QLabel(label_text)
        line_edit = QLineEdit()
        self.left_layout.addWidget(label)
        self.left_layout.addWidget(line_edit)
        setattr(self, attr_name, line_edit)

    def add_text_area(self, label_text, attr_name):
        label = QLabel(label_text)
        text_edit = QTextEdit()
        self.left_layout.addWidget(label)
        self.left_layout.addWidget(text_edit)
        setattr(self, attr_name, text_edit)

    def update_preview(self):
        # Collect input data
        name = self.input_name.text()
        email = self.input_email.text()
        phone = self.input_phone.text()
        summary = self.input_summary.toPlainText()
        education = self.input_education.toPlainText()
        experience = self.input_experience.toPlainText()
        skills = self.input_skills.toPlainText()

        # Create a preview text
        new_line = "\n"
        preview_text = (
            f"<b>Full Name:</b> {name}<br>"
            f"<b>Email:</b> {email}<br>"
            f"<b>Phone:</b> {phone}<br><br>"
            f"<b>Professional Summary:</b><br>{summary.replace(new_line, '<br>')}<br><br>"
            f"<b>Education:</b><br>{education.replace(new_line, '<br>')}<br><br>"
            f"<b>Work Experience:</b><br>{experience.replace(new_line, '<br>')}<br><br>"
            f"<b>Skills:</b><br>{skills.replace(new_line, '<br>')}"
        )
        self.preview_browser.setHtml(preview_text)

    def generate_pdf(self):
        # Get user input
        name = self.input_name.text()
        email = self.input_email.text()
        phone = self.input_phone.text()
        summary = self.input_summary.toPlainText()
        education = self.input_education.toPlainText()
        experience = self.input_experience.toPlainText()
        skills = self.input_skills.toPlainText()

        if not name or not email or not phone:
            QMessageBox.warning(self, "Input Error", "Name, Email, and Phone are required fields!")
            return

        # Generate the PDF
        try:
            filename = "resume.pdf"
            pdf = canvas.Canvas(filename, pagesize=letter)
            width, height = letter

            # Title
            pdf.setFont("Helvetica-Bold", 16)
            pdf.drawCentredString(width / 2.0, height - 50, "Resume")
            pdf.setFont("Helvetica", 12)
            y_position = height - 100

            # Personal Information
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y_position, "Personal Information")
            y_position -= 20
            pdf.setFont("Helvetica", 12)
            pdf.drawString(50, y_position, f"Name: {name}")
            y_position -= 15
            pdf.drawString(50, y_position, f"Email: {email}")
            y_position -= 15
            pdf.drawString(50, y_position, f"Phone: {phone}")
            y_position -= 30

            # Professional Summary
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y_position, "Professional Summary")
            y_position -= 20
            pdf.setFont("Helvetica", 12)
            for line in summary.split("\n"):
                pdf.drawString(50, y_position, line)
                y_position -= 15
            y_position -= 15

            # Education
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y_position, "Education")
            y_position -= 20
            pdf.setFont("Helvetica", 12)
            for line in education.split("\n"):
                pdf.drawString(50, y_position, line)
                y_position -= 15
            y_position -= 15

            # Work Experience
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y_position, "Work Experience")
            y_position -= 20
            pdf.setFont("Helvetica", 12)
            for line in experience.split("\n"):
                pdf.drawString(50, y_position, line)
                y_position -= 15
            y_position -= 15

            # Skills
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y_position, "Skills")
            y_position -= 20
            pdf.setFont("Helvetica", 12)
            for line in skills.split("\n"):
                pdf.drawString(50, y_position, line)
                y_position -= 15
            y_position -= 15

            # Save PDF
            pdf.save()
            QMessageBox.information(self, "Success", f"Resume generated successfully as '{filename}'.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate resume: {str(e)}")


# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResumeGeneratorApp()
    window.show()
    sys.exit(app.exec())

