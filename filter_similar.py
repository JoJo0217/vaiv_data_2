from sentence_transformers import SentenceTransformer, util
import json
import numpy as np
#bert model로 전체 내용 중에서 겹치는 부분을 삭제합니다.

embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")
# embedder = SentenceTransformer("BM-K/KoSimCSE-roberta-multitask")
# embedder = SentenceTransformer("sentence-transformers/all-roberta-large-v1")

# Load jsonl data into a Python list of dictionaries
data = []
with open("./step1/raw_dataset/gamseong/filtered_step2_step3_gam.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        data.append(json.loads(line))

# Get the prompts from the data
corpus = [item["prompt"] for item in data]

# Compute the embeddings for the prompts
corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

# Set a similarity threshold and initialize an empty set for duplicates
similarity_threshold = 0.6 # Adjust this value according to your needs
duplicates = set()
duplicates_list = []

# Compute pairwise cosine similarity scores, and find duplicates
for i, query_embedding in enumerate(corpus_embeddings):
    if i not in duplicates:
        cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
        cos_scores = cos_scores.cpu().numpy()

        duplicate_indices = np.where(cos_scores > similarity_threshold)[0]
        for j in duplicate_indices:
            if i != j and j not in duplicates:
                duplicates.add(j)
                duplicates_list.append((i, j, cos_scores[j]))

# Remove duplicates from the data based on the similarity threshold
unique_data = [item for i, item in enumerate(data) if i not in duplicates]

# Save unique data to a new jsonl file
with open("conv_unique.jsonl", "w", encoding="utf-8") as output_file:
    for item in unique_data:
        output_file.write(json.dumps(item, ensure_ascii=False) + "\n")

# Output duplicate sentence pairs and their similarity scores
for i, j, score in duplicates_list:
    print(f"Line {i}: {corpus[i]}")
    print(f"Line {j}: {corpus[j]}")
    print(f"Similarity: {score:.2f}")
    print()

print(f"\nremoved: {len(duplicates)}")
