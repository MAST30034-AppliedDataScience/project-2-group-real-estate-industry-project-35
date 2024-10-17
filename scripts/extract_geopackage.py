import os
from urllib.request import urlretrieve

# Use raw string for the file path to avoid issues with backslashes
output_relative_dir = "../data/raw/external"
URL_TEMPLATE = 'https://www.abs.gov.au/census/find-census-data/geopackages/download/Geopackage_2021_G01_VIC_GDA2020.zip'
url = f'{URL_TEMPLATE}'

# Ensure the output directory exists
os.makedirs(output_relative_dir, exist_ok=True)

# Set the path for the downloaded file
output_file = os.path.join(output_relative_dir, 'Geopackage.zip')

# Download the file
urlretrieve(url, output_file)
print(f"File has been saved to: {output_file}")
