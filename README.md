# Task 4 – Image Encryption Using Pixel Manipulation

## Objective

To create a basic image encryption and decryption tool using pixel manipulation.

## Description

The program modifies the RGB values of each pixel using a numerical encryption key.

During encryption, the key is added to each RGB value.

During decryption, the same key is subtracted to restore the original pixel values.

## Features

* Encrypts images using pixel manipulation.
* Decrypts encrypted images.
* Accepts a user-defined encryption key.
* Supports common image formats such as JPG and PNG.

## Technologies Used

* Python
* Pillow (PIL)

## How to Run

First install Pillow:

```bash
pip install pillow
```

Then run:

```bash
python image_encryptor.py
```

## Example

**Encryption:**

```text
Choice: 1
Input: test.jpg
Output: encrypted.png
Key: 80
```

**Decryption:**

```text
Choice: 2
Input: encrypted.png
Output: decrypted.png
Key: 80
```

## Conclusion

The project demonstrates a basic educational approach to image encryption by manipulating RGB pixel values using mathematical operations.
cd