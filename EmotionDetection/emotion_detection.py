''' Function to start the emotion 
    detection analysis given a string
'''
import requests
import json

def emotion_detector(text_to_analyse):
    '''
    emotion_detector function definition
    '''
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header for the emotion predict service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Request payload in json format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Post request definition
    response = requests.post(url, json=myobj, headers=headers)

    # Format Response
    formatted_response = json.loads(response.text)

    # Error handling in case of blank entries 
    if response.status_code == 400:
        emotion_dict = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        return (emotion_dict)

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    emotion_dict = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    }
    max_emotion_score = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = max_emotion_score

    # Return a dict for emotion detection results
    return emotion_dict