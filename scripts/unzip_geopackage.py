# Extract all files from a zipped Geopackage file
import zipfile
import os

zip_file_path = "../data/raw/external/Geopackage.zip"
extract_to_path = "../data/raw/external/extracted_files"

# Ensure the target directory exists
os.makedirs(extract_to_path, exist_ok=True)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print(f"Files extracted to {extract_to_path}")