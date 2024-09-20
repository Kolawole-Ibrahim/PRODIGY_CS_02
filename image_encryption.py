from PIL import Image
import numpy as np

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, save_path):
    image.save(save_path)

def encrypt_image(image):
    pixels = np.array(image)
    encrypted_pixels = pixels + 50  # Basic operation: add 50 to each pixel value
    encrypted_pixels = np.clip(encrypted_pixels, 0, 255)  # Ensure values are within valid range
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    return encrypted_image

def decrypt_image(image):
    pixels = np.array(image)
    decrypted_pixels = pixels - 50  # Reverse operation: subtract 50 from each pixel value
    decrypted_pixels = np.clip(decrypted_pixels, 0, 255)  # Ensure values are within valid range
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    return decrypted_image

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt an image")
    parser.add_argument("operation", choices=["encrypt", "decrypt"], help="Operation to perform")
    parser.add_argument("input_image", help="Path to the input image")
    parser.add_argument("output_image", help="Path to save the output image")
    args = parser.parse_args()

    image = load_image(args.input_image)
    
    if args.operation == "encrypt":
        processed_image = encrypt_image(image)
    elif args.operation == "decrypt":
        processed_image = decrypt_image(image)
    
    save_image(processed_image, args.output_image)
    print(f"Image has been {args.operation}ed and saved to {args.output_image}")

if __name__ == "__main__":
    main()
