from fbs_runtime.application_context.PyQt5 import ApplicationContext
from Constant import *

# "QMainWindow { background-color:" + APP_BG_COLOR + "}" + \

CSS_TAB_BAR = "QTabBar::tab { height: 25px; background:" + SECONDARY_COLOR + "; border-bottom-color: #C2C7CB }" + \
              "QTabWidget::tab-bar { left: 5px } " + \
              "QTabBar::tab { " + \
              "border: 1px solid " + SECONDARY_COLOR + " ;" + \
              "border-top-left-radius: 4px;" + \
              "border-top-right-radius: 4px;" + \
              "min-width: 8ex;" + \
              "padding: 2px" + \
              "}"

CSS_TAB_CLOSE = "QTabBar::close-button { image: url(clear-24px.svg); subcontrol-position: right }" + \
                "QTabBar::close-button:hover { background: #e0e0e0 }"

CSS_TAB = "QTabWidget::pane { border-top: 2px solid " + SECONDARY_COLOR + " }" + \
          "QTabBar::tab:selected { border-color: " + BASE_COLOR + "; border-bottom-color:" + SECONDARY_COLOR + \
          "; background:" + SECONDARY_COLOR + " }" + \
          "QTabBar::tab:!selected { border-color:#F5F5F5; border-bottom-color:" + SECONDARY_COLOR + \
          "; background:#F5F5F5 }" + \
          "QTabBar::tab:selected { margin-left: -4px; margin-right: -4px }" + \
          "QTabBar::tab { height: 30px; background:" + SECONDARY_COLOR + "; " + \
          "border-bottom-color: " + SECONDARY_COLOR + "; " + \
          "border-top: 2px solid " + SECONDARY_COLOR + " ;" + \
          "min-width: 30ex;" + \
          "padding: 2px" + \
          "}" + CSS_TAB_CLOSE

CSS_TAB_BASE = "QWidget { background-color:" + SECONDARY_COLOR + "}"

# Updated by Pinkesh Shah on 05-May-20
# Start Region
env = "TEST"

if env == "DEV":
    CSS_BASE = "QPlainTextEdit { border-style: solid; border-width:1px; border-color: grey;" + \
               "background-color: " + COLOR_WHITE + ";" "color: " + COLOR_DARK_GREY + "}" + \
               "QDockWidget { border-style: solid; border-width:1px; border-color: grey}" + \
               "QGroupBox { border-style: solid }" + \
               "QScrollArea { background-color:" + SECONDARY_COLOR + "}"

    CSS_FRAME = "QFrame {background-color: " + COLOR_BG + ";" + \
                "border-radius: 5px; " \
                "max-width: 250px; }"

    '''         Commented by Pinkesh Shah on 28-Apr-20
                # Start Region
                # max-height: 100px;
                # margin-top: 0px }"
                # End Region'''

    CSS_FRAME_LABEL = "QLabel { color: " + COLOR_BLACK + ";" + \
                      "font-size: 13px; " \
                      "font-weight : bold }"

    CSS_FRAME_MIKROTIK_LABEL = "QLabel { color: " + COLOR_DARK_GREY + ";" + \
                               "font-weight: bold; " \
                               "padding-left: 20px; " \
                               "font-size: 11px }"

    CSS_FRAME_GROUP_BOX = "QGroupBox { background-color: " + COLOR_WHITE + ";" + \
                          "padding-top: 0px }"

elif env == "TEST":
    CSS_BASE = "QPlainTextEdit { border-style: solid; border-width:1px; border-color: grey;" + \
               "background-color: " + COLOR_WHITE + ";" "color: " + COLOR_DARK_GREY + "}" + \
               "QDockWidget { border-style: solid; border-width:1px; border-color: grey}" + \
               "QGroupBox { border-style: solid }" + \
               "QScrollArea { background-color:" + COLOR_GREEN + ";" + \
               "color: " + COLOR_YELLOW + "}"

    CSS_FRAME = "QFrame { color: grey; border-radius: 5px; border-style: outset; border-width:1px; border-color: grey }" + \
                "QFrame:hover { background-color: " + HOVER_BG + " } "


    CSS_FRAME_LABEL = "QLabel { font-size: 11px; color: grey; border-width:0px } "

    CSS_FRAME_MIKROTIK_LABEL = "QLabel { font-weight: bold; " \
                               "font-size: 14px; " \
                               " border-width:0px }"

    CSS_FRAME_GROUP_BOX = "QGroupBox { background-color: white;" + \
                          "padding-top: 0px }"

# End Region

CSS_SCROLLBAR = "QScrollBar:vertical { width: 10px; background: " + SCROLL_BG + " ; border-radius: 4px}" + \
                "QScrollBar::handle:vertical {background-color: " + SCROLL_HANDLE_BG + " } "




def is_env_dev():
    if ENVIRONMENT == "DEV":
        return True
    return False
