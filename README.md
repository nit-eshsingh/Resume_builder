# meeting notes
https://docs.google.com/document/d/1ppqZmZcOYf7aqL9_c1vKw7kSbDsMgFltRJOLqG6K4vc/edit?tab=t.0#heading=h.mzehfgzruse

# Resume_builder
custom resume builder

# High-Level Design (HLD) for Resume Maker using ReportLab
1. Architecture Overview
The Resume Maker application will follow the MVC pattern:
Model → Manages the resume data (e.g., JSON, database).
View → Generates the PDF using ReportLab.
Controller → Handles user interactions and orchestrates data flow.
2. 
2. Design Pattern Choice
Builder Pattern: Used to construct the PDF step by step (e.g., sections like personal details, experience, education, etc.).
Singleton Pattern (if needed): Used to ensure a single instance of a PDF generator is used.
Factory Pattern (optional): Can be used to create different re sume templates dynamically.