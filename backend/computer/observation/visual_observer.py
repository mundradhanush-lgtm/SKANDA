from backend.computer.observation.providers.vision_router import vision_request

def visual_observer(image_bytes, instruction):
    vision_response=vision_request(image_bytes, instruction)
    return vision_response