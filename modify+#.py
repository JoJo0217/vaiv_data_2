import json

load_file="train.json"
save_file="train_template.json"
# eval.json 파일 로드
with open(load_file, "r", encoding="utf-8") as file:
    data = json.load(file)
    #data = [json.loads(line) for line in file.readlines()]

# "### 질문: "과 "### 답변: "을 prompt에 붙이기
for item in data:
    #item["prompt"] = f"### 질문: {item['prompt']} ### 답변: "
    item["prompt"] = f"아래는 작업을 설명하는 명령어입니다. 요청을 적절히 완료하는 응답을 작성하세요.\n\n### 명령어:\n{item['prompt']}\n\n### 응답:\n"
    #item['chosen']=""
    #item['rejected']=""
    if 'id' in item:
        del item['id']
# 수정된 데이터를 새로운 JSON 파일로 저장
with open(save_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
