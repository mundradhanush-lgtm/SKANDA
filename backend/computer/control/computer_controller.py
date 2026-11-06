from backend.computer.observation.screen_capture import capture_screen
from backend.computer.observation.visual_observer import visual_observer
from backend.ai.router import computer_ai_request

def computer_control(user_input):
    instruction='''Describe the current screen clearly and accurately so another system can interact with it.
Identify the active application or website, visible text, buttons, input fields, menus, tabs, dialogs, and other relevant interface elements. Explain their approximate positions and current states where possible.
Pay attention to anything that could be important for the user's requested task. If something is unclear, unreadable, hidden, or uncertain, explicitly say so instead of guessing.
Only report what is actually visible on the screen. Do not assume that an action has been completed, and do not suggest or perform actions.
Keep the description structured, concise, and useful for deciding the next interaction.'''
    image_bytes=capture_screen()
    screenshot_text_representation=visual_observer(image_bytes, instruction)
    decision=computer_ai_request(user_input, screenshot_text_representation)
    return decision