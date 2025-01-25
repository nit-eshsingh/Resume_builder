import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QMessageBox,
)


class AddWorkExperienceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi("../_frontend/work_experience.ui", self)

        # Initialize an empty list to store work experience data
        self.work_experience_data = []

        # Connect the save button to the handler function
        self.saveButton.clicked.connect(self.save_work_experience)

        # Initialize the table view
        self.initialize_table()

    def initialize_table(self):
        """Initialize the QTableWidget for displaying work experience."""
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Years", "Company Name", "Position", "Experience"])
        self.tableWidget.setRowCount(0)  # Start with no rows

    def save_work_experience(self):
        """Save work experience data and display it in the table."""
        # Get input data
        years = self.inputYears.text()
        company_name = self.inputCompanyName.text()
        position = self.inputPosition.text()
        experience = self.inputExperience.toPlainText()

        # Validate required fields
        if not years or not company_name or not position:
            QMessageBox.warning(self, "Input Error", "Years, Company Name, and Position are required fields!")
            return

        # Add the data to the list
        work_experience_entry = [years, company_name, position, experience]
        self.work_experience_data.append(work_experience_entry)

        # Update the table view
        self.update_table()

        # Clear the input fields after saving
        self.clear_inputs()

    def update_table(self):
        """Update the table view with the current work experience data."""
        self.tableWidget.setRowCount(len(self.work_experience_data))
        for row_index, row_data in enumerate(self.work_experience_data):
            for col_index, value in enumerate(row_data):
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(value))

    def clear_inputs(self):
        """Clear all input fields."""
        self.inputYears.clear()
        self.inputCompanyName.clear()
        self.inputPosition.clear()
        self.inputExperience.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddWorkExperienceApp()
    window.show()
    sys.exit(app.exec())
