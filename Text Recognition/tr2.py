from PIL import Image
import pytesseract

# Path to your image file
image_path = '..\Data Science\Projects\Text Recognition\pic1.jpg'

# Open the image using Pillow
with Image.open(image_path) as img:
    # Perform OCR on the image
    recognized_text = pytesseract.image_to_string(img)

    if recognized_text:
        print("Recognized Text:")
        print(recognized_text)
    else:
        print("Failed to recognize text.")