from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication

class AddSkillsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_skills.ui', self)
        self.saveButton.clicked.connect(self.save_skills)

    def save_skills(self):
        # Collect data from input fields
        languages = self.inputLanguages.text()
        libraries = self.inputLibrariesFramework.text()
        tools = self.inputToolsTechnologies.text()
        databases = self.inputDatabases.text()
        design_patterns = self.inputDesignPatterns.text()
        others = self.inputOthers.text()

        # Print or handle the collected data
        print("Languages:", languages)
        print("Libraries/Frameworks:", libraries)
        print("Tools/Technologies:", tools)
        print("Databases:", databases)
        print("Design Patterns:", design_patterns)
        print("Others:", others)

if __name__ == '__main__':
    app = QApplication([])
    window = AddSkillsWindow()
    window.show()
    app.exec()
