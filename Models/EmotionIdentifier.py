from transformers import pipeline
import numpy as np
from ProjectUtils.Consts import *


class EmotionIdentifier:
    emotion_idxs = {'anger': 1, 'disguts': 2, 'fear': 3, 'joy': 4,
                             'neutral': 5, 'sadness': 6, 'surprise': 7}
    emotion_by_idx = {1: 'anger', 2: 'disgust', 3: 'fear', 4: 'joy',
                               5: 'neutral', 6: 'sadness', 7: 'surprise'}

    def __init__(self):

        self.classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

    def identify_emotion(self, txt):
        """
        splitting text for windows, each windows get classification for emotion.
        emotion with most score will be the emotion of the text
        :param txt:
        :return: emotion classification of the text
        """
        emotions_buckets = np.zeros(8)
        num_windows = int(len(txt) / LENGTH_OF_WINDOW_FOR_CLASSIFICATION)
        for i in range(num_windows - 1):
            classification = self.classifier(
                txt[i * LENGTH_OF_WINDOW_FOR_CLASSIFICATION:(i + 1) * LENGTH_OF_WINDOW_FOR_CLASSIFICATION])
            tag = classification[0]['label']
            emotions_buckets[EmotionIdentifier.emotion_idxs[tag]] += 1

        return self.get_emotion_by_idx(emotions_buckets)

    def get_emotion_by_idx(self, emotions_buckets):
        """
        :param emotions_buckets:
        :return: index i which emotions_buckets[i] is maximum
        """
        emotion_with_max_score = np.argmax(emotions_buckets)
        emotion = EmotionIdentifier.emotion_by_idx[emotion_with_max_score]
        return emotion
