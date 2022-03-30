# 🎯 음식 주문 QnA-chatbot을 구현하는 프로젝트

* 코드스테이츠 AI 부트캠프 첫번째 프로젝트 수행 과제물입니다.
* [처음 배우는 딥러닝 챗봇](https://m.hanbit.co.kr/store/books/book_view.html?p_code=B7030488815)(한빛미디어)를 참고하여 만들었습니다. 
* 사용한 모델 : 의도 분류에 쓰인 모델은 CNN이며, 개체 인식에 쓰인 모델은 양방향 LSTM입니다.

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
