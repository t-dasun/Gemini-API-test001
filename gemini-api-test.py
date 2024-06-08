

API_KEY = 'AIzaSyBrefTNj1hEnWXBV1OM_V21KdpMhxVt9-s'

prompt = 'Provide a recipe for the baked goods in the image'

import PIL.Image
img = PIL.Image.open('baked_goods_1.jpg')
# img = PIL.Image.open('baked_goods_2.jpg')
# img = PIL.Image.open('baked_goods_3.jpg')
img

import google.generativeai as genai
from IPython.display import Markdown, clear_output, display

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name='gemini-pro-vision')
response = model.generate_content([prompt, img], stream=True)

# Extract and print the text output
text_output = ''.join([part.text for chunk in response for part in chunk.parts])
print(text_output)

# buffer = []
# for chunk in response:
#     for part in chunk.parts:
#         buffer.append(part.text)
#     clear_output()
#     display(Markdown(''.join(buffer)))