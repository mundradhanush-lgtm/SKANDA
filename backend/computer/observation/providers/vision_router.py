from backend.computer.observation.providers.vision_zai import zai_vision_request
from backend.computer.observation.providers.vision_groq import groq_vision_request

def vision_request(image_bytes, instruction):
    try:
        vision_reply=zai_vision_request(image_bytes, instruction)
        return vision_reply
    except Exception:
        try:
            vision_reply=groq_vision_request(image_bytes, instruction)
            return vision_reply
        except Exception:
            raise RuntimeError("All vision providers failed")