import json
import boto3
import json
import requests

def lambda_handler(event, context):
    url = "https://anime-db.p.rapidapi.com/anime"

    querystring = {"page": "1", "size": "10", "search": "Fullmetal", "genres": "Fantasy,Drama", "sortBy": "ranking",
                   "sortOrder": "asc"}

    headers = {
        "x-rapidapi-key": "32f0bd65ffmshc8b8f556b5bc1f2p158cdbjsn41e9f6e10186",
        "x-rapidapi-host": "anime-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    anime_data = response.json() # The data which is Full Metal related info is in the variable anime_data
    try:
        catalog = json.dumps(anime_data)
        s3_client = boto3.client('s3')
        s3_client.put_object(Body=catalog, Bucket='etl-api-testing-raw', Key='un-processed/Anime_Info.json')
        # The Data load to the bucket is carried next and the following data is a raw data
        return {
        'statusCode': 200,
        'body': json.dumps('Data load is successful')
        }
    except Exception as e:
        return {
        'statusCode': 500,
        'body': json.dumps('Data load is failed due to the following errors-->',e)
        }
