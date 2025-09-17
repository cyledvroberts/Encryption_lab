# CS 485 Lab 1: Encryption and AES Modes

## Overview
This repository contains all materials and code for **CS 485 Lab 1**, which explores encryption using different ciphers, modes, and padding techniques. The lab consists of two main tasks:

1. **Task 1: Encryption Using Different Ciphers and Modes**
   - Experiment with various encryption algorithms (AES, Blowfish, etc.) and modes (ECB, CBC, CFB, OFB) using OpenSSL.
   - Analyze the effect of single-bit changes on encrypted data to understand the properties of each mode.
   - A PDF lab report is included with answers, analysis, and screenshots.

2. **Task 2: Image Encryption with AES**
   - Develop a Python script to encrypt images in **AES ECB** and **AES CBC** modes.
   - Encrypt only image pixel data, preserving metadata to allow viewing of encrypted images.
   - Script uses **Pillow** for image manipulation and **PyCryptodome** for encryption.

## Requirements
- Python 3.x (tested on 3.12.1)
- Libraries (specified in `requirements.txt`):
  - `pillow==10.4.0`
  - `pycryptodome==3.20.0`
- Linux VM or Windows with VSCode and OpenSSL installed
- Sample image files provided: `Tux.jpg`, `whoisCB2.jpg`, `pic_original.bmp`
- OpenSSL (for Task 1 encryption experiments):
  - Linux: `/usr/bin/openssl`
  - Windows: `C:\Program Files\Git\usr\bin\openssl.exe`

## File Structure
CS485_Lab1/
├── Task1_LabReport.pdf # Answers, analysis, screenshots for Task 1
├── Task2_ImageEncrypt.py # Python script for Task 2
├── requirements.txt # Python dependencies
├── images/ # Sample image files for Task 2
└── README.md # This file

shell
Copy code

## Usage

### Task 2 Script
```bash
python Task2_ImageEncrypt.py -i <input_image> -o <output_image> -k <16-char_key> -m <AES_ECB|AES_CBC>
Example:

bash
Copy code
python Task2_ImageEncrypt.py -i images/pic_original.bmp -o images/out.bmp -k 0011223344556677 -m AES_ECB
The script will read the image, pad the bytes, encrypt them, and save the encrypted image.

Only pixel data is encrypted; metadata is preserved to allow viewing of the encrypted image.

Notes
AES key must be 16 characters for 128-bit encryption.

ECB mode reveals patterns in images, while CBC mode masks them.

