import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QMessageBox,
)


class AddEducationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi("education.ui", self)

        # Initialize an empty list to store education data
        self.education_data = []

        # Connect the save button to the handler function
        self.saveButton.clicked.connect(self.save_education)

        # Initialize the table view
        self.initialize_table()

    def initialize_table(self):
        """Initialize the QTableWidget for displaying education data."""
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Year", "Institute", "Degree", "Grades", "Location"])
        self.tableWidget.setRowCount(0)  # Start with no rows

    def save_education(self):
        """Save education data and display it in the table."""
        # Get input data
        year = self.inputYear.text()
        institute = self.inputInstitute.text()
        degree = self.inputDegree.text()
        grades = self.inputGrades.text()
        location = self.inputLocation.text()

        # Validate required fields
        if not year or not institute or not degree:
            QMessageBox.warning(self, "Input Error", "Year, Institute, and Degree are required fields!")
            return

        # Add the data to the list
        education_entry = [year, institute, degree, grades, location]
        self.education_data.append(education_entry)

        # Update the table view
        self.update_table()

        # Clear the input fields after saving
        self.clear_inputs()

    def update_table(self):
        """Update the table view with the current education data."""
        self.tableWidget.setRowCount(len(self.education_data))
        for row_index, row_data in enumerate(self.education_data):
            for col_index, value in enumerate(row_data):
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(value))

    def clear_inputs(self):
        """Clear all input fields."""
        self.inputYear.clear()
        self.inputInstitute.clear()
        self.inputDegree.clear()
        self.inputGrades.clear()
        self.inputLocation.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddEducationApp()
    window.show()
    sys.exit(app.exec())
