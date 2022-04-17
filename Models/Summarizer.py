import json
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
MODEL_TYPE = "t5-small"
PROCESSING_UNIT = 'cpu'


class Summarizer:
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained(MODEL_TYPE)
        self.model = T5Tokenizer.from_pretrained(MODEL_TYPE)
        self.device = torch.device(PROCESSING_UNIT)

    def get_summay(self,txt):
        to_summary = "summarize: "+txt
        tokenized_text = self.tokenizer.encode(to_summary, return_tensors="pt").to(PROCESSING_UNIT)

        summary_ids = self.model.generate(tokenized_text,
                                     num_beams=4,
                                     no_repeat_ngram_size=2,
                                     min_length=30,
                                     max_length=100,
                                     early_stopping=True
                                     )

        output=self.tokenizer.decode(summary_ids[0],skip_special_tokens=True)
