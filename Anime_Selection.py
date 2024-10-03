import requests
import json
import pandas as pd

import numpy as np

api_url = "https://api.jikan.moe/v4/genres/anime"
client_id = 'e146cb4b87528365d2b2978c4757bf6d'


params = {
    'genres': {'name': 'Sports'},
    
}

response = requests.get(api_url, headers={'X-MAL-CLIENT-ID': client_id})

data = response.json()

#print(response)
print(data)

# anime_df = pd.json_normalize(data['data'])
anime_list = []
# for anime in data.get('data', []):
    #anime_id = anime['node']['id']
    # print(anime_id)
    #api_url_id = f'https://api.myanimelist.net/v2/anime/{anime_id}?fields=title,genres'
    #response2 = requests.get(api_url_id, headers={'X-MAL-CLIENT-ID': client_id})
    #print(response2)
    #anime_data = response2.json()
    #print(anime_data)
    #for genre in anime_data['genres']:
        #if genre['name'] == 'Sports':
            #anime_list.append(anime['node']['title'])
    #if len(anime_list) >= 10:
        #break
    
    # print(f"Title: {anime['node']['title']}, ID: {anime['node']['id']}', ranking: {anime['ranking']['rank']}")

# print(anime_list)

# print(anime_df)

# Checking to see if git is working

# 2nd check to see if working