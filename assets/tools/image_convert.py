from PIL import Image, ImageDraw, ImageFont
import os

def resize_and_add_watermark(input_dir, output_dir, watermark_text1, watermark_text2, font_size=28):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all files in the input directory
    files = os.listdir(input_dir)

    for file in files:
        # Check if the file is an image (you may want to add more comprehensive checks)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)

            # Open the image
            original_image = Image.open(input_path)

            # Calculate the proportional height
            width_percent = (1500 / float(original_image.size[0]))
            height_size = int((float(original_image.size[1]) * float(width_percent)))

            # Resize the image
            resized_image = original_image.resize((1500, height_size), Image.Resampling.LANCZOS)

            # Add first watermark with a black shadow at the top left corner
            draw = ImageDraw.Draw(resized_image)
            font = ImageFont.truetype("NotoSansMono-Regular.ttf", font_size)
            shadow_offset = 2  # Adjust the shadow offset as needed
            draw.text((10 + shadow_offset, 10 + shadow_offset), watermark_text1, fill="black", font=font)
            draw.text((10, 10), watermark_text1, fill="white", font=font)

            # Add second watermark with a black shadow at the bottom right corner
            text_width = draw.textlength(watermark_text2, font=font)
            draw.text((resized_image.width - text_width - 10 - shadow_offset, resized_image.height - font_size - 20 - shadow_offset),
                      watermark_text2, fill="black", font=font)
            draw.text((resized_image.width - text_width - 10, resized_image.height - font_size - 20), watermark_text2, fill="white", font=font)

            # Save the result
            resized_image.save(output_path)

if __name__ == "__main__":
    input_directory = "input"
    output_directory = "output"
    watermark_text1 = "ScoloHub.com"
    watermark_text2 = "© Marcel K."
    font_size = 50

    resize_and_add_watermark(input_directory, output_directory, watermark_text1, watermark_text2, font_size)
