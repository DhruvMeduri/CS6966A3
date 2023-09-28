import jsonlines

with jsonlines.open('output.jsonl','r') as reader:
    for obj in reader:
        print(obj['Review'])