bert model을 활용해 유사도 0.77로 기존 일상대화 prompt를 다시 걸러낸 다음  
gpt3.5를 활용해 다시 답변 생성  
이후 추가로 답변 수정 후  

filter폴더는 bert 모델로 instruction과 output이 0.90이상의 유사도 즉 비슷한 내용을 담은 것들을 필터링 하여  
다시 gpt4 이용해 답변 수동 생성 
test prompt는  
no prompt, 다음 질문에 친절하고 간결히 답변하세요, 다음 질문에 친절하고 간결하고 정확하게 답변하세요. 3가지 테스트 폴더  
최종적으로 친절하고 간결만 들어갔다.  정확히는 너무 답변이 도움을 주기 위해 장황해지기 때문  
답변 길이: no -> 179, 친절하고 간결 -> 169, +정확히 -> 230  