# Adjusting to use only ASCII-compatible characters to avoid encoding issues
from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, txt="Resume", ln=True, align='C')
pdf.ln(10)

# Personal Information
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Nitesh Kumar Singh", ln=True, align='L')
pdf.cell(200, 10, txt="Pune, Maharashtra | +91-XXXXXXXXXX | nitesh@example.com | LinkedIn: linkedin.com/in/nitesh", ln=True, align='L')
pdf.ln(10)

# Section: Professional Summary
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Professional Summary", ln=True, align='L')
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="Experienced Senior Software Engineer with over 7 years in the automotive industry, specializing in software development and integration for embedded systems. Proficient in C, C++, and Python, with a proven track record of delivering high-quality solutions under strict deadlines. Passionate about driving innovation and process improvement.")

pdf.ln(5)

# Section: Work Experience
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Work Experience", ln=True, align='L')

# Job 1
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Senior Software Engineer", ln=True, align='L')
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Continental Automotive, Pune, Maharashtra", ln=True, align='L')
pdf.cell(200, 10, txt="January 2018 - Present", ln=True, align='L')
pdf.multi_cell(0, 10, txt="- Designed and implemented embedded software modules for automotive systems, improving efficiency by 15%.\n- Led a team of 5 engineers in developing and integrating advanced algorithms for autonomous systems.\n- Collaborated with cross-functional teams to troubleshoot and resolve critical software issues.\n- Enhanced code quality by implementing best practices and conducting regular code reviews.")

pdf.ln(5)

# Job 2
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Software Engineer", ln=True, align='L')
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="[Previous Company Name], [Location]", ln=True, align='L')
pdf.cell(200, 10, txt="July 2015 - December 2017", ln=True, align='L')
pdf.multi_cell(0, 10, txt="- Developed software solutions for embedded systems, achieving 98% functionality accuracy.\n- Optimized system performance by refactoring code and integrating advanced tools.\n- Contributed to technical documentation and training sessions for new team members.")

pdf.ln(5)

# Section: Education
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Education", ln=True, align='L')
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Bachelor of Technology in Computer Science", ln=True, align='L')
pdf.cell(200, 10, txt="[University Name], [Location]", ln=True, align='L')
pdf.cell(200, 10, txt="Graduated: 2015", ln=True, align='L')

pdf.ln(5)

# Section: Skills
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Technical Skills", ln=True, align='L')
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="- Programming Languages: C, C++, Python\n- Tools: Git, Jenkins, MATLAB\n- Expertise: Embedded systems development, software debugging, code optimization\n- Soft Skills: Leadership, Team Collaboration, Problem-Solving")

# Save the PDF to file
file_path = "./Senior_Software_Engineer_Resume.pdf"
pdf.output(file_path)

print(file_path)