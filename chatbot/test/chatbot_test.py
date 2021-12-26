import sys
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/') 

from config.DatabaseConfig import *
from utils.Database import Database
from utils.Preprocess import Preprocess

# 전처리 객체 생성
p = Preprocess(word2index_dic='chatbot/train_tools/dict/chatbot_dict.bin',
               userdic='chatbot/utils/user_dic.tsv')

# 질문/답변 학습 DB 연결 객체 생성
db = Database(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
)
db.connect()  # DB 연결

# 원문
query = input()

# 의도 파악
from models.intent.IntentModel import IntentModel
intent = IntentModel(model_name='chatbot/models/intent/intent_model.h5', preprocess=p)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

# 개체명 인식
from models.ner.NerModel import NerModel
ner = NerModel(model_name='chatbot/models/ner/ner_model.h5', preprocess=p)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)

print("질문 : ", query)
print("=" * 40)
print("의도 파악 : ", intent_name)
print("개체명 인식 : ", predicts)
print("답변 검색에 필요한 NER 태그", ner_tags)
print("=" * 40)

# 답변 검색
from utils.FindAnswer import FindAnswer

try:
    f = FindAnswer(db)
    answer_text, answer_image = f.search(intent_name, ner_tags) # 의도(intent_name)와 인식한 개체명(ner_tags)으로 답변을 검색
    answer = f.tag_to_word(predicts, answer_text)
except:
    answer = "죄송해요, 무슨 말인지 모르겠어요ㅠㅠ"

print("답변 : ", answer)

db.close()  # DB 연결 끊음


'''
[실행 결과]
질문 :  안녕하세요. 햄버거 주문 되나요??
========================================
의도 파악 :  주문
개체명 인식 :  [('안녕하세요', 'B_DT'), ('햄버거', 'B_FOOD'), ('주문', 'O'), ('되', 'O')]
답변 검색에 필요한 NER 태그 ['B_DT']
========================================
답변 :  햄버거 주문 처리 감사!!
'''