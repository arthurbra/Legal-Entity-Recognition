# docker pull huggingface/transformers-cpu
# export PYTHONIOENCODING=UTF-8

from transformers import pipeline

nlp_ler = pipeline(
    "ner",
    #dieses modell liefert nur müll...
    #model="mrm8488/bert-base-german-finetuned-ler",
    #tokenizer="mrm8488/bert-base-german-finetuned-ler",

    model="Sahajtomar/NER_legal_de",
    tokenizer="Sahajtomar/NER_legal_de",
    
    grouped_entities = True,
    #ignore_subwords = True
)

text = "Für eine Zuständigkeit des Verwaltungsgerichts Berlin nach § 52 Nr. 1 bis 4 VwGO hat der \
         Antragsteller keine Anhaltspunkte vorgetragen ."

print(text)
print(nlp_ler([text, text]))
