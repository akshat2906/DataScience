from PIL import Image
import pytesseract

def perform_ocr(image_path):
    try:
        # Open the image using Pillow
        with Image.open(image_path) as img:
            # Perform OCR on the image
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def readtext():
    # Replace 'image_path' with the path to your image file
    #image_path="C:\Users\HP\OneDrive\Desktop\Data Science\Python\Text Recognition\1.jpg"
    image_path ='pic1.jpg'

    # Perform OCR on the image
    recognized_text = perform_ocr(image_path)

    if recognized_text:
        print("Recognized Text:")
        print(recognized_text)
    else:
        print("Failed to recognize text.")

if __name__ == "__main__":
    readtext()