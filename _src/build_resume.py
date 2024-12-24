# from reportlab.lib.pagesizes import letter
from idlelib.configdialog import font_sample_text
# user driver ride userdriverride  payment
from reportlab.lib.pagesizes import C4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph


EMAILID = "niteshksmgs@gmail.com"
PHONE = "+91-9882545465"
LINKEDIN = "linkedin.com/in/niteshksmgs19/"
ADDRESS = "Bangalore, India"

styles = getSampleStyleSheet()
style = styles['Normal']

PARAGRAPH_STYLE = ParagraphStyle(
    "Style",
    fontName='Times-Roman',
    alignment=4
)


def create_stylized_resume_pdf(file_name):
    # Create the PDF canvas
    pdf = canvas.Canvas(file_name, pagesize=C4)
    page_width, page_height = C4 # page_width 649 page_height 918
    left_margin = right_margin = top_margin = bottom_margin = 50
    usable_width = page_width - left_margin - right_margin
    usable_height = page_height - top_margin - bottom_margin

    # Starting y-position for content
    x_postion = left_margin
    y_position = page_height - top_margin # 868

    # Function to draw a horizontal line
    def draw_line(y):
        pdf.setStrokeColor(colors.black)
        pdf.setLineWidth(1)
        pdf.line(30, y, page_width - 30, y)
        return y - 5

    # Function to add a section title with a horizontal line
    def add_title(text, y):
        y -= 10
        pdf.setFont("Helvetica-Bold", 14)
        pdf.setFillColor(colors.blue)
        pdf.drawString(30, y, text)
        pdf.setFillColor(colors.black)
        return draw_line(y - 10)

    # Function to add regular text
    def add_text(text, y, indent=0, bold=False):
        if bold:
            pdf.setFont("Helvetica-Bold", 14)
        else:
            pdf.setFont("Helvetica", 12)
        for line in text.split("\n"):
            paragraph = Paragraph(line,style=PARAGRAPH_STYLE)
            width,height = paragraph.wrap(usable_width, usable_height)
            print(width,height)

            pdf.drawString(30 + indent, y, line)
            y = y - 14
        return y

    # Header
    pdf.setFont("Helvetica-Bold", 20)
    pdf.setFillColor(colors.black)
    # pdf.drawString(30,y_position, "NITESH KUMAR SINGH")
    pdf.drawCentredString(
        page_width/2,
        y_position,
        "NITESH KUMAR SINGH",
        mode=0)
    y_position = add_text(
        f"{ADDRESS} | {PHONE} | {EMAILID} | {LINKEDIN}",
        y_position - 20
    )
    y_position = draw_line(y_position - 10)
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(colors.black)
    # y_position = add_text(
    #     "A self-directed and motivated engineer experienced working effectively in dynamic environments. \n"
    #     "Fluent in Python programming language and DevOps tools like Jenkins and AWS.",
    #     y_position
    # )

    # Contact Information
    # y_position = add_title("Contact Information:", y_position)


    # Professional Experience
    y_position = add_title("Experience:", y_position)
    experiences = [
        {
            "role": "Technical Specialist",
            "company": "CONTINENTAL AG",
            "duration": "July 2022 - Present",
            "details": [
                "\u2022 Designed and implemented the ETL transformation process from Kafka streams to MongoDB, resulting in continuous data processing and a significant reduction in latency.",
                "\u2022 Developed a multi-branch pipeline using Jenkinsfile, streamlining the deployment process and ensuring efficient code integration across different projects.",
                "\u2022 Successfully deployed our local server on AWS using a Linux-based EC2 server and ODBC connector installation, optimizing infrastructure and enabling seamless scalability.",
                "\u2022 Utilized Plant UML, database schemas, sequence diagrams, dynamic logger, and Confluence to ensure continuity in operations and effective collaboration with team members.",
                "\u2022 Implemented static tool analyzers, including SonarQube, to improve code quality and maintain high standards of software development.",
                "\u2022 Generated graphical representations of builds into plots on AWS server for visualization and analysis of code quality, facilitating data-driven decision making and continuous improvement.",
                "\u2022 Developed web scraping techniques to extract data from Jira servers for ADAS projects, solved B+ tree of parent-child model using memoization.",
                "\u2022 Built data extraction from GraphQL web service API response using multiprocessing for synchronization with the database, enhancing data integrity and system efficiency.",
                "\u2022 Created a Microsoft flow using Power Automate diagram to obtain continuous integration of gateway failure into a Power BI report, enabling real-time monitoring.",
                "\u2022 Collaborated with cross-functional teams to ensure seamless integration of ETL processes and web scraping techniques from different servers.",
                "\u2022 Developed a OSS report generator project to scan all the python packages used inside the project and create a report for scanning for license clearance. Ex- MIT, Apache, BSD and GPL.\n"
            ]
        },
        {
            "role": "Senior Software Engineer",
            "company": "Bosch Global Software Technologies",
            "duration": "Aug 2018 - July 2022",
            "details": [
                "\u2022 Spearheaded a development team in the creation of a software application for configuring communication in heavy automotive, leveraging the power and versatility of Python and the PyQt5.",
                "\u2022 Developed Python tools, both command-line interface based and desktop applications, for mobile hydraulics, enhancing efficiency and productivity.",
                "\u2022 Created a project Elf2A2L to parse non-human readable files Executable and Linkable Format (.elf) for data analytics and conversion into a readable format ASAM MCD-2 MC Language.(.a2l), improving data accessibility and usability.",
                "\u2022 Served as Scrum Master and Engineering Product Quality (EPQ) auditor for a Web framework development project, ensuring adherence of CMMI level-5 standard.",
                "\u2022 Enhanced the user experience by simplifying the process of automatic code generation, for heavy mobile hydraulic vehicle for different OEMs.",
                "\u2022 Created a robust back-end data handling structure using established software design patterns, enhancing the reliability and scalability of the software development.",
                "\u2022 Optimized software performance by reducing execution time by up to 50%, improving overall system efficiency and responsiveness.",
                "\u2022 Implemented Jenkins pipeline stages, including repository checkout, static code analyzer, test run on source code, FOSS ID run (OSS report generation), executable creation, test run on executable and delivery.",
                "\u2022 Designed a user-friendly HMI panel for control-x hardware used for Drives and controls using UI/UX Touchgfx software from stm32."
            ]
        }
    ]

    for exp in experiences:
        y_position = add_text(f"{exp['role']} - {exp['company']} ({exp['duration']})", y_position, bold=True)
        for detail in exp['details']:
            y_position = add_text(f"{detail}", y_position, indent=10)

    # Education
    y_position = add_title("Education:", y_position)
    y_position = add_text(
        "B.Tech in Electronics and Communication Engineering, NIT Hamirpur (2014 - 2018) | 8.21 CGPA\n"
        "Senior Secondary, Laxmi Public School (2011 - 2013) | 93.6%",
        y_position
    )

    # Skills
    y_position = add_title("Skills:", y_position)
    y_position = add_text(
        "Python: PySpark, PyQt5, Web Scraping, pandas, numpy, psycopg2\n"
        "DevOps: AWS, Jenkins, Groovy, Batch Script, FOSS ID\n"
        "Design Patterns: UML Diagrams, DB Schemas, Sequence Diagram, ETL\n"
        "Others: MongoDB, GraphQL, Kafka, Artifactory Servers, SonarQube, Power Automate",
        y_position
    )

    # Publications
    y_position = add_title("Publications:", y_position)
    y_position = add_text(
        'Co-Author: "Energy detection based spectrum sensing for gamma shadowed α–η–μ and α–κ–μ fading channels"\n'
        "Journal: International Journal of Electronics and Communications\nPublished: September 1, 2018",
        y_position
    )

    # Languages
    y_position = add_title("Languages:", y_position)
    y_position = add_text("Hindi (Native)\nEnglish (Fluent)", y_position)

    # Hobbies & Interests
    y_position = add_title("Hobbies & Interests:", y_position)
    y_position = add_text(
        "Traveling and exploring places\nListening to music\nPlaying Cricket, Chess, Badminton, and Table Tennis",
        y_position
    )

    # Save the PDF
    pdf.save()

# File name for the PDF
file_name = "Nitesh_Kumar_Singh_Resume.pdf"
create_stylized_resume_pdf(file_name)

print(f"PDF file '{file_name}' created successfully!")

