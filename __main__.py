#!/usr/bin/env python3

# Filename: __main__.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""PDFCrawler is a simple search application built using Python and PyQt5."""

import sys

from model import *
from view import *
from controller import *

__version__ = "1.0"
__author__ = "Klaus Moser"

# Create an instance of 'QApplication'
crawler = QApplication(sys.argv)

# Show the calculator's GUI
view = View()
view.show()

# Create the controller incl. Model & GUI
c = Controller(Model(view), view)

# Execute calculator's main loop
sys.exit(crawler.exec_())
