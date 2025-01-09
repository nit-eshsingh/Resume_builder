# from idlelib.configdialog import font_sample_text
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.platypus import Paragraph
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import C4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

RESUME_NAME = "NITESH KUMAR SINGH"
EMAILID = "niteshksmgs@gmail.com"
PHONE = "+91-9882545465"
# LINKEDIN = "linkedin.com/in/niteshksmgs19/"
LINKEDIN = '<a href="https://www.linkedin.com/in/niteshksmgs19/"><u>linkedin.com/in/niteshksmgs19/</u></a>'
ADDRESS = "Bangalore, India"

# styles = getSampleStyleSheet()
# style = styles['Normal']
#
# PARAGRAPH_STYLE = ParagraphStyle(
#     "Style",
#     fontName='Times-Roman',
#     alignment=4
# )




# def draw_aligned_text(canvas, text, x, y, width):
#     # Create a Paragraph with justified alignment
#     styles = getSampleStyleSheet()
#     style = styles['BodyText']
#     style.alignment = 4  # 4 corresponds to justified alignment
#
#     # Create a Paragraph
#     paragraph = Paragraph(text, style)
#
#     # Create a "fake" frame to wrap and justify text
#     _, height = paragraph.wrap(width, 0)  # Calculate the height needed for the text
#     paragraph.drawOn(canvas, x, y - height)  # Draw the text on the canvas
#
#
# # Define text and canvas
# text = "This is an example of a long paragraph that will be wrapped and aligned with justification on a canvas. Justified alignment ensures that the text is evenly distributed across the width, creating a clean and professional appearance."
#
# c = canvas.Canvas("justified_text_wrap.pdf", pagesize=letter)
# page_width, page_height = letter
#
# # Define position and width for the text block
# x = 50
# y = page_height - 50
# text_width = 500
#
# # Draw justified text
# draw_aligned_text(c, text, x, y, text_width)
#
# # Save the canvas
# c.save()


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

    # Function to draw a horizontal line
    def draw_line(y_position):
        # pass
        pdf.setStrokeColor(colors.rgb2cmyk(0,0,9))
        pdf.setLineWidth(1)
        pdf.line(left_margin, y_position, usable_width + right_margin, y_position)
        print(f"{y_position} ,drawed_line")
        return y_position - 5

    # Function to add a section title with a horizontal line
    def add_title(text, y_position):
        y_position = y_position - 10
        pdf.setFont("Helvetica-Bold", 14)
        pdf.setFillColor(colors.rgb2cmyk(0,0,9))
        pdf.drawString(30, y_position, text)
        pdf.setFillColor(colors.black)
        print(f"{x_position},{y_position},add_title {text}")
        return draw_line(y_position - 5)

    def write_justified_text(pdf, text, x_position, y_position, usable_width):
        # Create a Paragraph with justified alignment
        styles = getSampleStyleSheet()
        style = styles['Bullet']
        # style = styles['BodyText']
        style.alignment = 4  # 4 corresponds to justified alignment

        # Create a Paragraph
        paragraph = Paragraph(text, style)

        # Create a "fake" frame to wrap and justify text
        _, height = paragraph.wrap(usable_width, 0)  # Calculate the height needed for the text
        paragraph.drawOn(pdf, x_position + 20, int(y_position) - height)
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
        style = styles['BodyText']
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
            # paragraph = Paragraph(line,style=PARAGRAPH_STYLE)
            # width,height = paragraph.wrap(usable_width, usable_height)
            # print(width,height)

            pdf.drawString(30 + indent, y_position, line)
            y_position = y_position - 8
            print(f"{x_position},{y_position} ,draw_text {text}")
        return y_position

    y_position = write_justified_centered_text(pdf, f"<b>{RESUME_NAME}</b>",x_position, y_position, usable_width, styling="Heading1")
    personal_detail = f"<b>{ADDRESS} | {PHONE} | <u>{EMAILID}</u> | <u>{LINKEDIN}</u></b>"

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


    # Professional Experience
    y_position = add_title("Experience:", y_position)
    print(y_position, "Experience")
    bold_characters = {"ETL": "<b>ETL</b>", "Kafka": "<b>Kafka</b>"}
    experiences = [
        {
            "role": "Senior Software Engineer",
            "company": "BMW Techworks",
            "duration": "Jan 2025 - Present",
            "details": [
                f"\u2022 Developed a multi-branch pipeline using <b>Jenkinsfile</b>, streamlining the deployment process "
                f"and ensuring efficient code integration across different projects.",
            ]
        },
        {
            "role": "Technical Specialist",
            "company": "CONTINENTAL Automotive",
            "duration": "July 2022 - Jan 2025",
            "details": [
                f"\u2022 Implemented an {bold_characters.get('ETL')} process to transform {bold_characters.get('Kafka')} streams into MongoDB, enabling continuous data processing with reduced latency.",
                f"\u2022 Developed a multi-branch pipeline using <b>Jenkinsfile</b>, streamlining the deployment process "
                f"and ensuring efficient code integration across different projects.",
                f"\u2022 Successfully deployed our local server on <b>AWS</b> using a Linux-based EC2 server and ODBC connector installation, optimizing infrastructure and enabling seamless scalability.",
                f"\u2022 Utilized Plant <b>UML</b>, database schemas, sequence diagrams, dynamic logger, and Confluence to ensure continuity in operations and effective collaboration with team members.",
                f"\u2022 Implemented static tool analyzers, including <b>SonarQube</b>, to improve code quality and maintain high standards of software development.",
                f"\u2022 Generated <b>graphical</b> representations of builds into plots on AWS server for visualization and analysis of code quality, facilitating data-driven decision making and continuous improvement.",
                f"\u2022 Developed web scraping techniques to extract data from Jira servers for ADAS projects, solved B+ tree of parent-child model using <b>memoization</b>.",
                f"\u2022 Built data extraction from <b>GraphQL</b> web service API response using <b>multiprocessing</b> for synchronization with the database, enhancing data integrity and system efficiency.",
                f"\u2022 Created a Microsoft flow using <b>Power Automate</b> diagram to obtain continuous integration of gateway failure into a Power BI report, enabling real-time monitoring.",
                f"\u2022 Collaborated with cross-functional teams to ensure seamless integration of ETL processes and <b>web scraping</b> techniques from different servers.",
                f"\u2022 Developed a <b>OSS</b> report generator project to scan all the python packages used inside the project and create a report for scanning for license clearance. Ex- MIT, Apache, BSD and GPL.\n"
            ]
        },
        {
            "role": "Senior Software Engineer",
            "company": "Bosch Global Software Technologies",
            "duration": "Aug 2018 - July 2022",
            "details": [
                "\u2022 <b>Spearheaded</b> a development team in the creation of a software application for configuring "
                "communication in heavy automotive, leveraging the power and versatility of Python and the <b>PyQt5.</b>",
                "\u2022 Developed Python tools, both command-line interface based and desktop applications, for mobile hydraulics, enhancing efficiency and productivity.",
                "\u2022 Created a project <b>Elf2A2L</b> to parse non-human readable files Executable and Linkable Format (.elf) for data analytics and conversion into a readable format ASAM MCD-2 MC Language.(.a2l), improving data accessibility and usability.",
                "\u2022 Served as <b>Scrum Master</b> and Engineering Product Quality (<b>EPQ</b>) auditor for a Web framework development project, ensuring adherence of CMMI level-5 standard.",
                "\u2022 Enhanced the user experience by simplifying the process of automatic code generation, for heavy mobile hydraulic vehicle for different <b>OEMs</b>.",
                "\u2022 Created a robust back-end data handling structure using established software design patterns, enhancing the reliability and scalability of the software development.",
                "\u2022 Optimized software performance by reducing execution time by up to <b>50%</b>, improving overall system efficiency and responsiveness.",
                "\u2022 Implemented Jenkins pipeline stages, including repository checkout, static code analyzer, test run on source code, <b>FOSS ID</b> run (OSS report generation), executable creation, test run on executable and delivery.",
                "\u2022 Designed a user-friendly <b>HMI panel</b> for control-x hardware used for Drives and controls using UI/UX Touchgfx software from stm32.",
            ]
        }
    ]

    for exp in experiences:
        y_position = y_position - 8
        print(y_position, "experiences in loop")
        # write_justified_right_text()
        write_justified_right_text(pdf, f"<b>{exp['duration']}</b>", x_position, y_position, usable_width+10)
        y_position = draw_text(f"{exp['role']} | {exp['company']}", y_position, bold=True)
        for detail in exp['details']:
            # print(y_position, "loop")
            y_position = write_justified_text(pdf,f"{detail}",x_position, y_position, usable_width)
            # print(y_position, "return loop")
        y_position = y_position - 14

    # Skills
    y_position = add_title("Skills:", y_position)
    # y_position = draw_text(
    #     "Python: PySpark, PyQt5, Web Scraping, pandas, numpy, psycopg2\n"
    #     "DevOps: AWS, Jenkins, Groovy, Batch Script, FOSS ID\n"
    #     "Design Patterns: UML Diagrams, DB Schemas, Sequence Diagram, ETL\n"
    #     "Others: MongoDB, GraphQL, Kafka, Artifactory Servers, SonarQube, Power Automate",
    #     y_position
    # )
    skill_detail = ["<b>Python:</b>PySpark, fastapi, PyQt5, Web Scraping, pandas, numpy, psycopg2.\n",
                    "<b>DevOps :</b> AWS, Jenkins, Groovy, Batch Script, FOSS ID.\n",
                    "<b>Design Patterns :</b> UML Diagrams, DB Schemas, Sequence Diagram, ETL.\n",
                    "<b>Others :</b> MongoDB, PostgreSQL, GraphQL, Kafka, Artifactory Servers, SonarQube, Power Automate."]

    for detail_item in skill_detail:
        y_position = write_justified_text(pdf, f"{detail_item}", x_position, y_position, usable_width)
    y_position = y_position - 10

    # Education
    y_position = add_title("Education:", y_position)
    education_detail = [
        {
            "college": "<b>National Institute of Technology, Hamirpur (NITH)</b>",
            "course": "<i>Bachelor of Technology in Electronics and Communication Engineering</i>",
            "duration": "<b>Aug 2014 - May 2018</b>",
            "grades": "<i>CGPA : 8.21</i>",
            "location": "<i>H.P., India</i>"
        },
        {
            "college": "<b>Laxmi Public School (LPS)</b>",
            "course": "<i>Senior Secondary </i>",
            "duration": "<b>Apr 2011 - May 2013</b>",
            "grades": "<i>Percentage : 93.6%</i>",
            "location": "<i>DDU, U.P., India</i>"
        }
    ]

    # education_detail = ["<b>National Institute of Technology</b>",
    #                     "<i>Bachelor of Technology in Electronics and Communication Engineering</i> | 8.21 CGPA ",
    #                     "<b>Laxmi Public School</b>",
    #                     "<i>Senior Secondary </i> | <b>93.6%</b>"]
    for detail_item in education_detail:
        y_position = write_justified_text(pdf, f"{detail_item['college']}", x_position, y_position, usable_width)
        write_justified_right_text(pdf, f"{detail_item['duration']}", x_position, y_position, usable_width + 10)
        y_position = write_justified_text(pdf, f"{detail_item['course']} | {detail_item['grades']}", x_position, y_position, usable_width)
        write_justified_right_text(pdf, f"{detail_item['location']}", x_position, y_position, usable_width + 10)
    y_position = y_position - 10

    # Publications
    y_position = add_title("Publications:", y_position)
    hyperlink = '<a href="https://www.sciencedirect.com/science/article/abs/pii/S1434841118301791"><u>Energy detection based spectrum sensing for gamma shadowed α–η–μ and α–κ–μ fading channels.</u></a>'
    # hyperlink = '<a href="https://www.sciencedirect.com/science/article/abs/pii/S1434841118301791"><b>Co-Author:</b> Energy detection based spectrum sensing for gamma shadowed α–η–μ and α–κ–μ fading channels</a>'
    publication_detail = [f"<b>Co-Author: {hyperlink}</b>",
        "<b>Journal:</b> International Journal of Electronics and Communications",
        "<b>Published:</b> September 1, 2018",
        "Collaborated with Dr. Sandeep Kumar (Principal Scientist), Dr. Kuldeep Singh and the research team to design and implement innovative solutions enhancing radar navigation systems through advanced spectrum sensing techniques."]
    for detail_item in publication_detail:
        y_position = write_justified_text(pdf, f"{detail_item}", x_position, y_position, usable_width)

    y_position = y_position - 10

    # Languages
    # y_position = add_title("Languages:", y_position)
    # y_position = draw_text("Hindi (Native)\nEnglish (Fluent)", y_position)

    # Hobbies & Interests
    y_position = add_title("Hobbies & Interests:", y_position)
    hobbies_item = "Traveling and exploring places, Listening to music, Chess, Badminton, and Table Tennis"
    write_justified_text(pdf, f"{hobbies_item}", x_position, y_position, usable_width)

    # Save the PDF
    pdf.save()

# File name for the PDF
file_name = "Nitesh_Kumar_Singh.pdf"
create_stylized_resume_pdf(file_name)

print(f"PDF file '{file_name}' created successfully!")

