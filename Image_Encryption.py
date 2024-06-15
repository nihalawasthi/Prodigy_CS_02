from PIL import Image

def encrypt_image(image_path, encryption_key):
    try:
        # Open the image
        img = Image.open(image_path)
        width, height = img.size

        # Encrypt the image pixels
        pixels = img.load()
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                # Apply encryption algorithm (for simplicity, let's just XOR with encryption_key)
                r ^= encryption_key
                g ^= encryption_key
                b ^= encryption_key

                pixels[x, y] = (r, g, b)

        # Return the encrypted image object
        return img
    except Exception as e:
        print("Error encrypting image:", str(e))

def decrypt_image(encrypted_image, decryption_key):
    try:
        # Create a copy of the encrypted image
        decrypted_img = encrypted_image.copy()
        width, height = decrypted_img.size

        # Decrypt the image pixels
        pixels = decrypted_img.load()
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                # Apply decryption algorithm (since XOR is its own inverse, we use the same operation)
                r ^= decryption_key
                g ^= decryption_key
                b ^= decryption_key

                pixels[x, y] = (r, g, b)

        # Return the decrypted image object
        return decrypted_img
    except Exception as e:
        print("Error decrypting image:", str(e))

def swap_pixels(image_path):
    try:
        # Open the image
        img = Image.open(image_path)
        width, height = img.size

        # Swap the image pixels
        pixels = img.load()
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = (b, r, g)  # Swapping the values of R, G, and B channels

        # Return the swapped image object
        return img
    except Exception as e:
        print("Error swapping pixels:", str(e))

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")

    while True:
        choice = input("What would you like to do?\n1. Encrypt\n2. Decrypt\n3. Swap Pixels\n4. Exit\nChoice: ")

        if choice == '1':
            encryption_key = int(input("Enter the encryption key (an integer): "))

            # Encrypt the image
            encrypted_image = encrypt_image(image_path, encryption_key)

            # Show a black image after encryption
            black_image = Image.new('RGB', encrypted_image.size, (0, 0, 0))
            black_image.show()

            decrypt_choice = input("Would you like to decrypt the image? (yes/no): ")
            if decrypt_choice.lower() == 'yes':
                decryption_key = int(input("Enter the decryption key: "))

                # Decrypt the image
                decrypted_image = decrypt_image(encrypted_image, decryption_key)
                decrypted_image.show()

                swap_choice = input("Would you like to swap pixels or exit? (swap/exit): ")
                if swap_choice.lower() == 'swap':
                    swapped_image = swap_pixels(image_path)
                    swapped_image.show()
                    break
                elif swap_choice.lower() == 'exit':
                    break
                else:
                    print("Invalid choice.")

        elif choice == '2':
            decryption_key = int(input("Enter the decryption key: "))

            # Decrypt the image
            encrypted_image = Image.open(image_path)
            decrypted_image = decrypt_image(encrypted_image, decryption_key)
            decrypted_image.show()

            swap_choice = input("Would you like to swap pixels or exit? (swap/exit): ")
            if swap_choice.lower() == 'swap':
                swapped_image = swap_pixels(image_path)
                swapped_image.show()
                break
            elif swap_choice.lower() == 'exit':
                break
            else:
                print("Invalid choice.")

        elif choice == '3':
            swapped_image = swap_pixels(image_path)
            swapped_image.show()
            break

        elif choice == '4':
            break

        else:
            print("Invalid choice.")
