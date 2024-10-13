import os
from urllib.request import urlretrieve
output_relative_dir = f'D:\STUDYfile\\ads2\\111ads\project-2-group-real-estate-industry-project-35\data\\raw\external'
URL_TEMPLATE = 'https://www.education.vic.gov.au/Documents/about/research/datavic/dv346-schoollocations2023.csv'
url = f'{URL_TEMPLATE}'
output_dir = f"{output_relative_dir}"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'VIC_School_Location.csv')
urlretrieve(url, output_file)
print(f"File has been saved to: {output_file}")