from transformers import pipeline
PRETRAINED = "raynardj/ner-disease-ncbi-bionlp-bc5cdr-pubmed"
ners = pipeline(task="ner",model=PRETRAINED, tokenizer=PRETRAINED)
