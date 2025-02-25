from reportlab.lib.pagesizes import C4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

RESUME_NAME = "RANJANA KASHYAP"
EMAILID = "ranjananithamirpur@gmail.com"
PHONE = "+91-9736043013"
# LINKEDIN = "linkedin.com/in/niteshksmgs19/"
LINKEDIN = '<a href="https://www.linkedin.com/in/ranjana-kashyap-3bb426130/"><u>linkedin.com/in/ranjanakashyap/</u></a>'
ADDRESS = "Gurugram"



def create_stylized_resume_pdf(file_name):
    # Create the PDF canvas
    pdf = canvas.Canvas(file_name, pagesize=C4)
    page_width, page_height = C4 # page_width 649 page_height 918
    left_margin = 30
    right_margin = 50
    top_margin = 30
    bottom_margin = 30
    usable_width = int(page_width) - left_margin - right_margin
    usable_height = int(page_height) - top_margin - bottom_margin

    # Starting y-position for content
    x_position = left_margin
    y_position = int(page_height) - top_margin # 868

    def _image_insertion():
        # Define the circular image file path
        # image_path = "circular_ranjana_image.png"  # Ensure this is a circular PNG with transparency
        image_path = "ranjana_pic_new.png"
        # Position and size of the circular image
        image_x_position = 515   # X coordinate
        image_y_position = 790  # Y coordinate
        image_width = 115  # Desired width
        image_height = 125  # Desired height

        # Draw the circular PNG image at the specified position
        pdf.drawImage(image_path, image_x_position, image_y_position, width=image_width, height=image_height,
                      mask='auto')

    #function to check for new page
    def _check_for_new_page_addition(y_position):
        if y_position:# < bottom_margin:  # Check if space is left on the page
            pdf.showPage()  # Add a new page
            y_position = int(page_height) - top_margin
            return y_position

    # Function to draw a horizontal line
    def draw_line(y_position, objective=None):
        # pass
        # x2_position = 0
        # if objective:
        #     x2_position = usable_width - right_margin
        # else:
        x2_position = usable_width + right_margin
        pdf.setStrokeColor(colors.rgb2cmyk(0,0,9))
        pdf.setLineWidth(1)
        pdf.line(left_margin, y_position, x2_position, y_position)
        print(f"{y_position} ,drawed_line")
        return y_position - 5

    # Function to add a section title with a horizontal line
    def add_title(text, y_position, objective=None):
        y_position = y_position - 10
        pdf.setFont("Helvetica-Bold", 14)
        pdf.setFillColor(colors.rgb2cmyk(0,0,9))
        pdf.drawString(30, y_position, text)
        pdf.setFillColor(colors.black)
        print(f"{x_position},{y_position},add_title {text}")
        return draw_line(y_position - 5, objective)

    def write_justified_text(pdf, text, x_position, y_position, usable_width, bullet_points=False):
        # Create a Paragraph with justified alignment
        style = ParagraphStyle('Bullet')
        # style = styles['Bullet']
        # style = styles['BodyText']
        style.alignment = 4  # 4 corresponds to justified alignment
        # draw_text("•", y_position, indent=0, bold=False)
        # pdf.drawString(x_position, y_position, "•")
        # Create a Paragraph
        paragraph = Paragraph(text, style)

        # Create a "fake" frame to wrap and justify text
        _, height = paragraph.wrap(usable_width, 0)  # Calculate the height needed for the text
        if bullet_points:
            pdf.drawString(x_position + 5, int(y_position) - 11, "•")
        paragraph.drawOn(pdf, x_position + 15, int(y_position) - height)
        print(f"before y_position {y_position}")
        y_position = y_position - height
        print(f"{x_position},{y_position} ,draw_aligned_text {text}")
        return y_position# Draw the text on the canvas

    def write_justified_centered_text(pdf, text, x_position, y_position, usable_width, styling=None):
        # Create a Paragraph with justified alignment
        styles = getSampleStyleSheet()
        if styling == "Heading1":
            style = styles['Heading1']
            style.alignment = 1  # 4 corresponds to justified alignment
        if styling == "Normal":
            # styles = getSampleStyleSheet()
            style = styles['Normal']
            style.alignment = 1  # 4 corresponds to justified alignment
        pdf.setFillColor(colors.rgb2cmyk(0, 0, 9))
        paragraph = Paragraph(text, style)
        # Create a "fake" frame to wrap and justify text
        _, height = paragraph.wrap(usable_width, usable_height)  # Calculate the height needed for the text
        paragraph.drawOn(pdf, x_position, int(y_position))
        pdf.setFillColor(colors.black)
        print(f"before y_position {y_position}")
        y_position = y_position - height
        print(f"{x_position},{y_position} ,write_justified_centered_text {text}")
        return y_position# Draw the text on the canvas

    def write_justified_right_text(pdf, text, x_position, y_position, usable_width):
        # Create a Paragraph with justified alignment
        styles = getSampleStyleSheet()
        style = styles['Normal']
        style.alignment = 2  # 2 corresponds to right alignment

        # Create a Paragraph
        paragraph = Paragraph(text, style)

        # Create a "fake" frame to wrap and justify text
        _, height = paragraph.wrap(usable_width, 0)  # Calculate the height needed for the text
        paragraph.drawOn(pdf, x_position, int(y_position))
        print(f"before y_position {y_position}")
        # y_position = y_position - height
        print(f"{x_position},{y_position} ,write_justified_right_text {text}")
        return y_position# Draw the text on the canvas

    # Function to add regular text
    def draw_text(text, y_position, indent=0, bold=False):
        if bold:
            pdf.setFont("Helvetica-Bold", 12)
        else:
            pdf.setFont("Helvetica", 11)
        for line in text.split("\n"):
            pdf.drawString(30 + indent, y_position, line)
            y_position = y_position - 8
            print(f"{x_position},{y_position} ,draw_text {text}")
        return y_position

    # _image_insertion()

    y_position = write_justified_centered_text(pdf, f"<u><b>{RESUME_NAME}</b></u>",x_position, y_position, usable_width, styling="Heading1")
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
        write_justified_right_text(pdf, f"<b>{exp['duration']}</b>", x_position, y_position, usable_width+10)
        y_position = draw_text(f"{exp['role']} | {exp['company']}", y_position, bold=True)
        for detail in exp['details']:
            # print(y_position, "loop")
            y_position = write_justified_text(pdf,f"{detail}",x_position, y_position, usable_width, True)
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
        y_position = write_justified_text(pdf, f"{detail_item['college']}", x_position, y_position, usable_width, True)
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
    Languages_details = ["Hindi (Native)","English (Fluent)"]
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

# File name for the PDF
file_name = "../_samples/Ranjana_Kashyap_Resume.pdf"
create_stylized_resume_pdf(file_name)

print(f"PDF file '{file_name}' created successfully!")

