"""Detecta emociones en un texto mediante el servicio de análisis."""

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADER = {
    "grpc-metadata-mm-model-id": (
        "emotion_aggregated-workflow_lang_en_stock"
    )
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Devuelve el resultado con todas las emociones sin valor."""
    return {
        **{emotion: None for emotion in EMOTIONS},
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze):
    """Devuelve las puntuaciones emocionales y la emoción dominante.

    Si el servicio responde con estado 400, devuelve None para cada valor.
    """
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        URL,
        json=myobj,
        headers=HEADER,
        timeout=30,
    )

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    data = response.json()
    emotions = data["emotionPredictions"][0]["emotion"]

    result = {
        emotion: emotions[emotion]
        for emotion in EMOTIONS
    }
    result["dominant_emotion"] = max(
        result,
        key=result.get,
    )

    return result
