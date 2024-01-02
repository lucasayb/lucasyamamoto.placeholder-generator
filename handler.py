from PIL import Image, ImageFont, ImageDraw
import base64
import io
import os

def generate_image(image_width, image_height, image_name):
    font_size = 40
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'arial_narrow.ttf')
    font = ImageFont.truetype(font_path, font_size)
    with io.BytesIO() as output:
        image = Image.new('RGB', (int(image_width),int(image_height)), (200, 200, 200))
        draw = ImageDraw.Draw(image)
        text_length = draw.textlength(image_name, font=font)
        x = (int(image_width) - int(text_length)) // 2
        y = (int(image_height) - int(font_size)) // 2
        draw.text((x, y), image_name, font=font, fill=(150, 150, 150))
        image.save(output, format="JPEG")
        return output.getvalue()

def render_image(image_bytes, status_code):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'image/jpeg'
        },
        'body': base64.b64encode(image_bytes).decode('utf-8'),
        'isBase64Encoded': True
    }

def placeholder(event, context):
    params = event.get('pathParameters', None)
    image_name = params.get('image_name', '100x100')
    
    if 'x' not in image_name:
        image_name = '100x100'
        
    image_width, image_height = image_name.split('x')
    
    image_bytes = generate_image(image_width, image_height, image_name)
        
    return render_image(image_bytes, 200)
