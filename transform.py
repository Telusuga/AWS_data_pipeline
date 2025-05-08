import json
import boto3
import json
import pandas as pd
import io

s3 = boto3.client('s3')
#This function is to pull data from the respective s3 bucket
def get_data_from_s3(bucket_name, key):
    response = s3.get_object(Bucket=bucket_name, Key=key)
    content = response['Body'].read().decode('utf-8')
    return content


def lambda_handler(event, context):
    anime_data=get_data_from_s3('etl-api-testing-raw','un-processed/Anime_Info.json')
    anime_data=json.loads(anime_data) # Once the data is pulled now we perform the appropriate transformation
    #print(test)
    #print(type(test))
    catalog = []
    for i in range(len(anime_data['data'])):
        ID = anime_data['data'][i]['_id']
        Title_Name = anime_data['data'][i]['title']
        Ranking = anime_data['data'][i]['ranking']
        type_of_movie = anime_data['data'][i]['type']
        filtered_data = {
            'ID': ID,
            'Title_Name': Title_Name,
            'Ranking': Ranking,
            'Type_of_Movie': type_of_movie
        }
        catalog.append(filtered_data)  # The filtered data contains single record and is loaded to catalog list
    #print(catalog)
    catalog_buffer=io.StringIO()  #StringIO() is to hold in-memory buffer
    catalog_pd=pd.DataFrame.from_dict(catalog) #To convert the dict value to csv we first read the value
    catalog_pd.to_csv(catalog_buffer,index=False) # Later we convert it to csv object 
    catalog=catalog_buffer.getvalue()  # Now we will be taking the string value and passing it to the s3 function as a string
    try:
        s3_client = boto3.client('s3')
        s3_client.put_object(Body=catalog, Bucket='etl-api-testing-raw', Key='processed/Anime_Info.csv')  # put_object method will only accept string in the body 
        s3.delete_object(Bucket='etl-api-testing-raw', Key='un-processed/Anime_Info.json')  # Once the transformation is completed the raw data is removed or we can move it to archived folder
        print('The raw old data is deleted')
        return {
        'statusCode': 200,
        'body': json.dumps('The Bucket Load is successful')
        }
    except Exception as e:
        return {
        'statusCode': 500,
        'body': json.dumps('The Bucket Load is successful due to the following reason',e)
        }
