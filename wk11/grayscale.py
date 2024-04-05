from PIL import Image

# Open the color image to process
input_image = Image.open("www/images/babson.jpg")

# Get the width and height of the image
width, height = input_image.size

# Create a new blank image with the same size as the original image, in grayscale mode
output_image = Image.new("RGB", (width, height))

# Loop through each pixel
for y in range(height):
    for x in range(width):
        # Get the pixel value from the original image
        pixel = input_image.getpixel((x, y))
        # print(pixel)

        # Calculate the average of the RGB channel values
        gray_value = sum(pixel) // 3

        # Set the average value in the new image
        output_image.putpixel((x, y), (gray_value, gray_value, gray_value))

# Save the grayscale image
output_image.save("wk11/gray_output.jpg")
