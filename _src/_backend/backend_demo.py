import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QScrollArea,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import Qt
from reportlab.lib.pagesizes import C4
from reportlab.pdfgen import canvas


class ResumeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../_frontend/resume_generator.ui", self)

        # Create a scroll area for the preview
        self.scroll_area = QScrollArea()
        self.preview_container = QWidget()
        self.preview_layout = QVBoxLayout(self.preview_container)

        self.preview_browser = QTextBrowser()
        self.preview_layout.addWidget(self.preview_browser)

        self.scroll_area.setWidget(self.preview_container)
        self.scroll_area.setWidgetResizable(True)
        self.previewLayout.addWidget(self.scroll_area)

        # Connect input fields to update the preview
        self.inputName.textChanged.connect(self.update_preview)
        self.inputLocation.textChanged.connect(self.update_preview)
        self.inputPhone.textChanged.connect(self.update_preview)

        self.inputLinkedin.textChanged.connect(self.update_preview)
        self.inputEmail.textChanged.connect(self.update_preview)
        self.inputHobies.textChanged.connect(self.update_preview)
        self.inputGithub.textChanged.connect(self.update_preview)
        self.inputSummary.textChanged.connect(self.update_preview)

        # self.inputEducation.textChanged.connect(self.update_preview)
        # self.inputExperience.textChanged.connect(self.update_preview)
        # self.inputSkfggills.textChanged.connect(self.update_preview)

        # Connect the generate button
        self.generateButton.clicked.connect(self.generate_pdf)

    def update_preview(self):
        # Get input data  26000 16000
        name = self.inputName.text()
        location = self.inputLocation.text()
        phone = self.inputPhone.text()
        linkedin = self.inputLinkedin.text()
        email = self.inputEmail.text()
        hobies = self.inputHobies.text()
        github = self.inputGithub.text()
        summary = self.inputSummary.toPlainText()
        # education = self.inputEducation.toPlainText()
        # experience = self.inputExperience.toPlainText()
        # skills = self.inputSkills.toPlainText()

        # Create a preview
        # Create a preview text
        new_line = "\n"
        preview_text = (
            f"<b>Full Name:</b> {name}<br>"
            f"<b>Location:</b> {location}<br>"
            f"<b>Phone:</b> {phone}<br>"
            f"<b>Linkedin:</b> {linkedin}<br>"
            f"<b>Email:</b> {email}<br>"
            f"<b>Phone:</b> {hobies}<br>"
            f"<b>Github:</b> {github}<br>"
            f"<b>Professional Summary:</b><br>{summary.replace(new_line, '<br>')}<br><br>"
            # f"<b>Education:</b><br>{education.replace(new_line, '<br>')}<br><br>"
            # f"<b>Work Experience:</b><br>{experience.replace(new_line, '<br>')}<br><br>"
            # f"<b>Skills:</b><br>{skills.replace(new_line, '<br>')}"
        )
        self.preview_browser.setHtml(preview_text)

    def generate_pdf(self):
        # Get user input
        name = self.inputName.text()
        location = self.inputLocation.text()
        phone = self.inputPhone.text()
        linkedin = self.inputLinkedin.text()
        email = self.inputEmail.text()
        hobies = self.inputHobies.text()
        github = self.inputGithub.text()
        summary = self.inputSummary.toPlainText()
        # education = self.inputEducation.toPlainText()
        # experience = self.inputExperience.toPlainText()
        # skills = self.inputSkills.toPlainText()

        if not name or not email or not phone:
            QMessageBox.warning(self, "Input Error", "Name, Email, and Phone are required fields!")
            return

        # Generate the PDF
        try:
            filename = "../resume.pdf"
            pdf = canvas.Canvas(filename, pagesize=C4)
            width, height = C4

            # Title
            pdf.setFont("Helvetica-Bold", 16)
            pdf.drawCentredString(width / 2.0, height - 50, "Resume")
            pdf.setFont("Helvetica", 12)
            y_position = height - 100

            # Helper function to handle page breaks
            def draw_text_block(pdf, text, x, y, line_height=15):
                nonlocal y_position
                for line in text.split("\n"):
                    if y_position < 50:  # If space is not enough for a line, create a new page
                        pdf.showPage()
                        pdf.setFont("Helvetica", 12)
                        y_position = height - 50
                    pdf.drawString(x, y_position, line)
                    y_position -= line_height

            # Personal Information
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y_position, "Personal Information")
            y_position -= 20
            pdf.setFont("Helvetica", 12)
            draw_text_block(pdf, f"Name: {name}\nEmail: {email}\nPhone: {phone}", 50, y_position)

            # Professional Summary
            pdf.setFont("Helvetica-Bold", 14)
            draw_text_block(pdf, "Professional Summary", 50, y_position)
            y_position -= 20
            pdf.setFont("Helvetica", 12)
            draw_text_block(pdf, summary, 50, y_position)

            # Education
            # pdf.setFont("Helvetica-Bold", 14)
            # draw_text_block(pdf, "Education", 50, y_position)
            # y_position -= 20
            # pdf.setFont("Helvetica", 12)
            # draw_text_block(pdf, education, 50, y_position)
            #
            # # Work Experience
            # pdf.setFont("Helvetica-Bold", 14)
            # draw_text_block(pdf, "Work Experience", 50, y_position)
            # y_position -= 20
            # pdf.setFont("Helvetica", 12)
            # draw_text_block(pdf, experience, 50, y_position)
            #
            # # Skills
            # pdf.setFont("Helvetica-Bold", 14)
            # draw_text_block(pdf, "Skills", 50, y_position)
            # y_position -= 20
            # pdf.setFont("Helvetica", 12)
            # draw_text_block(pdf, skills, 50, y_position)

            # Save PDF
            pdf.save()
            QMessageBox.information(self, "Success", f"Resume generated successfully as '{filename}'.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate resume: {str(e)}")


# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResumeGenerator()
    window.show()
    sys.exit(app.exec())
