from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = np.array(img)

    # Encrypt by adding the key and clipping values to stay within 0-255
    encrypted_pixels = np.clip(pixels + key, 0, 255).astype(np.uint8)
    encrypted_image = Image.fromarray(encrypted_pixels)

    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as: {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = np.array(img)

    # Decrypt by subtracting the key and clipping values to stay within 0-255
    decrypted_pixels = np.clip(pixels - key, 0, 255).astype(np.uint8)
    decrypted_image = Image.fromarray(decrypted_pixels)

    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as: {output_path}")

def main():
    print("Simple Image Encryption Tool")
    action = input("Would you like to (E)ncrypt or (D)ecrypt an image? ").strip().upper()

    image_path = input("Enter the path of the image: ")
    output_path = input("Enter the output path for the processed image: ")
    key = int(input("Enter a key (integer value for pixel manipulation): "))

    if action == 'E':
        encrypt_image(image_path, output_path, key)
    elif action == 'D':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice. Please select 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()