import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    # Convierte la cadena JSON en un diccionario de Python
    datos = json.loads(response.text)

    # Obtiene las puntuaciones de la primera predicción
    emociones = datos["emotionPredictions"][0]["emotion"]

    nombres = ["anger", "disgust", "fear", "joy", "sadness"]
    puntuaciones = {nombre: emociones[nombre] for nombre in nombres}

    # Encuentra la emoción con la puntuación más alta
    emocion_dominante = max(puntuaciones, key=puntuaciones.get)

    # Devuelve el resultado en el formato solicitado
    return {
        **puntuaciones,
        "dominant_emotion": emocion_dominante
    }