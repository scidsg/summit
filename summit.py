import os
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from collections import Counter, defaultdict


def preprocess_image(image):
    # Convert to grayscale
    gray_image = image.convert("L")
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(gray_image)
    contrast_image = enhancer.enhance(1.3)  # Adjust the contrast factor as needed
    # Binarize the image: a threshold value of 128 is used here, adjust as needed
    binarized_image = contrast_image.point(lambda x: 0 if x < 128 else 255, "1")
    # Apply a filter to denoise
    processed_image = binarized_image.filter(
        ImageFilter.MedianFilter(size=3)
    )  # The size of the filter can be adjusted
    return processed_image


# Configuration for Tesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
custom_oem_psm_config = "--oem 1"

# Directory setup
base_path = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(base_path, "images")
text_folder = os.path.join(base_path, "text")

if not os.path.exists(text_folder):
    os.makedirs(text_folder)

# Initialize data structures
word_to_files = defaultdict(set)
file_word_summary = {}

# Process each file
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(folder_path, filename)
        try:
            img = Image.open(img_path)
            processed_img = preprocess_image(img)
            text = pytesseract.image_to_string(processed_img, config="--oem 1")
            words = text.lower().split()
            counter = Counter(words)
            file_word_summary[filename] = counter

            # Record each word's occurrence in the current file
            for word in words:
                word_to_files[word].add(filename)

            # Save the OCR result to a text file
            output_file = os.path.join(text_folder, filename + ".txt")
            with open(output_file, "w") as file:
                file.write(text)
            print(f"✅ Text from {filename} has been saved to {output_file}")

        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")
            continue

# Total word summary across all files
total_word_summary = Counter()
for counter in file_word_summary.values():
    total_word_summary += counter

# Write the summary file
summary_file_path = os.path.join(text_folder, "📝 Summary.txt")
with open(summary_file_path, "w") as summary_file:
    # Global top 10 words
    summary_file.write("Top 10 words across all files:\n")
    for word, count in sorted(total_word_summary.items(), key=lambda x: (-x[1], x[0]))[:10]:
        summary_file.write(f"{word}: {count}\n")
        summary_file.write("  Files: " + ", ".join(sorted(word_to_files[word])) + "\n")
    summary_file.write("\n")

    # Per-file word summary
    for file, counter in file_word_summary.items():
        summary_file.write(f"Summary for {file}:\n")
        for word, count in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
            summary_file.write(f"{word}: {count}\n")
        summary_file.write("\n")

print(f"👍 Summary written to {summary_file_path}.")
