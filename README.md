# MAST30034 Project 2 README.md
Name: `Lijialan Wang`
Student ID: `1195112`

Name: `Jiani Ji`
Student ID: `1266536`

Name: `Lingyi Feng`
Student ID: `1086464`

Name: `Yanbin Hong`
Student ID: `1266168`

**Research Goal:** Predicting rental prices and growth trends for residential properties in Victoria and identifying the most livable and affordable areas with internal and external features.

**Timeline:** WEEK 6 - WEEK 10, and WEEK 11 & 12 for presentation.

**Data:** Data files are stored in the `data` folder in `.csv`, `.xlsx`, `.gpkg` and `.XML` formats.

Internal data: 
paths, Parking, beds from *www.domain.com.au*. 

External data: 
- People's Income
- Number of Schools
- Amenities (APIs distance): CBD, Gyms, Libraries, Markets, Schools, Police Stations, Train Stations.
- Neighborhood Safety
- Number of immigrants
- Population

To run the pipeline, please visit the files below:
1. `scripts`: This file contains all the internal and external data that needs to be downloaded. Firstliy, running `create_data_files.ipynb`, `extract_geopackage.py` and `unzip_geopackage.py` then download other features.
2. `notebooks`: This file contains data analysis, visualization, features engineering, and modeling to predict the top ten suburbs with the fastest price growth and identify the best livable and affordable suburbs. Jupyter Notebook Order: `data_preprocessing`, `SA2`, `SA2_map`,`convert_address`1-4, all APIs distance 1-4, `postcode_schools.ipynb`, `Price_2021_2023.ipynb`, `property_merge`1-4, `final_data.ipynb`, `age.ipynb`.
3. `models`: Order: `xgboost.ipynb`, `rf.ipynb`, `svr.ipynb`, `arima_with_xg_gowth_rate.ipynb`, `liveability.ipynb`
4. `plots`: All plots and predicted maps are stored in this file.