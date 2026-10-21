''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector, EMOTIONS

#Initiate the flask app : DONE
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # Recupera el texto a analizar de los argumentos de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')
    # Pasa el texto a la función emotion_detector y almacena la respuesta
    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    emotion_text = ", ".join(
        f"'{emotion}': {response[emotion]}"
        for emotion in EMOTIONS[:-1]
    )
    emotion_text += f" and '{EMOTIONS[-1]}': {response[EMOTIONS[-1]]}"

    return (
        "For the given statement, the system response is "
        f"{emotion_text}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # DONE
    return render_template('index.html')

if __name__ == "__main__":
    # DONE
    app.run(host="0.0.0.0", port=5000)
