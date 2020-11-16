# model_view_controller.py
import sys
from os.path import dirname, abspath
from pathlib import Path

import basic_backend
import mvc_exceptions as mvc_exc
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QPlainTextEdit, QLabel, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


__version__ = "0.1"
__author__ = "Klaus Moser"


class ModelBasic:

    def set_default_path(self, path):
        basic_backend.set_default_path(path=path)

    def get_default_path(self):
        return basic_backend.get_default_path()

    def crawl(self, path, word):
        basic_backend.walk_folder(folder_path=path)
        basic_backend.walk_pdf_files(word=word)

    def get_results(self):
        return basic_backend.items.copy()

    def delete_log(self):
        basic_backend.delete_log()

    def get_home_dir(self):
        return basic_backend.get_home_dir()


class View(QMainWindow):
    """PDFCrawler's View (GUI)."""

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

        # Create the display, input, buttons etc.
        self._create_result_display()
        self._create_buttons()
        self._create_input_box()
        self._set_labels()
        self._create_path_box()
        # Add to screen/central widget
        self.setCentralWidget(self._centralWidget)

    def _set_labels(self):
        """Set all labels"""
        # Create the label widget(s)
        self.label = QLabel(self._centralWidget)
        self.label_path = QLabel(self._centralWidget)
        self.label_word = QLabel(self._centralWidget)
        # Set label properties
        self.label.setGeometry(10, 10, 611, 141)
        self.label_path.setGeometry(10, 210, 47, 13)
        self.label_word.setGeometry(10, 250, 47, 13)
        # Set label texts
        self.label.setText("")
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
        self.path_box.setGeometry(55, 200, 391, 31)

    def _create_input_box(self):
        """Create Input Box for the word"""
        # Create the display widget
        self.input_box_word = QLineEdit(self._centralWidget)
        # Set some display's properties
        self.input_box_word.setGeometry(55, 240, 391, 31)

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
            "Search": (460, 200, 75, 31),
            "Default": (540, 200, 75, 31),
            "Start": (460, 240, 75, 31),
            "End": (550, 560, 75, 31),
            "Cancel": (10, 560, 75, 31),
            "Save": (460, 560, 75, 31),
        }
        # Create the buttons
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(self._centralWidget)
            self.buttons[btnText].setText(btnText)
            self.buttons[btnText].setGeometry(pos[0], pos[1], pos[2], pos[3])

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
        self.setDisplayText("")

    def show_file_dialog(self, home_dir):
        """Show file dialog."""
        return QFileDialog.getExistingDirectory(self, 'Open file', home_dir)


class Controller(object):

    def __init__(self, model, view_):
        self.model = model
        self._view = view_
        # Connect signals and slots
        self._connect_signals()

    def _set_default_path(self):
        pass

    def _get_default_path(self):
        pass

    def _start(self):
        """Start Crawling."""
        try:
            path = dirname(abspath(__file__)) + r"\TEST_FILES"
            word = "Data"
            self.model.crawl(path, word)
            res = self.model.get_results()
            self._view.set_display_text(res)
        except mvc_exc.NoResults as err:
            self._view.set_display_text(err)

    def _choose_filepath(self):
        """Select the search path."""
        home_dir = self.model.get_home_dir()
        try:
            search_path = self._view.show_file_dialog(home_dir)
            self._view.set_path_text(search_path)
        except mvc_exc.FileDialogError as err:
            self._view.set_display_text(err)

    def _connect_signals(self):
        """Connect signals and slots."""
        self._view.buttons["Search"].clicked.connect(self._choose_filepath)
        #self._view.buttons["Default"].clicked.connect()
        self._view.buttons["Start"].clicked.connect(self._start)
        #self._view.buttons["Cancel"].clicked.connect()
        #self._view.buttons["Save"].clicked.connect()
        self._view.buttons["End"].clicked.connect(self._view.close)

        self._view.input_box_word.returnPressed.connect(self._start)


if __name__ == "__main__":
    # Create an instance of `QApplication`
    crawler = QApplication(sys.argv)

    # Show the calculator's GUI
    view = View()
    view.show()

    c = Controller(ModelBasic(), view)

    # Execute calculator's main loop
    sys.exit(crawler.exec_())
