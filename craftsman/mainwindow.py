from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

from qtpy import QtGui
import resources_rc

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        self.UiComponents()


    # add any custom methods here
    def UiComponents(self):
		#self.playButton.setIcon(QtGui.QIcon('play.svg'))
		pass
