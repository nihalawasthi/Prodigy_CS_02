from PIL import Image

def encrypt_image(image_path, encryption_key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                if len(pixel) == 3:
                    r, g, b = pixel
                    a = None
                elif len(pixel) == 4:
                    r, g, b, a = pixel
                else:
                    raise ValueError("Unsupported pixel format")

                r ^= encryption_key
                g ^= encryption_key
                b ^= encryption_key

                if a is None:
                    pixels[x, y] = (r, g, b)
                else:
                    pixels[x, y] = (r, g, b, a)
        return img
    except Exception as e:
        print("Error encrypting image:", str(e))
        return None

def decrypt_image(encrypted_image):
    try:
        decryption_key = int(input("Enter the decryption key: "))
        decrypted_img = encrypted_image.copy()
        width, height = decrypted_img.size
        pixels = decrypted_img.load()
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                if len(pixel) == 3:
                    r, g, b = pixel
                    a = None
                elif len(pixel) == 4:
                    r, g, b, a = pixel
                else:
                    raise ValueError("Unsupported pixel format")

                r ^= decryption_key
                g ^= decryption_key
                b ^= decryption_key

                if a is None:
                    pixels[x, y] = (r, g, b)
                else:
                    pixels[x, y] = (r, g, b, a)
        return decrypted_img
    except Exception as e:
        print("Error decrypting image:", str(e))
        return None

def swap_pixels(image_path):
    try:
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                if len(pixel) == 3:
                    r, g, b = pixel
                    pixels[x, y] = (b, r, g)
                elif len(pixel) == 4:
                    r, g, b, a = pixel
                    pixels[x, y] = (b, r, g, a)
                else:
                    raise ValueError("Unsupported pixel format")
        return img
    except Exception as e:
        print("Error swapping pixels:", str(e))
        return None

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")

    while True:
        choice = input("What would you like to do?\n1. Encrypt\n2. Decrypt\n3. Swap Pixels\n4. Exit\nChoice: ")

        if choice == '1':
            encryption_key = int(input("Enter the encryption key (an integer): "))
            encrypted_image = encrypt_image(image_path, encryption_key)
            if encrypted_image is not None:
                encrypted_image.show()
                encrypted_image.save("encrypted_image.png")

                decrypt_choice = input("Would you like to decrypt the image? (yes/no): ")
                if decrypt_choice.lower() == 'yes':
                    decrypted_image = decrypt_image(encrypted_image)
                    if decrypted_image is not None:
                        decrypted_image.show()

        elif choice == '2':
            encrypted_image = Image.open(image_path)
            decrypted_image = decrypt_image(encrypted_image)
            if decrypted_image is not None:
                decrypted_image.show()

        elif choice == '3':
            swapped_image = swap_pixels(image_path)
            if swapped_image is not None:
                swapped_image.show()

        elif choice == '4':
            break

        else:
            print("Invalid choice.")
