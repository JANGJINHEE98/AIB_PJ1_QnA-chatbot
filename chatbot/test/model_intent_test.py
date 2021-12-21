from re import U
import sys
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot')
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel 

w2i_dic_PATH = '/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/train_tools/dict/chatbot_dict.bin'
user_dic_PATH = '/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/utils/user_dic.tsv'

# 전처리 모듈 인스턴스 생성 
p = Preprocess(word2index_dic=w2i_dic_PATH, userdic=user_dic_PATH)

intent = IntentModel(model_name='chatbot/models/intent/intent_model.h5', preprocess=p)

query = "베토디 3개 시킬게요"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스:", predict)
print("의도 예측 테이블:", predict_label)

'''
[실행 결과]
오늘 탕수육 주문 가능한가요?
의도 예측 클래스: 2
의도 예측 테이블: 주문

오늘 날씨 너무 춥다
의도 예측 클래스: 4
의도 예측 테이블: 기타

날씨도 추운데, 설렁탕 한그릇 먹을까?
의도 예측 클래스: 4
의도 예측 테이블: 기타

이것도 모르냐 바보같은 녀석
의도 예측 클래스: 4
의도 예측 테이블: 기타

베토디 3개 시킬게요
의도 예측 클래스: 1
의도 예측 테이블: 욕설

안녕하세요~ 날씨가 너무 좋네요!
의도 예측 클래스: 4
의도 예측 테이블: 기타

안녕하세요~
의도 예측 클래스: 1
의도 예측 테이블: 욕설

안녕
의도 예측 클래스: 0
의도 예측 테이블: 인사


[모델을 같은 조건으로 한번 더 학습 후 결과]

안녕하세요~
의도 예측 클래스: 0
의도 예측 테이블: 인사

베토디 3개 시킬게요
의도 예측 클래스: 4
의도 예측 테이블: 기타
'''