# Automated Pattern Generator for Print-on-Demand

## Project Description

This is a personal project to automate the creation of pattern files of a particular size. It is specifically used to generate pattern files for a print-on-demand website, Threadless. The project allows you to upload an image, and the design is printed on various products. Most products work with the same file upload, but some products require specific file sizes. Manually preparing these files is time-consuming and repetitive, especially when dealing with patterns that simply need to be repeated for different file sizes. This project aims to automate that process.

Currently, the patterns generated are for file sizes that I usually work with. Most of these are around 4000 x 4000 px or larger to retain image quality. I haven't yet explored smaller sizes, as I first need to determine how the patterns will look at those dimensions.

The project was built using the Python image manipulation library Pillow. Images are read and processed, and the output images are saved to a designated folder using Python libraries.

## Features

- Generates repeating patterns for various file sizes
- Automatically resizes images while maintaining the aspect ratio
- Moves the original image to the output folder for better organization

## Technologies Used

- Python
- Pillow (Python Imaging Library)
- `shutil` for file operations
- `os` for managing file paths

## Setup and Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the pattern generator:
    ```bash
    python pattern_generator.py

## Usage
1. Place the images you want to process in the input folder.

2. Run the script using:
    ```bash
    python pattern_generator.py

3. The processed images and patterns will be saved in the `output_patterns/` folder, organized by image name.

## Project Structure
    ```bash
    pattern_generator/
    │
    ├── input/                   # Folder where you place your input images
    ├── output/                  # Folder where the generated patterns will be saved
    ├── get_filenames.py         # Script to fetch image filenames
    ├── pattern_generator.py     # Main script for generating patterns
    ├── requirements.txt         # Dependencies for the project
    └── README.md                # Project documentation (this file)

