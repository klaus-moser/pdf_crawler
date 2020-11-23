import mvc_exceptions as mvc_exc
from os.path import basename, isfile


class Controller(object):

    def __init__(self, model, view_):
        """Init the model, view, get default path & connect siganls."""
        self.model = model
        self._view = view_
        self._get_default_path()
        # Connect signals and slots
        self._connect_signals()

    def _set_default_path(self):
        """Set the current path as default."""
        if self.model.search_path:
            self.model.set_default_path(self.model.search_path)

    def _get_default_path(self):
        """If a default path was set get it."""
        self._view.set_path_text(basename(self.model.search_path))

    def _crawl(self):
        """Start Crawling."""
        path = self.model.search_path
        word = self._view.get_word_text()

        if not path:
            warning = "No path chosen!"
            self._view.show_warning(warning)
        elif not word:
            warning = "No word chosen!"
            self._view.show_warning(warning)
        else:
            try:
                if isfile(path):
                    # Single .pdf
                    ret = self.model.crawl_file(path, word)
                    self._view.set_display_text(ret)
                else:
                    # Folder with several .pdfs
                    pdf_files = self.model.walk_folder(path)

                    if pdf_files:
                        for pdf in pdf_files:
                            ret = self.model.crawl_file(pdf, word)
                            self._view.set_display_text(ret)

            except mvc_exc.NoResults as err:
                self._view.set_display_text(err)

    def _browse(self):
        """Select the search path."""
        home_dir = self.model.get_home_dir()
        try:
            if self._view.checkbox_dir.isChecked():
                re = self._view.show_dir_dialog(home_dir)
            else:
                re = self._view.show_file_dialog(home_dir)
            if re:
                self.model.search_path = re
            self._view.set_path_text(basename(self.model.search_path))
        except mvc_exc.FileDialogError as err:
            self._view.set_display_text(err)

    def _show_info(self):
        """Show the Information Pop-Up."""
        try:
            text = self.model.get_info_text()
            self._view.show_information(text)
        except FileNotFoundError as err:
            self._view.set_display_text(err)

    def _clear_display(self):
        """Clear the result display."""
        self._view.clear_display()

    def _connect_signals(self):
        """Connect signals and slots."""
        self._view.buttons["Browse"].clicked.connect(self._browse)
        self._view.buttons["Set Default"].clicked.connect(self._set_default_path)
        self._view.buttons["Start"].clicked.connect(self._crawl)
        self._view.buttons["Clear"].clicked.connect(self._clear_display)
        # self._view.buttons["Cancel"].clicked.connect()
        self._view.buttons["Info"].clicked.connect(self._show_info)
        # self._view.buttons["Save as .txt"].clicked.connect()
        self._view.buttons["End"].clicked.connect(self._view.close)
        self._view.input_box_word.returnPressed.connect(self._crawl)
        # Checkboxes: The source object of signal is passed to the function using lambda
        self._view.checkbox_dir.stateChanged.connect(lambda: self._view.btn_state(self._view.checkbox_dir))
        self._view.checkbox_file.toggled.connect(lambda: self._view.btn_state(self._view.checkbox_file))


if __name__ == '__main__':
    print(__file__)
