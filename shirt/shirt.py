import sys
from PIL import Image, ImageOps

def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]


    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not (input_path.lower().endswith(valid_extensions) and output_path.lower().endswith(valid_extensions)):
        sys.exit("Error: Input and output files must have .jpg, .jpeg, or .png extensions")

    if input_path.split('.')[-1].lower() != output_path.split('.')[-1].lower():
        sys.exit("Error: Input and output files must have the same extension")


    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit(f"Error: The file '{input_path}' does not exist")

    shirt_image = Image.open("shirt.png")


    input_image_resized = ImageOps.fit(input_image, shirt_image.size)

    input_image_resized.paste(shirt_image, (0, 0), shirt_image)


    input_image_resized.save(output_path)

if __name__ == "__main__":
    main()
