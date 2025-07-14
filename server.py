'''
This is the Emotion detection service
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    '''
    This function gets a text from web interface, provides its analysis, returns values
    for 5 emotions and main emotion
    '''
    text = request.args.get("textToAnalyze")
    resp = emotion_detector(text)
    if resp['dominant_emotion'] is None:
        return " Invalid text! Please try again!"
    return f"""For the given statement,
    the system response is \'anger\': {resp['anger']}, 
    \'disgust\': {resp['disgust']}, \'fear\': {resp['fear']},
    \'joy\': {resp['joy']} and \'sadness\': {resp['sadness']}. 
    The dominant emotion is {resp['dominant_emotion']}."""

@app.route("/")
def render_index_page():
    '''
    The default way
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
