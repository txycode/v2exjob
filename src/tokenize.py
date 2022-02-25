import os
import json
from ckip_transformers.nlp import CkipNerChunker

current_path = os.path.dirname(os.path.abspath(__file__))


def show_result(ner):
    print(ner)
    for s in ner:
        for e in s:
            print(e)

ner_driver = CkipNerChunker(model_name='ckiplab/bert-base-chinese')
with open(f'{current_path}/data/topic/topic_150938.json', 'r') as f:
    topic = json.load(f)
    text = topic['content']
    title = topic['title']
    print(title)
    ner = ner_driver(title)
    show_result(ner)
    # print(text)
    # ner = ner_driver(text)
    # show_result(ner)
    