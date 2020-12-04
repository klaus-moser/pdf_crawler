#!/usr/bin/env python3

# Filename: controller.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This is the controller."""

import mvc_exceptions as mvc_exc
from os.path import basename, isfile


class Controller(object):
    """Controller to control the model, view & backend."""

    def __init__(self, model, view_):
        """Init the model, view, get default path & connect signals."""
        self.model = model
        self._view = view_
        self._get_default_path()
        # Connect signals and slots
        self._connect_signals()

    def _set_default_path(self):
        """Set the current path as default."""
        self._view.hide_progressbar()
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
                    # Several .pdfs
                    ret = self.model.crawl_files(path, word)
                    self._view.set_display_text(ret)

            except mvc_exc.ErrorCrawlingFile:
                raise mvc_exc.ErrorCrawlingFile(self._view.set_display_text("Error crawling file"))
            finally:
                pass

    def _browse(self):
        """Select the search path."""
        self._view.hide_progressbar()
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
        self._view.hide_progressbar()
        try:
            text = self.model.get_info_text()
            self._view.show_information(text)
        except FileNotFoundError as err:
            self._view.set_display_text(err)

    def _clear_display(self):
        """Clear the result display."""
        self._view.hide_progressbar()
        self._view.clear_display()

    def _toggle_checkbox(self):
        """Connect to View when checkbox is toggled & clear current path."""
        self._view.hide_progressbar()
        self._view.btn_state(self._view.checkbox_file)
        self.model.search_path = ""

    def _state_changed_checkbox(self):
        """Connect to View when checkbox-state is changed & clear current path."""
        self._view.hide_progressbar()
        self._view.btn_state(self._view.checkbox_dir)
        self.model.search_path = ""

    def _save_results(self):
        """Save results to .txt file."""
        self._view.hide_progressbar()
        text = self._view.display_text()
        path = self._view.get_path_to_save(self.model.get_home_dir())
        self.model.save_results(path, text)

    def _connect_signals(self):
        """Connect signals and slots."""
        self._view.buttons["Browse"].clicked.connect(self._browse)
        self._view.buttons["Set Default"].clicked.connect(self._set_default_path)
        self._view.buttons["Start"].clicked.connect(self._crawl)
        self._view.buttons["Clear"].clicked.connect(self._clear_display)
        # self._view.buttons["Cancel"].clicked.connect()
        self._view.buttons["Info"].clicked.connect(self._show_info)
        self._view.buttons["Save as .txt"].clicked.connect(self._save_results)
        self._view.buttons["End"].clicked.connect(self._view.close)
        self._view.input_box_word.returnPressed.connect(self._crawl)
        # Checkboxes: The source object of signal is passed to the function using lambda
        self._view.checkbox_dir.stateChanged.connect(self._state_changed_checkbox)
        self._view.checkbox_file.toggled.connect(self._toggle_checkbox)


if __name__ == '__main__':
    print(__file__)
