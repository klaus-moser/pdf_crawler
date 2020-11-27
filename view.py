from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *


class View(QMainWindow):
    """View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.width = 628
        self.height = 600
        self.setWindowTitle("PDF-Crawler")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setFixedSize(self.width, self.height)
        # Set the central widget and the general layout
        self._centralWidget = QWidget(self)
        # Create the display, input, buttons, checkboxes etc.
        self._create_result_display()
        self._create_buttons()
        self._create_input_box()
        self._set_labels()
        self._create_path_box()
        self._create_checkboxes()
        # Create pop-ups
        self._create_pop_ups()
        # Add to screen/central widget
        self.setCentralWidget(self._centralWidget)
        # Progressbar
        self._create_progress_bar()

    def _create_progress_bar(self):
        self.progressbar = QProgressBar(self._centralWidget)
        self.progressbar.setMaximum(100)
        self.progressbar.setGeometry(105, 561, 300, 30)

    def _create_pop_ups(self):
        """Create & init the pop-up windows."""
        # Info Pop-Up
        self.info_pop_up = QMessageBox(self._centralWidget)
        self.info_pop_up.setWindowTitle("Information")
        self.info_pop_up.setIcon(QMessageBox.Information)
        self.info_pop_up.setStandardButtons(QMessageBox.Close)
        # Warning Pop-Up
        self.warning_pop_up = QMessageBox(self._centralWidget)
        self.warning_pop_up.setWindowTitle("Notion!")
        self.warning_pop_up.setIcon(QMessageBox.Warning)
        self.warning_pop_up.setStandardButtons(QMessageBox.Close)

    def _set_labels(self):
        """Set all labels"""
        # Create the label widget(s)
        self.label = QLabel(self._centralWidget)
        self.label_info = QLabel(self._centralWidget)
        self.label_path = QLabel(self._centralWidget)
        self.label_word = QLabel(self._centralWidget)
        # Set label properties
        self.label_info.setGeometry(10, 170, 300, 20)
        self.label.setGeometry(10, 10, 611, 141)
        self.label_path.setGeometry(10, 210, 47, 13)
        self.label_word.setGeometry(10, 250, 47, 13)
        # Set label texts
        self.label.setText("")
        self.label_info.setText("Choose between:")
        self.label_path.setText("Path:")
        self.label_word.setText("Word:")
        # Set logo file
        self.label.setPixmap(QPixmap("logo.PNG"))
        self.label.setScaledContents(False)

    def _create_path_box(self):
        """Create Input Box for the path"""
        # Create the path widget
        self.path_box = QTextEdit(self._centralWidget)
        # Set some properties
        self.path_box.setGeometry(55, 200, 380, 31)

    def _create_input_box(self):
        """Create Input Box for the word"""
        # Create input box for search word.
        self.input_box_word = QLineEdit(self._centralWidget)
        # Set some properties
        self.input_box_word.setGeometry(55, 240, 380, 31)

    def _create_result_display(self):
        """Create the box to show the results"""
        # Create the display widget
        self.display = QPlainTextEdit(self._centralWidget)
        # Set some display's properties
        self.display.setGeometry(10, 280, 611, 271)
        self.display.setReadOnly(True)

    def _create_buttons(self):
        """Create the buttons."""
        self.buttons = {}
        # Button text | position
        buttons = {
            "Browse": (445, 200, 85, 31),
            "Set Default": (537, 200, 85, 31),
            "Start": (445, 240, 85, 31),
            "Info": (537, 160, 85, 31),
            "End": (537, 560, 85, 31),
            "Cancel": (10, 560, 85, 31),
            "Save as .txt": (435, 560, 95, 31),
            "Clear": (537, 240, 85, 31)
        }
        # Create the buttons
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(self._centralWidget)
            self.buttons[btnText].setText(btnText)
            self.buttons[btnText].setGeometry(pos[0], pos[1], pos[2], pos[3])

    def _create_checkboxes(self):
        """Create all check boxes."""
        self.checkbox_file = QCheckBox(self._centralWidget)
        self.checkbox_dir = QCheckBox(self._centralWidget)
        self.checkbox_file.setGeometry(260, 170, 100, 20)
        self.checkbox_dir.setGeometry(150, 170, 100, 20)
        # Set text
        self.checkbox_dir.setText("Directory")
        self.checkbox_file.setText("File")
        # Default state checkboxes
        self.checkbox_dir.setChecked(True)
        self.checkbox_file.setChecked(False)

    def btn_state(self, check_box):
        """Check the state of the checkboxes."""
        self.set_path_text("")
        if check_box.text() == "Directory":
            if check_box.isChecked():
                self.checkbox_file.setChecked(False)
            else:
                self.checkbox_file.setChecked(True)

        elif check_box.text() == "File":
            if check_box.isChecked():
                self.checkbox_dir.setChecked(False)
            else:
                self.checkbox_dir.setChecked(True)

    def set_display_text(self, text):
        """Set display's text."""
        for line in text:
            t = "File: {}\tPage: {}\tMatches: {}".format(line[0], line[1], line[2])
            self.display.appendPlainText(t)
        self.display.setFocus()

    def set_path_text(self, path):
        """Set the text in the path label."""
        self.path_box.setText(path)

    def display_text(self):
        """Get display's text."""
        return self.display.toPlainText()

    def clear_display(self):
        """Clear the display."""
        self.display.setPlainText("")

    def show_dir_dialog(self, home_dir):
        """Show dir dialog."""
        return QFileDialog.getExistingDirectory(self, 'Choose folder', home_dir)

    def show_file_dialog(self, home_dir):
        """Show file dialog."""
        filter_ = "Pfd files (*.pdf)"
        path = QFileDialog.getOpenFileName(self, 'Choose folder', home_dir, filter=filter_)
        return path[0]

    def get_path_to_save(self, home_dir):
        """Dialog to choose a path to save the results."""
        return QFileDialog.getSaveFileName(self, "Save Results", home_dir, filter="*.txt")

    def show_information(self, text):
        """Pop-Up window to show usage and general information."""
        self.info_pop_up.setText(text)
        self.info_pop_up.exec_()

    def show_warning(self, state):
        """Pop-Up to warn user to choose path or word."""
        self.warning_pop_up.setText(state)
        self.warning_pop_up.exec_()

    def get_word_text(self):
        """Returns the word."""
        return self.input_box_word.text()


if __name__ == "__main__":
    print(__file__)
