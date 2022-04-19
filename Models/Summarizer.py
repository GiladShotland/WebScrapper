import json
import torch
from transformers import pipeline
from ProjectUtils.Consts import *


class Summarizer:
    def __init__(self):
        self.generator = pipeline("text2text-generation")

    def get_summary(self, txt):
        """
        splitting the text for windows.
        summarizing each window and adding the summaries all together
        :param txt:
        :return: summaries
        """
        num_windows = int(len(txt) / LENGTH_OF_WINDOW_FOR_SUMMARIZATION)
        summary_length_for_window = int(LENGTH_OF_SUMMARY / num_windows)
        ans = ""
        for i in range(num_windows - 1):

            generator_output=  self.generator("summarize: " + txt[i * LENGTH_OF_WINDOW_FOR_SUMMARIZATION:(
                                                                                                         i + 1) * LENGTH_OF_WINDOW_FOR_SUMMARIZATION],
                                  max_length=summary_length_for_window)
            output_dict = generator_output[0]
            ans += output_dict['generated_text']

        return ans
