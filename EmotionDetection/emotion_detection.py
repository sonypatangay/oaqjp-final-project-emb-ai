import requests
import json
import math

def emotion_detector(text_to_analyse):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   myobj = { "raw_document": { "text": text_to_analyse } }
   header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   response = requests.post(url, json = myobj, headers=header)
   if response.status_code == 200:
    formatted_response = json.loads(response.text)
    for emotion in formatted_response['emotionPredictions']:
        emotionDict = emotion['emotion']
        emotionKey = max(zip(emotionDict.values(), emotionDict.keys()))[1]
        anger = emotion['emotion']['anger']
        disgust = emotion['emotion']['disgust']
        fear = emotion['emotion']['fear']
        joy  = emotion['emotion']['joy']
        sadness = emotion['emotion']['sadness']
   elif response.status_code == 400:
        emotionKey = None
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
    
   return {'anger': anger, 'disgust': disgust, 'anger': anger, 'fear': fear, 
    'joy': joy, 'sadness': sadness, 'dominant_emotion': emotionKey }

   
   
   
   

