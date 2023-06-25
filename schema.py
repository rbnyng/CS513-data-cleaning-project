import pandas as pd

df = pd.read_csv('source_data/winemag-data-130k-v2.csv')

# Create WineReviews DataFrame
wine_reviews = df[['Unnamed: 0', 'description', 'points', 'price', 'title', 'variety', 'designation']].copy()
wine_reviews['reviewer_id'] = df['taster_name'].astype('category').cat.codes
wine_reviews['winery_id'] = df['winery'].astype('category').cat.codes
wine_reviews.rename(columns={'Unnamed: 0': 'index'}, inplace=True)

# Create Reviewers DataFrame
reviewers = df[['taster_name', 'taster_twitter_handle']].drop_duplicates().reset_index(drop=True)
reviewers['reviewer_id'] = reviewers.index

# Create Wineries DataFrame
wineries = df[['country', 'province', 'region_1', 'region_2', 'winery']].drop_duplicates().reset_index(drop=True)
wineries['winery_id'] = wineries.index

wine_reviews.to_csv('intermediate_data/wine_reviews.csv', index=False)
reviewers.to_csv('intermediate_data/reviewers.csv', index=False)
wineries.to_csv('intermediate_data/wineries.csv', index=False)