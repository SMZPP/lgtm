import os
from PIL import Image, ImageDraw, ImageFont

def create_lgtm_images(input_folder="input", output_folder="output", text="L  G  T  M", font_size=130, text_color="white"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            image = Image.open(input_path)
            draw = ImageDraw.Draw(image)

            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()

            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = (image.width - text_width) / 2
            text_y = (image.height - text_height) / 2

            draw.text((text_x, text_y), text, font=font, fill=text_color)
            draw.text((text_x*0.8, text_y*1.4), " Looks  Good  To  Me !!! ", font=ImageFont.truetype("arial.ttf", 60), fill=text_color)

            image.save(output_path)
            print(f"LGTM画像を{output_path}に保存しました。")

create_lgtm_images()
