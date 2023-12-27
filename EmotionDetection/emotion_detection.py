import requests
import json

def emotion_detector(text_to_analyse):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   myobj = { "raw_document": { "text": text_to_analyse } }
   header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   response = requests.post(url, json = myobj, headers=header)
   formatted_response = json.loads(response.text)
   for emotion in formatted_response['emotionPredictions']:
     anger = emotion['emotion']['anger']
     disgust = emotion['emotion']['disgust']
     fear = emotion['emotion']['fear']
     joy  = emotion['emotion']['joy']
     sadness = emotion['emotion']['sadness']
     return {'anger': anger, 'disgust': disgust, 'anger': anger, 'fear': fear, 'joy': joy, 'sadness': sadness}
   
   
   
   
   

