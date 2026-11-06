import base64
import requests
from api_keys import zai

zai_api_url="https://api.z.ai/api/paas/v4/chat/completions"
zai_model="glm-5.3-flashx"

def zai_vision_request(image_bytes, instruction):
    if not image_bytes:
        raise ValueError("Image data is empty.")
    encoded_image=base64.b64encode(image_bytes).decode("utf-8")
    image_data_url=f"data:image/png;base64,{encoded_image}"
    headers={
        "Authorization": f"Bearer {zai}",
        "Content-Type": "application/json"
    }
    payload={
        "model": zai_model,
        "messages": [
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
        ],
        "stream": False
    }
    response=requests.post(
        zai_api_url,
        headers=headers,
        json=payload,
        timeout=60
    )
    response.raise_for_status()
    response_data=response.json()
    try:
        return response_data["choices"][0]["message"]["content"]

    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError(
            "Unexpected response received from Z.ai."
        ) from error
