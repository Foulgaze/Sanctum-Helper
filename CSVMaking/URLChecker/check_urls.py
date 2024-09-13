import pandas as pd
import requests

# Load the CSV into a pandas DataFrame
df = pd.read_csv('cards.csv')  # Replace 'your_file.csv' with your actual file path
goodCards = open("goodUUIDs.txt", "w")
badCards = open("badUUIDs.txt", "w")
# Drop duplicate set codes to check only one card per set
unique_sets = df.drop_duplicates(subset='setCode')

def check_url_validity(set_code, card_number):
    url = f"https://api.scryfall.com/cards/{set_code.lower()}/{card_number}?format=image&version=normal&face=front"
    response = requests.get(url)
    return response.status_code == 200  # Returns True if the URL is valid (status code 200)

# Iterate over each row in the DataFrame and check the URL
for index, row in df.iterrows():
    if index % 1000 == 0:
        print(f"{index}")
    set_code = row['setCode']
    card_number = row['number']
    
    is_valid = check_url_validity(set_code, card_number)
    uuid = row["uuid"]
    if is_valid:
        goodCards.write(f"{uuid}\n")
    else:
        badCards.write(f"{uuid}\n")

