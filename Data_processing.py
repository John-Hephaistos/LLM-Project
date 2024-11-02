import pandas as pd
import re
import numpy as np
import json

def remove_non_alphanumeric(text):
    return re.sub(r'[^a-zA-Z0-9]', ' ', text)



df = pd.DataFrame(pd.read_csv("C:/Users/VLAD/LLM-Project/data/raw/IMDB Dataset.csv"))
df['review'] = df['review'].apply(remove_non_alphanumeric)

df.rename(columns={'review': 'prompt', 'sentiment': 'completion'}, inplace=True)




df['completion'] = df['completion'].replace({'positive':1, 'negative':2})
#df['completion'] = df['completion'].apply(lambda x: f" {x} ")
dataset_length = len(df)
# only use a % of the large dataset
percentege = 0.1
dataset_length = int(dataset_length * percentege)
df = df[:dataset_length]
sub_df = df['prompt'].apply(lambda x: len(x))
sub_df = np.array(sub_df)
print(sub_df.sum())

# 80 - 10 - 10 split

train_index = int(dataset_length * 0.8)
val_index = int(dataset_length * 0.9)
df_train = df[:train_index]
print(df_train)
df_train.to_csv('train_data.csv', index=False)
df_val = df[train_index:val_index]
print(df_val)
df_val.to_csv('val_data.csv', index=False)
df_test = df[val_index:]
print(df_test)
df_test.to_csv('test_data.csv', index=False)



input_files = ['train_data.csv', 'val_data.csv', 'test_data.csv']
output_files = ['train_data_prepared_gpt4.jsonl','val_data_prepared_gpt4.jsonl', 'test_data_prepared_gpt4.jsonl']

for input_file, output_file in zip(input_files, output_files):
    with open(output_file, 'w') as out_file:
        data = pd.read_csv(input_file)
        for line in data:
            prompt = data["prompt"]
            completion = data["completion"]
            gpt4_data = {
                "messages": [
                    {"role": "system",
                     "content": "As a social scientist, your task is to analyze the sentiment of user movie reviews extracted from IMDB. Please assign a sentiment score of 1 or 2 for each movie review, where 1 signifies positive sentiment, and 2 corresponds to negative sentiment."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": completion}
                ]
            }

            # Write the new data to the output file in JSONL format
            out_file.write(json.dumps(gpt4_data) + '\n')


# Open the input JSONL file
input_file = 'train_data_prepared.jsonl'
output_file = 'train_data_prepared_gpt4.jsonl'

# Open the output file for writing
with open(output_file, 'w') as out_file:
    # Read each line from the input file
    with open(input_file, 'r') as in_file:
        for line in in_file:
            # Parse the JSON line
            data = json.loads(line)

            # Extract the prompt and completion
            prompt = data["prompt"]
            completion = data["completion"]

            # Convert to GPT-4 message format
            gpt4_data = {
                "messages": [
                    {"role": "system", "content": "As a social scientist, your task is to analyze the sentiment of user movie reviews extracted from IMDB. Please assign a sentiment score of 1 or 2 for each movie review, where 1 signifies positive sentiment, and 2 corresponds to negative sentiment."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": completion}
                ]
            }

            # Write the new data to the output file in JSONL format
            out_file.write(json.dumps(gpt4_data) + '\n')


input_file = 'val_data_prepared.jsonl'
output_file = 'val_data_prepared_gpt4.jsonl'

# Open the output file for writing
with open(output_file, 'w') as out_file:
    # Read each line from the input file
    with open(input_file, 'r') as in_file:
        for line in in_file:
            # Parse the JSON line
            data = json.loads(line)

            # Extract the prompt and completion
            prompt = data["prompt"]
            completion = data["completion"]

            # Convert to GPT-4 message format
            gpt4_data = {
                "messages": [
                    {"role": "system", "content": "As a social scientist, your task is to analyze the sentiment of user movie reviews extracted from IMDB. Please assign a sentiment score of 1 or 2 for each movie review, where 1 signifies positive sentiment, and 2 corresponds to negative sentiment."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": completion}
                ]
            }

            # Write the new data to the output file in JSONL format
            out_file.write(json.dumps(gpt4_data) + '\n')

input_file = 'test_data_prepared.jsonl'
output_file = 'test_data_prepared_gpt4.jsonl'

# Open the output file for writing
with open(output_file, 'w') as out_file:
    # Read each line from the input file
    with open(input_file, 'r') as in_file:
        for line in in_file:
            # Parse the JSON line
            data = json.loads(line)

            # Extract the prompt and completion
            prompt = data["prompt"]
            completion = data["completion"]

            # Convert to GPT-4 message format
            gpt4_data = {
                "messages": [
                    {"role": "system", "content": "As a social scientist, your task is to analyze the sentiment of user movie reviews extracted from IMDB. Please assign a sentiment score of 1 or 2 for each movie review, where 1 signifies positive sentiment, and 2 corresponds to negative sentiment."},
                    {"role": "user", "content": prompt}
                ]
            }

            # Write the new data to the output file in JSONL format
            out_file.write(json.dumps(gpt4_data) + '\n')