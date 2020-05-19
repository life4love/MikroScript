from fbs_runtime.application_context.PyQt5 import ApplicationContext
from MainWindow import MainWindowGui

import sys

from Logs import LogRecord

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindowGui()

    # Updated by Pinkesh Shah on 09-May-20 to show window maximized
    # Start Region
    # window.show()
    window.showMaximized()
    # End Region

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)

