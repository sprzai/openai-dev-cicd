import openai

openai.api_key = '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'


response = openai.Image.create(
    prompt="un pulpo con alas de dragon y se encuentra en un planeta de otra galaxia",
    size="512x512",
    response_format="url"
)


import requests
from PIL import Image
from io import BytesIO


image_url = response["data"][0]["url"]
image_content = requests.get(image_url).content
image = Image.open(BytesIO(image_content))
image.show()
