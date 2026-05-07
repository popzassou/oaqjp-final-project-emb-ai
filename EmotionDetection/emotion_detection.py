import requests
import json

def emotion_detector(text_to_analyze):
    # Tentukan URL dan headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Kirim POST request
    response = requests.post(url, json=input_json, headers=headers)
    
    # Mengubah teks response menjadi dictionary menggunakan json library
    formatted_response = json.loads(response.text)
    
    # Mengekstrak kumpulan emosi dari struktur JSON yang diberikan oleh Watson NLP
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Mengambil masing-masing skor
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Mencari emosi yang paling dominan (skor tertinggi)
    # Fungsi max() dengan parameter key akan mencari nilai tertinggi dalam dictionary
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Mengembalikan dictionary sesuai format yang diminta di Task 3
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }