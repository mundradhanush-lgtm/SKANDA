import pyautogui
from io import BytesIO

def capture_screen():
    screenshot=pyautogui.screenshot()
    image_buffer=BytesIO()
    screenshot.save(image_buffer, "PNG")
    image_bytes=image_buffer.getvalue()
    return image_bytes