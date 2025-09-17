"""
Cyle Roberts CS 485 Program 1
Encryption

Purpose:
This program was written to compare ECB and CBC encryption using jpg and bmp files.
To run this program, call the program from the command line on a machine with
Python3 installed, the Pillow library installed, and the Cryptodome library installed.
This program takes 4 command line arguments with the -i, -o, -k, and -m flags
specifying "input" file (path), "output" file (path), key, and "AES_ECB" or "AES_CBC" specifying the mode.

INPUT FILE SPECS:
If an input file is specified without a file extension, the program will check
the current directory or a specified prepended directory for the file name with
an appended jpg extension, then a bmp file extension after.

KEY SPECS:
This program requires a 16-character key to be specified.

Example call:
python3 /home/cyle/Desktop/CS485pgm1.py -i pic_original -o out -k 0011223344556677 -m AES_ECB

In this example, the key was of size 16 characters, the file extension was
unspecified so it searched for pic_original first, then "pic_original.jpg", then "pic_original.bmp".
I used a hard-coded IV from the example command line arguments in the assignment
description for the CBC encryption.
This program was tested on a Ubuntu 22.04.5 LTS machine running Python 3.10.12 with
Pillow Version: 9.0.1 and pycryptodome 3.20.0.
"""

import argparse
from PIL import Image
from Crypto.Cipher import AES


def padInput(input_bytes):
    pad_len = 16 - (len(input_bytes) % 16)
    pad = bytes([pad_len] * pad_len)
    return input_bytes + pad


def convertInputByte(input_file):
    try:
        with open(input_file, "rb") as file:
            img = Image.open(file)
            metadata = img.info
            input_bytes = img.tobytes()
            print(f"{input_file} found")
            return img, input_bytes, metadata
    except FileNotFoundError:
        print(f"File not found. Trying {input_file}.jpg")
        try:
            with open(input_file + ".jpg", "rb") as file:
                img = Image.open(file)
                metadata = img.info
                input_bytes = img.tobytes()
                print(f"{input_file}.jpg found")
                return img, input_bytes, metadata
        except FileNotFoundError:
            print(f"File not found. Trying {input_file}.bmp")
            try:
                with open(input_file + ".bmp", "rb") as file:
                    img = Image.open(file)
                    metadata = img.info
                    input_bytes = img.tobytes()
                    print(f"{input_file}.bmp found")
                    return img, input_bytes, metadata
            except FileNotFoundError:
                print("File not found. Exiting...")
                exit(0)


def encryptECB(plaintext, key):
    key_bytes = key.encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def encryptCBC(plaintext, key):
    key_bytes = key.encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=b'0102030405060708')
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def createEncryptedImg(image, encrypted_data, output_file, metadata):
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)
    encrypted_image.save(output_file, format=image.format, **metadata)


modes = ['AES_ECB', 'AES_CBC']

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, required=True, help="Input filename")
parser.add_argument('-o', '--output', type=str, required=True, help="Output filename")
parser.add_argument('-k', '--key', type=str, required=True, help="Encryption key")
parser.add_argument('-m', '--mode', type=str, required=True, choices=modes,
                    help="Encryption mode (AES_ECB or AES_CBC)")

args = parser.parse_args()

input_file = args.input
output_file = args.output
encryption_key = args.key
encryption_mode = args.mode

image, input_bytes, metadata = convertInputByte(input_file)
input_bytes_padded = padInput(input_bytes)

if encryption_mode == 'AES_ECB':
    encrypted_data = encryptECB(input_bytes_padded, encryption_key)
else:
    encrypted_data = encryptCBC(input_bytes_padded, encryption_key)

createEncryptedImg(image, encrypted_data, output_file, metadata)