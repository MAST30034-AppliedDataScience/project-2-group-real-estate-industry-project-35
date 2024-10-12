import requests
import pandas as pd
import os
import time

# Define headers for the HTTP request to mimic a real browser visit
headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"2ed05-1YqybhYeX3f3I5gJYWooeQ/9SH8"',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

# Fetch property rental data for a given price range and page, with a retry mechanism for handling errors
def fetch_data(price_min, price_max, page, retries=3):
    # Define the URL and query parameters
    url = f'https://www.domain.com.au/rent/'
    params = {
        'price': f'{price_min}-{price_max}',
        'state': 'vic',
        'page': page
    }

    # Try fetching data up to a certain number of retries in case of errors
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()  # Ensure the request succeeded

            # Parse the JSON response
            json_data = response.json()
            total_pages = json_data['props']['totalPages']
            listings = json_data['props']['listingsMap']

            data = []
            # Iterate through the listings and extract relevant information
            for i, item in listings.items():
                agent_name = item['listingModel']['branding'].get('agentName', 'N/A')
                price = item['listingModel'].get('price', 'N/A')
                address = (
                    item['listingModel']['address'].get('street', '') + " " +
                    item['listingModel']['address'].get('suburb', '') + " " +
                    item['listingModel']['address'].get('state', '') + " " +
                    item['listingModel']['address'].get('postcode', '')
                )
                beds = item['listingModel']['features'].get('beds', 0)
                baths = item['listingModel']['features'].get('baths', 0)
                parking = item['listingModel']['features'].get('parking', 0)
                data.append([agent_name, price, address, beds, baths, parking])
            
            return data, total_pages

        except (requests.RequestException, KeyError) as e:
            # Handle errors and retries
            print(f"Attempt {attempt + 1} failed for price range {price_min}-{price_max}, page {page}: {e}")
            if attempt < retries - 1:
                time.sleep(2)
            else:
                print(f"Failed to fetch data after {retries} attempts.")
                return [], 0

# Check if data for a specific price range has already been saved
def check_existing_data(price_min, price_max):
    filename = r'D:\STUDYfile\ads2\111ads\project-2-group-real-estate-industry-project-35\data\raw\property\combined_rent_data.xlsx'
    price_qujian = f'{price_min}-{price_max}'

    if os.path.exists(filename):
        existing_data = pd.read_excel(filename)
        if price_qujian in existing_data['price_qujian'].values:
            return True
    return False

# Save data to an Excel file at the specified location
def save_to_excel(data, price_min, price_max):
    filename = r'D:\STUDYfile\ads2\111ads\project-2-group-real-estate-industry-project-35\data\raw\property\combined_rent_data.xlsx'

    price_qujian = f'{price_min}-{price_max}'
    for row in data:
        row.append(price_qujian)

    # If the file exists, load it, otherwise create a new DataFrame
    if os.path.exists(filename):
        existing_data = pd.read_excel(filename)
    else:
        existing_data = pd.DataFrame(columns=['agentName', 'price', 'address', 'beds', 'baths', 'parking', 'price_qujian'])

    # Create a new DataFrame for the fetched data and combine it with existing data
    new_data_df = pd.DataFrame(data, columns=['agentName', 'price', 'address', 'beds', 'baths', 'parking', 'price_qujian'])

    combined_data = pd.concat([existing_data, new_data_df]).drop_duplicates()

    # Save the combined data back to the Excel file
    combined_data.to_excel(filename, index=False)
    print(f"Data for price range {price_min}-{price_max} saved to {filename}")

# Main function to iterate through price ranges and fetch/save data
def main():
    price_min = 0
    price_max = 6000
    price_step = 50

    # Loop through price ranges and process the data
    for price in range(price_min, price_max, price_step):
        current_price_min = price
        current_price_max = price + price_step

        # Skip fetching if the data for the price range already exists
        if check_existing_data(current_price_min, current_price_max):
            print(f"Data for price range {current_price_min}-{current_price_max} already exists, skipping...")
            continue

        # Fetch data for the current price range
        page = 1
        data, total_pages = fetch_data(current_price_min, current_price_max, page)
        print(f"Price Range {current_price_min}-{current_price_max}, Total Pages: {total_pages}")

        # Limit the number of pages fetched to 50 to avoid overloading the server
        max_pages = min(total_pages, 50)
        if total_pages > 50:
            print(f"Price Range {current_price_min}-{current_price_max} has more than 50 pages, only fetching first 50 pages.")

        all_data = []

        # Fetch data page by page until reaching the maximum page count
        while page <= max_pages:
            data, _ = fetch_data(current_price_min, current_price_max, page)
            all_data.extend(data)
            page += 1

        # Save the fetched data to the Excel file
        save_to_excel(all_data, current_price_min, current_price_max)

# Run the main function
if __name__ == "__main__":
    main()
