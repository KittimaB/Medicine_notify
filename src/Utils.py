import pyautogui

def Scale_Width_Height():
    scale = 2
    size_screen = pyautogui.size()
    width = ((size_screen.width / scale) / 683)
    height = ((size_screen.height / scale) / 400)
    return width, height

def show_widget_fullscreen(widget):
    # widget.showFullScreen()
    widget.showNormal()