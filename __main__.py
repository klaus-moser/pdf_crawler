# __main__.py

import sys
from model_view_controller import *

__version__ = "0.1"
__author__ = "Klaus Moser"

# Create an instance of 'QApplication'
crawler = QApplication(sys.argv)

# Show the calculator's GUI
view = View()
view.show()

# Create the controller incl. Model & GUI
c = Controller(Model(), view)

# Execute calculator's main loop
sys.exit(crawler.exec_())
