import base64
from api_keys import groq

groq_model="qwen/qwen3.8-27b"

def groq_vision_request(image_bytes, instruction):
    if not image_bytes:
        raise ValueError("Image data is empty.")
    encoded_image=base64.b64encode(image_bytes).decode("utf-8")
    image_data_url=f"data:image/png;base64,{encoded_image}"
    response=groq.chat.completions.create(
        model=groq_model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": instruction
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_data_url
                        }
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content