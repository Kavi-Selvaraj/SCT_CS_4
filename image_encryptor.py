from PIL import Image


def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    image.save(output_path)
    print("\nImage encrypted successfully!")


def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    image.save(output_path)
    print("\nImage decrypted successfully!")


print("=" * 40)
print("       IMAGE ENCRYPTION TOOL")
print("=" * 40)

print("\n1. Encrypt")
print("2. Decrypt")

choice = input("\nEnter your choice (1/2): ")
input_path = input("Enter image path: ")
output_path = input("Enter output image name: ")
key = int(input("Enter encryption key (0-255): "))

if choice == "1":
    encrypt_image(input_path, output_path, key)

elif choice == "2":
    decrypt_image(input_path, output_path, key)

else:
    print("\nInvalid choice.")