from google_play_scraper import reviews, Sort
import pandas as pd
import os

# Create a directory for output files
os.makedirs("data", exist_ok=True)

# Define the apps and their corresponding bank names
apps = {
    'com.combanketh.mobilebanking': 'Commercial_Bank_of_Ethiopia',
    'com.boa.boaMobileBanking': 'Bank_of_Abyssinia',
    'com.dashen.dashensuperapp': 'Dashen_Bank'
}

# Scrape 400 reviews per app and save to individual CSVs
for app_id, bank_filename in apps.items():
    print(f"Scraping reviews for {bank_filename.replace('_', ' ')}...")
    
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=3000
    )

    # Prepare the review data
    reviews_data = []
    for r in result:
        reviews_data.append({
            'review': r['content'],
            'rating': r['score'],
            'date': r['at'].strftime('%Y-%m-%d'),
            'bank': bank_filename.replace('_', ' '),
            'source': 'Google Play'
        })

    # Convert to DataFrame
    df = pd.DataFrame(reviews_data)

    # Clean data: remove duplicates and missing
    df.drop_duplicates(subset=['review'], inplace=True)
    df.dropna(inplace=True)

    # Save to CSV
    output_path = f"data/{bank_filename}_reviews.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")
