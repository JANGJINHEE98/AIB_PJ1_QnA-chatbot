# AIB_PJ1_QnA-chatbot

의도 분류에 쓰인 모델 CNN
개체 인식에 쓰인 모델 양방향 LSTM 

[의도 분류 모델 class]
인사    0
욕설    1
주문    2
예약    3
기타    4

[개체 인식에 쓰인 모델 class]
{1: 'O', - (한글 이외(외국어, 한자, 숫자))
 2: 'B_DT', - 날짜
 3: 'B_FOOD', - 음식
 4: 'I', - (감탄사)
 5: 'B_OG', - 조직, 회사
 6: 'B_PS', - 사람
 7: 'B_LC', - 지역
 8: 'NNP', - (고유명사)
 9: 'B_TI', - 시간
 0: 'PAD'}

의도 분류 모델 학습데이터
models/intent/total_train_data.csv

개체 인식 모델 학습데이터
models/ner/ner_train.txt




'O'  이외(기타)
'B_DT'  날짜
'B_FOOD'  음식
'B_OG'  조직, 회사
'B_PS'  사람
'B_LC'  지역
'B_TI'  시간