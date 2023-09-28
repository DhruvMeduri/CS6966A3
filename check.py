import jsonlines

with jsonlines.open('a1_analysis_data.jsonl','r') as reader:
    for obj in reader:
        print(obj['Review'])