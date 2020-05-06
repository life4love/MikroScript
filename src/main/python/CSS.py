from fbs_runtime.application_context.PyQt5 import ApplicationContext

ENVIRONMENT = "DEV"
BACKGROUND_COLOR = "#FBFBFB"
# APP_BG_COLOR = "#F1F1F1"
# APP_BG_COLOR = "#efebe9"
APP_BG_COLOR = "#D7D7D7"
SECONDARY_COLOR = "#f9f9f9"
THIRD_COLOR = "#F1F1F1"
BASE_COLOR = "#ff6b09"

COLOR_WHITE = "#FFFFFF"
COLOR_PALE_WHITE = "#DB7093"
COLOR_LIGHT_GREY = "#F1F1F1"
COLOR_MEDIUM_GREY = "#E4E4E4"
COLOR_DARK_GREY = "#A9A9A9"
COLOR_RED = "#FF0000"
COLOR_BLUE = "#0000FF"
COLOR_BLACK = "#000000"
COLOR_GREEN = "#008000"
COLOR_YELLOW = "#FFFF00"

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
env = "DEV"

if env == "DEV":
    CSS_BASE = "QPlainTextEdit { border-style: solid; border-width:1px; border-color: grey;" + \
               "background-color: " + COLOR_WHITE + ";" "color: " + COLOR_DARK_GREY + "}" + \
               "QDockWidget { border-style: solid; border-width:1px; border-color: grey}" + \
               "QGroupBox { border-style: solid }" + \
               "QScrollArea { background-color:" + SECONDARY_COLOR + "}"

    CSS_FRAME = "QFrame {background-color: " + COLOR_MEDIUM_GREY + ";" + \
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

    CSS_FRAME = "QFrame { background-color: " + COLOR_BLUE + ";" + \
                "border-radius: 5px; " \
                "max-width: 250px; }"

    CSS_FRAME_LABEL = "QLabel { background-color: " + COLOR_RED + ";" + \
                      "color: " + COLOR_BLACK + ";" + \
                      "font-size: 13px; " \
                      "font-weight : bold }"

    CSS_FRAME_MIKROTIK_LABEL = "QLabel { color: " + COLOR_DARK_GREY + ";" + \
                               "background-color: " + COLOR_RED + ";" + \
                               "font-weight: bold; " \
                               "padding-left: 20px; " \
                               "font-size: 11px }"

    CSS_FRAME_GROUP_BOX = "QGroupBox { background-color: " + COLOR_PALE_WHITE + ";" + \
                          "padding-top: 0px }"

# End Region


def is_env_dev():
    if ENVIRONMENT == "DEV":
        return True
    return False
