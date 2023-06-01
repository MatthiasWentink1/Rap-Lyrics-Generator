from transformers import BertTokenizer, BertForMaskedLM
from datasets import load_dataset
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForMaskedLM.from_pretrained("bert-base-uncased")

def tokenize_function(examples):
    result = tokenizer(examples["text"])
    if tokenizer.is_fast:
        result["word_ids"] = [result.word_ids(i) for i in range(len(result["input_ids"]))]


if __name__ == '__main__':
    imdb_dataset = load_dataset("imdb")

    tokenized_datasets = imdb_dataset.map(
        tokenize_function, batched=True, remove_columns=["text","label"]
    )

    print(tokenized_datasets)

