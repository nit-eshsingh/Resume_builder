from reportlab.lib.pagesizes import C4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import json


class ResumePDF:
    """
    A class to generate a stylized resume in PDF format using ReportLab.
    """

    # RESUME_NAME = "RANJANA KASHYAP"
    # EMAILID = "ranjananithamirpur@gmail.com"
    # PHONE = "+91-9736043013"
    # LINKEDIN = '<a href="https://www.linkedin.com/in/ranjana-kashyap-3bb426130/"><u>linkedin.com/in/ranjanakashyap/</u></a>'
    # ADDRESS = "Gurugram"

    def __init__(self, file_name, py_qt_dict):
        """
        Initializes the ResumePDF class.
        :param file_name: The output PDF file name.
        """
        self.file_name = file_name
        self.pdf = canvas.Canvas(self.file_name, pagesize=C4)
        self.page_width, self.page_height = C4  # page_width 649 page_height 918
        self.left_margin = 30
        self.right_margin = 50
        self.top_margin = 30
        self.bottom_margin = 30
        self.usable_width = self.page_width - self.left_margin - self.right_margin
        self.usable_height = self.page_height - self.top_margin - self.bottom_margin
        self.x_position = self.left_margin
        self.y_position = self.page_height - self.top_margin
        self.RESUME_NAME = py_qt_dict.get("CANDIDATE_NAME")
        self.EMAILID = py_qt_dict.get("EMAIL_ID")
        self.PHONE = py_qt_dict.get("PHONE_NUMBER")
        self.LINKEDIN = f'<a href="{py_qt_dict.get("LINKEDIN")}"><u>{py_qt_dict.get("LINKEDIN").replace("https://www.", "")}</u></a>' if py_qt_dict.get("LINKEDIN") else None
        self.ADDRESS = py_qt_dict.get("ADDRESS")
        self.OBJECTIVE = py_qt_dict.get("OBJECTIVE")
        self.EXPERIENCE = py_qt_dict.get("EXPERIENCE")
        self.EDUCATION = py_qt_dict.get("EDUCATION")
        self.SKILLS = py_qt_dict.get("SKILLS")
        self.HOBIES_AND_INTERESTS = py_qt_dict.get("HOBIES_AND_INTERESTS")
        self.LANGUAGES = py_qt_dict.get("LANGUAGES")
        self.INTERESTS = py_qt_dict.get("INTERESTS")
        self.ACHIEVEMENTS = py_qt_dict.get("ACHIEVEMENTS")
        self.OTHERS = py_qt_dict.get("OTHERS")
        self.CERTIFICATION = py_qt_dict.get("CERTIFICATION")

    def _check_for_new_page_addition(self):
        """
        Checks if a new page is needed and adds one if necessary.
        """
        if self.y_position < self.bottom_margin:
            self.pdf.showPage()
            self.y_position = self.page_height - self.top_margin

    def _draw_line(self):
        """
        Draws a horizontal line on the resume.
        """
        self.pdf.setStrokeColor(colors.rgb2cmyk(0, 0, 9))
        self.pdf.setLineWidth(1)
        self.pdf.line(
            self.left_margin,
            self.y_position,
            self.usable_width + self.right_margin,
            self.y_position,
        )
        print(f"{self.y_position} ,drawed_line")
        self.y_position -= 5

    def _add_title(self, text, objective=None):
        """
        Adds a section title to the resume.
        :param text: The title text.
        """
        self.y_position -= 10
        self.pdf.setFont("Helvetica-Bold", 14)
        self.pdf.setFillColor(colors.rgb2cmyk(0, 0, 9))
        self.pdf.drawString(self.x_position, self.y_position, text)
        print(f"{self.x_position},{self.y_position},add_title {text}")
        self._draw_line()
        self.y_position -= 5

    def _write_text(self, text, bullet_points=False):
        """
        Writes justified text with optional bullet points.
        :param text: The text to write.
        :param bullet_points: Whether to include bullet points.
        """
        style = ParagraphStyle("Bullet", alignment=4)
        paragraph = Paragraph(text, style)
        _, height = paragraph.wrap(self.usable_width, 0)
        if bullet_points:
            self.pdf.drawString(self.x_position + 5, int(self.y_position) - 11, "•")
        paragraph.drawOn(self.pdf, self.x_position + 15, self.y_position - height)
        print(f"before y_position {self.y_position}")
        self.y_position -= height + 5
        print(f"{self.x_position},{self.y_position} ,draw_aligned_text {text}")
        self._check_for_new_page_addition()

    def _write_centered_text(self, text, style_name="Normal"):
        """
        Writes centered text with a given style.
        :param text: The text to write.
        :param style_name: The style name to use.
        """
        styles = getSampleStyleSheet()
        style = styles[style_name]
        style.alignment = 1  # Center aligned
        paragraph = Paragraph(text, style)
        _, height = paragraph.wrap(self.usable_width, self.usable_height)
        paragraph.drawOn(self.pdf, self.x_position, self.y_position)
        print(f"before y_position {self.y_position}")
        self.y_position -= height + 5
        print(
            f"{self.x_position},{self.y_position} ,write_justified_centered_text {text}"
        )

    def _write_right_aligned_text(self, text):
        """
        Writes right-aligned text.
        :param text: The text to write.
        """
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.alignment = 2  # Right aligned
        paragraph = Paragraph(text, style)
        _, height = paragraph.wrap(self.usable_width, 0)
        paragraph.drawOn(self.pdf, self.x_position, self.y_position)
        print(f"before y_position {self.y_position}")
        print(
            f"{self.x_position},{self.y_position} ,self._write_right_aligned_text {text}"
        )

    # Function to add regular text
    def draw_text(self, text, indent=0, bold=False):
        if bold:
            self.pdf.setFont("Helvetica-Bold", 12)
        else:
            self.pdf.setFont("Helvetica", 11)
        for line in text.split("\n"):
            self.pdf.drawString(30 + indent, self.y_position, line)
            self.y_position = self.y_position - 8
            print(f"{self.x_position},{self.y_position} ,draw_text {text}")
        return self.y_position

    def generate_pdf(self):
        """
        Generates the resume PDF with all sections.
        """
        self._write_centered_text(
            f"<u><b>{self.RESUME_NAME}</b></u>",
        )
        personal_detail = (
            f"<b><u>{self.EMAILID}</u> | {self.PHONE} | <u>{self.LINKEDIN}</u></b>"
        )

        self._write_centered_text(personal_detail)
        self.y_position = self.y_position - 12
        self.pdf.setFont("Helvetica", 12)
        self.pdf.setFillColor(colors.black)

        # Objectives Section
        self._add_title("Objective:", True)
        # objective_details = "To foster a safe and healthy work environment by implementing effective HSE policies and practices, while driving sustainability initiatives that reduce environmental impact, optimize resource utilization, and ensure compliance with organizational and regulatory standards for long-term sustainable development."
        # hobbies_item = "Singing, Listening to music, Travelling, Photography[Capturing Moments], Cooking/Baking."
        self._write_text(f"{self.OBJECTIVE}")

        self.y_position = self.y_position - 45

        # Professional Experience
        self._add_title("Professional Experience:", self.y_position)
        print(self.y_position, "Experience")
        # bold_characters = {"ETL": "<b>ETL</b>", "Kafka": "<b>Kafka</b>"}

        experiences = self.EXPERIENCE
        for exp in experiences:
            self.y_position = self.y_position - 8
            print(self.y_position, "experiences in loop")
            # self._write_right_aligned_text()
            self._write_right_aligned_text(f"<b>{exp['DURATION']}</b>")
            self.draw_text(
                f"{exp['ROLE']} | {exp['COMPANY']}", self.y_position, bold=True
            )
            for detail in exp["DETAILS"]:
                # print(self.y_position, "loop")
                self._write_text(f"{detail}", True)
                # print(self.y_position, "return loop")
            self.y_position = self.y_position - 10


        self._add_title("Education:", self.y_position)
        education_detail = self.EDUCATION
        # education_detail = [
        #     {
        #         "college": "<b>Regional Labour Institute, Faridabad</b>",
        #         "course": "<i>PG Diploma in Industrial Safety </i>",
        #         "duration": "<b>Jun 2021 - Jun 2022</b>",
        #         "grades": "<i>Percentage : 79.2%, Silver Medalist</i>",
        #         "location": "<i>Haryana, India</i>",
        #     },
        #     {
        #         "college": "<b>National Institute of Technology, Hamirpur (NITH)</b>",
        #         "course": "<i>Bachelor of Technology in Chemical Engineering</i>",
        #         "duration": "<b>Aug 2014 - May 2018</b>",
        #         "grades": "<i>Percentage : 87.8%</i>",
        #         "location": "<i>H.P., India</i>",
        #     },
        # ]

        for detail_item in education_detail:
            self._write_text(f"{detail_item['INSTITUTE']}", True)
            self._write_right_aligned_text(
                f"{detail_item['DURATION']}",
            )
            self._write_text(f"{detail_item['DEGREE']}")
            self._write_right_aligned_text(
                f"{detail_item['LOCATION']}",
            )
            self._write_text(f"{detail_item['GRADES']}")

        self.y_position = self.y_position - 10

        # Publications
        self._add_title("Expertise and Certification:")
        # hyperlink = '<a href="https://www.sciencedirect.com/science/article/abs/pii/S1434841118301791"><u>Energy detection based spectrum sensing for gamma shadowed α–η–μ and α–κ–μ fading channels.</u></a>'
        # hyperlink = '<a href="https://www.sciencedirect.com/science/article/abs/pii/S1434841118301791"><b>Co-Author:</b> Energy detection based spectrum sensing for gamma shadowed α–η–μ and α–κ–μ fading channels</a>'
        Certification = [
            "Working at Heights Training from Global Wind Organisation",
            "First Aid, CPR and Medical Emergency Preparedness from St John Ambulance",
            "Certified Process Safety Management (PSM) professional from M/S Chola MS",
            "Certified Internal Energy Auditor for ISO 50001:2018 –Energy Management System",
            "ISO 9001:2015 - Quality Management System",
            "ISO 14001:2015 - Environment Management System",
            "ISO 45001:2018 - Occupational Health & Safety Management system",
            "ISO 31000:2018 - Risk Management System Trained internally from Uflex Limited",
            "Six Sigma Green Belt Trained internally from Uflex Limited.",
            # "Certified in Advanced Training Skills."
        ]
        for detail_item in Certification:
            self._write_text(f"{detail_item}", True)

        self.y_position = self.y_position - 10

        # Languages
        self._add_title("Languages:", self.y_position)
        # draw_text("Hindi (Native)\nEnglish (Fluent)", self.y_position)
        Languages_details = self.LANGUAGES
        # Languages_details = ["Hindi (Native)", "English (Fluent)"]
        # _write_text(pdf, f"{Languages_details}", x_position, self.y_position, usable_width)
        for detail_item in Languages_details:
            self._write_text(f"{detail_item.get('LANGUAGE')} ({detail_item.get('PROFICIENCY')})", True)

        self.y_position = self.y_position - 10

        # Hobbies & Interests
        self._add_title("Hobbies & Interests:", self.y_position)
        hobbies_item = ",".join(self.HOBIES_AND_INTERESTS)
        # hobbies_item = "Singing, Listening to music, Travelling, Photography[Capturing Moments], Cooking/Baking."
        self._write_text(f"{hobbies_item}", True)

        # Save the PDF
        self.pdf.save()


if __name__ == "__main__":
    file_name = "Candidate_Resume.pdf"
    py_qt_dict = json.load(open("resume_input.json"))

    resume = ResumePDF(file_name, py_qt_dict)
    resume.generate_pdf()

    print("PY_qt:", py_qt_dict)
