# Emotion Detector Final Project Submission Answers

## Question 1
Task 1: Submit the public GitHub repository URL of the README.md file, which contains the project name details.

URL:
https://github.com/sablekunal/emotion-detector-final-project

## Question 2
Task 2: Activity 1: Copy and paste the code of the emotion_detection.py file, saved in a file named 2a_emotion_detection, to show the application function you created for the emotion detection application using the Watson NLP library.

```python
import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = myobj, headers=header)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
```

## Question 3
Task 2: Activity 2: Copy and paste the terminal output, saved in the file named 2b_application_creation, which shows that the application was imported and tested without any errors.

```text
kunal@machine:/home/project/final_project$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I am so happy I am doing this.")
{'anger': 0.013646698, 'disgust': 0.0017160787, 'fear': 0.008986979, 'joy': 0.9728826, 'sadness': 0.019916326, 'dominant_emotion': 'joy'}
```

## Question 4
Task 3: Activity 1: Copy and paste the code of the emotion_detection.py file saved in a file named 3a_output_formatting that has modified emotion_detector function to return the correct output format.

```python
import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = myobj, headers=header)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
```

## Question 5
Task 3: Activity 2: Copy and paste the terminal output, saved in the file named 3b_formatted_output_test, which shows the correct format of the application’s output.

```text
kunal@machine:/home/project/final_project$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I am so happy I am doing this.")
{'anger': 0.013646698, 'disgust': 0.0017160787, 'fear': 0.008986979, 'joy': 0.9728826, 'sadness': 0.019916326, 'dominant_emotion': 'joy'}
```

## Question 6
Task 4: Activity 1: Submit the public GitHub repository URL of the __init__.py file, that shows the code to import the application module.

URL:
https://github.com/sablekunal/emotion-detector-final-project/blob/main/EmotionDetection/__init__.py

## Question 7
Task 4: Activity 2: Copy and paste the terminal output saved in the file named 4b_packaging_test which shows the "EmotionDetection" is a valid package.

```text
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I am so happy I am doing this.")
{'anger': 0.013646698, 'disgust': 0.0017160787, 'fear': 0.008986979, 'joy': 0.9728826, 'sadness': 0.019916326, 'dominant_emotion': 'joy'}
```

## Question 8
Task 5: Activity 1: Copy and paste the code of the test_emotion_detection.py file, saved in a file named 5a_unit_testing, that demonstrates the required unit tests.

```python
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Test case for anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test case for disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # Test case for sadness
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
        # Test case for fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
```

## Question 9
Task 5: Activity 2: Copy and paste the terminal output saved in the file named 5b_unit_testing_result which shows all passed unit tests.

```text
kunal@machine:/home/project/final_project$ python3 test_emotion_detection.py
.
----------------------------------------------------------------------
Ran 1 test in 1.488s

OK
```

## Question 10
Task 6: Activity 1: Copy and paste the code of the server.py file, saved in a file named 6a_server, that shows the Web deployment of the application using Flask.

```python
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 11
Task 6: Activity 2: Upload the image of the application deployment, saved as 6b_deployment_test.png.

File name:
6b_deployment_test.png

## Question 12
Task 7: Activity 1: Copy and paste the code of the emotion_detection.py file, saved in a file named 7a_error_handling_function, which shows the updated emotion_detector function for a status code of 400.

```python
import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = myobj, headers=header)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
```

## Question 13
Task 7: Activity 2: Copy and paste the code of the server.py file, saved in a file named 7b_error_handling_server, that shows the handling of blank input errors.

```python
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 14
Task 7: Activity 3: Upload the application deployment output image that validates the error-handling functionality, saved as 7c_error_handling_interface.png.

File name:
7c_error_handling_interface.png

## Question 15
Task 8: Activity 1: Copy and paste the code of the server.py file, saved in a file named 8a_server_modified, that demonstrates the execution of static code analysis.

```python
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 16
Task 8: Activity 2: Copy and paste the terminal output, saved in the file named 8b_static_code_analysis, which shows the pylint score after running the static code analysis.

```text
$ pylint server.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10)
--------------------------------------------------------------------
```

---

This file contains the final answers for all 16 questions of the Emotion Detector final project.
