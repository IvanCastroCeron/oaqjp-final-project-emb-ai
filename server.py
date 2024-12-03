''' Executing this function initiates the application of emotion detector
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app:
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    out_dict = emotion_detector(text_to_analyze)

    # Error handling for blank entries
    if out_dict['dominant_emotion'] is None:
        return "Invalid Text! Please try again!."

    return f"For the given statement, the system response is \
    'anger': {out_dict['anger']}, \
    'disgust': {out_dict['disgust']}, \
    'fear': {out_dict['fear']}, \
    'joy': {out_dict['joy']} and \
    'sadness': {out_dict['sadness']}. \
    The dominant emotion is {out_dict['dominant_emotion']}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
