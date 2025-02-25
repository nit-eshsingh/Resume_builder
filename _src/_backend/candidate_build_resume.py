from reportlab.lib.pagesizes import C4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

class ResumePDF:
    """
    A class to generate a stylized resume in PDF format using ReportLab.
    """
    RESUME_NAME = "RANJANA KASHYAP"
    EMAILID = "ranjananithamirpur@gmail.com"
    PHONE = "+91-9736043013"
    LINKEDIN = '<a href="https://www.linkedin.com/in/ranjana-kashyap-3bb426130/"><u>linkedin.com/in/ranjanakashyap/</u></a>'
    ADDRESS = "Gurugram"

    def __init__(self, file_name):
        """
        Initializes the ResumePDF class.
        :param file_name: The output PDF file name.
        """
        self.file_name = file_name
        self.pdf = canvas.Canvas(self.file_name, pagesize=C4)
        self.page_width, self.page_height = C4
        self.left_margin = 30
        self.right_margin = 50
        self.top_margin = 30
        self.bottom_margin = 30
        self.usable_width = self.page_width - self.left_margin - self.right_margin
        self.usable_height = self.page_height - self.top_margin - self.bottom_margin
        self.x_position = self.left_margin
        self.y_position = self.page_height - self.top_margin

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
        self.pdf.setStrokeColor(colors.rgb2cmyk(0,0,9))
        self.pdf.setLineWidth(1)
        self.pdf.line(self.left_margin, self.y_position, self.usable_width + self.right_margin, self.y_position)
        print(f"{self.y_position} ,drawed_line")
        self.y_position -= 5

    def _add_title(self, text, objective=None):
        """
        Adds a section title to the resume.
        :param text: The title text.
        """
        self.y_position -= 10
        self.pdf.setFont("Helvetica-Bold", 14)
        self.pdf.setFillColor(colors.rgb2cmyk(0,0,9))
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
        style = ParagraphStyle('Bullet', alignment=4)
        paragraph = Paragraph(text, style)
        _, height = paragraph.wrap(self.usable_width, 0)
        if bullet_points:
            self.pdf.drawString(self.x_position + 5, self.y_position - 11, "•")
        paragraph.drawOn(self.pdf, self.x_position + 15, self.y_position - height)
        print(f"before y_position {self.y_position}")
        self.y_position -= height + 5
        print(f"{self.x_position},{self.y_position} ,draw_aligned_text {text}")

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
        print(f"{self.x_position},{self.y_position} ,write_justified_centered_text {text}")

    def _write_right_aligned_text(self, text):
        """
        Writes right-aligned text.
        :param text: The text to write.
        """
        styles = getSampleStyleSheet()
        style = styles['Normal']
        style.alignment = 2  # Right aligned
        paragraph = Paragraph(text, style)
        _, height = paragraph.wrap(self.usable_width, 0)
        paragraph.drawOn(self.pdf, self.x_position, self.y_position)
        print(f"before y_position {self.y_position}")
        print(f"{self.x_position},{self.y_position} ,write_justified_right_text {text}")

    def generate_pdf(self):
        """
        Generates the resume PDF with all sections.
        """
        # self._write_centered_text(f"<u><b>{self.RESUME_NAME}</b></u>", "Heading1")
        # personal_details = f"<b><u>{self.EMAILID}</u> | {self.PHONE} | <u>{self.LINKEDIN}</u></b>"
        # self._write_centered_text(personal_details, "Normal")
        # self._add_title("Objective:")
        # self._write_text("To foster a safe and healthy work environment...")
        # self._add_title("Education:")
        # self._write_text("<b>National Institute of Technology, Hamirpur</b> | B.Tech in Chemical Engineering | 87.8%", True)
        # self._write_text("<b>Regional Labour Institute, Faridabad</b> | PG Diploma in Industrial Safety | 79.2%, Silver Medalist", True)
        # self._add_title("Languages:")
        # self._write_text("Hindi (Native), English (Fluent)", True)
        # self._add_title("Hobbies & Interests:")
        # self._write_text("Singing, Listening to music, Travelling, Photography, Cooking/Baking.", True)
        # self.pdf.save()
        # print(f"PDF file '{self.file_name}' created successfully!")
        y_position = self._write_centered_text(f"<u><b>{self.RESUME_NAME}</b></u>", x_position, y_position,
                                                   usable_width, styling="Heading1")
        personal_detail = f"<b><u>{EMAILID}</u> | {PHONE} | <u>{LINKEDIN}</u></b>"

        write_justified_centered_text(pdf, personal_detail, x_position, y_position, usable_width, styling="Normal")
        y_position = y_position - 12
        # pdf.drawCentredString(
        #     page_width/2,
        #     y_position,
        #     f"{RESUME_NAME}",
        #     mode=0)

        # y_position = draw_text(
        #     f"{ADDRESS}  |  {PHONE}  |  {EMAILID}  |  {LINKEDIN}",
        #     y_position - 20, indent=10
        # )
        # personal_detail = f"<b>{ADDRESS} | {PHONE} | <u>{EMAILID}</u> | <u>{LINKEDIN}</u></b>"
        # y_position = write_justified_text(pdf, f"{personal_detail}", x_position, y_position, usable_width)
        # # print(y_position, "return loop")
        # y_position = y_position - 14
        # y_position = draw_line(y_position - 10)
        pdf.setFont("Helvetica", 12)
        pdf.setFillColor(colors.black)
        # y_position = draw_text(
        #     "A self-directed and motivated engineer experienced working effectively in dynamic environments. \n"
        #     "Fluent in Python programming language and DevOps tools like Jenkins and AWS.",
        #     y_position
        # )

        # Contact Information
        # y_position = add_title("Contact Information:", y_position)

        # y_position = y_position - 10

        # Objectives Section
        y_position = add_title("Objective:", y_position, True)
        objective_details = "To foster a safe and healthy work environment by implementing effective HSE policies and practices, while driving sustainability initiatives that reduce environmental impact, optimize resource utilization, and ensure compliance with organizational and regulatory standards for long-term sustainable development."
        # hobbies_item = "Singing, Listening to music, Travelling, Photography[Capturing Moments], Cooking/Baking."
        write_justified_text(pdf, f"{objective_details}", x_position, y_position, usable_width)

        y_position = y_position - 45

        # Professional Experience
        y_position = add_title("Professional Experience:", y_position)
        print(y_position, "Experience")
        bold_characters = {"ETL": "<b>ETL</b>", "Kafka": "<b>Kafka</b>"}
        experiences = [
            {
                "role": "Deputy Manager (ESG) - EHS and Sustainability",
                "company": "BluPine Energy Pvt. Ltd.",
                "duration": "April 2024 - Present",
                "details": [
                    f"Analyze site safety statistics data for Operational and under construction(Solar and Wind) project sites, prepare monthly SteerCo presentations, and highlight gaps.",
                    f"Coordinate IMS system implementation across the portfolio.",
                    "Responsible for implementation of ISO 14001 and 45001 across portfolio.",
                    "Conduct ESIA and ESDD studies for new projects along with vendors.",
                    "Ensure compliance with the Environmental and Social Management System (ESMS) and IFC standards",
                    f"Drive safety culture improvement initiatives, including standardized training modules, induction videos, reward & recognition programs, and standardized safety signage.",
                    f"Co-ordinating for carry out third-party safety audits for Operations and Maintenance at project sites as per the specified frequency and ensure timely closure of observations.",
                    "Worked on budget planning for financial year to ensure the smooth achievement of organizational goals and targets, optimizing resources and aligning financial strategies with business objectives.",
                    "Coordinating with site HSE personnel from the head office to address and resolve issues."
                ]
            },
            {
                "role": "Section Head - WCM",
                "company": "Grasim Industries Limited [ Birla Cellulosic ]",
                "duration": "June 2022 - Dec 2023",
                "details": [
                    # f"Analyzing Site's safety statistics data of O&M and project site and preparing monthly SteerCo presentation, highlighting the gaps to the management.",
                    # f"Responsible for conducting third party safety audit of O&M and project site as per the defined frequency and get the observations closed.",
                    # f"Coordinator for implementing IMS system across portfolio.",
                    # f"Conducting ESIA and ESDD along with vendor and closing the observation.",
                    # f"Driving various initiatives at site to improve safety culture such as Standardized training module, Induction video, Reward & recognition and standardized safety signages etc.",
                    "Led the implementation of ISO9001, 14001, and 45001 standards, ensuring compliance and successful audits at the site.",
                    "Developed and maintained documentation for Process Safety Management (PSM) and Sustainability (Higgs Index), demonstrating a strong commitment to safety and environmental responsibility.",
                    "Defined, planned, and executed organizational goals and objectives, aligning them withoverall company strategy.",
                    "Actively tracked and communicated the status of key initiatives, providing regular updates to stakeholders and ensuring transparency and accountability.",
                    "Successfully managed multiple projects, consistently meeting delivery targets and providing status updates on performance against plan.",
                    "Utilized Minitab tool for Regression & Correlation, Design of Experiment, FMEA, and other statistical analysis, effectively analyzing data and identifying trends and insights.",
                    "Demonstrated excellent analytical skills and problem-solving abilities, utilizing root cause analysis to identify and implement effective solutions.",
                    "Measured and reported on key performance indicators (leading and lagging) at the site level, developing and implementing corrective action plans to address areas of concern.",
                    "Identified key issues, gathered and analyzed data, and synthesized findings to support hypotheses and develop actionable recommendations."
                ]
            },
            {
                "role": "Process Control Engineer",
                "company": "Johnson Matthey India Private Limited",
                "duration": "September 2021 - June 2022",
                "details": [
                    f"Ensuring effective production planning for optimum productivity.",
                    # f"Documentation and responsible for closure of EHS and QMS observations with in time.",
                    # f"Ensuring effective production planning for optimum productivity.",
                    f"Downtime analysis and action plan generation.",
                    # f"Planning and execution of validation of new product and implementation in mass production.",
                    # f"Carry out and support CI project implementation works by providing technical setup.",
                    # f"Accountability and controlling of consumables.",
                    f"Responsible for developing LEAN culture compliance with health and safety regulations.",
                    f"Documentation of IATF, ISO14001 and OHSAS 18001 audits.",
                    # f"Responsible for monitoring and controlling Production KPI’s (Plan Execution, Line attainment, Process Downtime, Schedule Downtime, CT, Rejection etc.)",
                ]
            },
            {
                "role": "Officer",
                "company": "UFLEX Limited (Chemical Business)",
                "duration": "June 2018 - August 2021",
                "details": [
                    f"Implemented and documented Quality Management System (ISO 9001:2015), Environment Management System (ISO 14001:2015), Occupational Health and Safety Management System (ISO 45001:2018), and Risk Management System (ISO 31000:2018) at UFLEX Limited (Chemical Business).",
                    f"Ensured compliance with legal requirements related to waste generation, pressure testing of vessels, effluent generation.",
                    f"Led improvement projects within time-bound targets, focusing on efficiency improvements, process excellence initiatives, cost savings, safety, environment, and productivity management.",
                    f"Conducted risk assessments, job safety analyses (JSA), and hazard and operability studies (HAZOP) for various processes.",
                    # f"Coordinated with maintenance, environmental health and safety (EHS), excellence, and production teams to ensure smooth project implementation.",
                    f"Conducted process audits and reviews to ensure strict adherence to defined guidelines and systems.",
                    f"Utilized process mapping techniques such as input/output diagrams, value stream mapping (VSM), root cause analysis (RCA), Six Sigma, Lean Six Sigma, World Class Manufacturing (WCM), Total Productive Maintenance (TPM), Total Quality Management (TQM), Overall Equipment Effectiveness (OEE), and planning and implementing countermeasures to monitor results.",

                ]
            },
        ]

        for exp in experiences:
            y_position = y_position - 8
            print(y_position, "experiences in loop")
            # write_justified_right_text()
            write_justified_right_text(pdf, f"<b>{exp['duration']}</b>", x_position, y_position, usable_width + 10)
            y_position = draw_text(f"{exp['role']} | {exp['company']}", y_position, bold=True)
            for detail in exp['details']:
                # print(y_position, "loop")
                y_position = write_justified_text(pdf, f"{detail}", x_position, y_position, usable_width, True)
                # print(y_position, "return loop")
            y_position = y_position - 10

        # y_position = _check_for_new_page_addition(y_position)
        # y_position = _check_for_new_page_addition(y_position)

        # Skills
        # y_position = add_title("Skills:", y_position)
        # # y_position = draw_text(
        # #     "Python: PySpark, PyQt5, Web Scraping, pandas, numpy, psycopg2\n"
        # #     "DevOps: AWS, Jenkins, Groovy, Batch Script, FOSS ID\n"
        # #     "Design Patterns: UML Diagrams, DB Schemas, Sequence Diagram, ETL\n"
        # #     "Others: MongoDB, GraphQL, Kafka, Artifactory Servers, SonarQube, Power Automate",
        # #     y_position
        # # )
        # skill_detail = ["<b>Python:</b>PySpark, fastapi, PyQt5, Web Scraping, pandas, numpy, psycopg2.\n",
        #                 "<b>DevOps :</b> AWS, Jenkins, Groovy, Batch Script, FOSS ID.\n",
        #                 "<b>Design Patterns :</b> UML Diagrams, DB Schemas, Sequence Diagram, ETL.\n",
        #                 "<b>Others :</b> MongoDB, PostgreSQL, GraphQL, Kafka, Artifactory Servers, SonarQube, Power Automate."]
        #
        # for detail_item in skill_detail:
        #     y_position = write_justified_text(pdf, f"{detail_item}", x_position, y_position, usable_width)
        # y_position = y_position - 10

        # this the

        # Education
        y_position = add_title("Education:", y_position)
        education_detail = [
            {
                "college": "<b>Regional Labour Institute, Faridabad</b>",
                "course": "<i>PG Diploma in Industrial Safety </i>",
                "duration": "<b>Jun 2021 - Jun 2022</b>",
                "grades": "<i>Percentage : 79.2%, Silver Medalist</i>",
                "location": "<i>Haryana, India</i>"
            },
            {
                "college": "<b>National Institute of Technology, Hamirpur (NITH)</b>",
                "course": "<i>Bachelor of Technology in Chemical Engineering</i>",
                "duration": "<b>Aug 2014 - May 2018</b>",
                "grades": "<i>Percentage : 87.8%</i>",
                "location": "<i>H.P., India</i>"
            }
        ]

        # education_detail = ["<b>National Institute of Technology</b>",
        #                     "<i>Bachelor of Technology in Electronics and Communication Engineering</i> | 8.21 CGPA ",
        #                     "<b>Laxmi Public School</b>",
        #                     "<i>Senior Secondary </i> | <b>93.6%</b>"]
        for detail_item in education_detail:
            y_position = write_justified_text(pdf, f"{detail_item['college']}", x_position, y_position, usable_width,
                                              True)
            write_justified_right_text(pdf, f"{detail_item['duration']}", x_position, y_position, usable_width + 10)
            y_position = write_justified_text(pdf, f"{detail_item['course']}", x_position, y_position, usable_width)
            write_justified_right_text(pdf, f"{detail_item['location']}", x_position, y_position, usable_width + 10)
            y_position = write_justified_text(pdf, f"{detail_item['grades']}", x_position, y_position, usable_width)

        y_position = y_position - 10

        y_position = _check_for_new_page_addition(y_position)

        # Publications
        y_position = add_title("Expertise and Certification:", y_position)
        # hyperlink = '<a href="https://www.sciencedirect.com/science/article/abs/pii/S1434841118301791"><u>Energy detection based spectrum sensing for gamma shadowed α–η–μ and α–κ–μ fading channels.</u></a>'
        # hyperlink = '<a href="https://www.sciencedirect.com/science/article/abs/pii/S1434841118301791"><b>Co-Author:</b> Energy detection based spectrum sensing for gamma shadowed α–η–μ and α–κ–μ fading channels</a>'
        publication_detail = [
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
        for detail_item in publication_detail:
            y_position = write_justified_text(pdf, f"{detail_item}", x_position, y_position, usable_width, True)

        y_position = y_position - 10

        # Languages
        y_position = add_title("Languages:", y_position)
        # y_position = draw_text("Hindi (Native)\nEnglish (Fluent)", y_position)
        Languages_details = ["Hindi (Native)", "English (Fluent)"]
        # write_justified_text(pdf, f"{Languages_details}", x_position, y_position, usable_width)
        for detail_item in Languages_details:
            y_position = write_justified_text(pdf, f"{detail_item}", x_position, y_position, usable_width, True)

        y_position = y_position - 10

        # Hobbies & Interests
        y_position = add_title("Hobbies & Interests:", y_position)
        hobbies_item = "Singing, Listening to music, Travelling, Photography[Capturing Moments], Cooking/Baking."
        write_justified_text(pdf, f"{hobbies_item}", x_position, y_position, usable_width, True)

        # Save the PDF
        pdf.save()


if __name__ == "__main__":
    file_name = "../_samples/Candidate_Resume.pdf"
    resume = ResumePDF(file_name)
    resume.generate_pdf()
