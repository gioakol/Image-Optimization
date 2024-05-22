import streamlit as sl
from PIL import Image
import webp

def optimize_image(image_path, output_path, quality=80):
    try:
        image = Image.open(image_path)

        # Convert to RGB if necessary
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Optimize and save to WebP format
        webp.save_image(image, output_path, quality=quality)

    except Exception as e:
        sl.error(f"Error when trying to optimize the image.: {e}")

def main():
    sl.title("Image Optimizer")

    uploaded_file = sl.file_uploader("Select image", ["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        with open("uploaded_image.jpg", "wb") as f:
            f.write(uploaded_file.read())

        try:
            # Optimize and convert to WebP
            optimize_image("uploaded_image.jpg", "optimized_image.webp")
            sl.success("Optimized image to WebP")

            # Download the optimized WebP image
            with open("optimized_image.webp", "rb") as f:
                image_data = f.read()
                sl.download_button("Download optimized image (WebP)", image_data, "optimized_image.webp")

        except Exception as e:
            sl.error(f"Image optimization error: {e}")

main()