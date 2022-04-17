from transformers import pipeline


class EmotionIdentifier:
    def __init__(self):
        self.classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

    def identify_emotion(self,txt):
        classification = self.classifier(txt)
        return classification[0]['joy']
