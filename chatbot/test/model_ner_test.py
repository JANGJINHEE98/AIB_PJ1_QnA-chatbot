import sys
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot')

from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

w2i_dic_PATH = '/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/train_tools/dict/chatbot_dict.bin'
user_dic_PATH = '/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/utils/user_dic.tsv'

p = Preprocess(word2index_dic=w2i_dic_PATH,
               userdic=user_dic_PATH)

ner = NerModel(model_name='chatbot/models/ner/ner_model.h5', preprocess=p)
query = '돈까스 배달 되나요?'
predicts = ner.predict(query)
print("입력 쿼리:", query)
print("결과:", predicts)

pre_tags = ner.predict_tags(query)
print(pre_tags)

'''
[note]
BIO 태그는 아래와 같다. 
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

[test 결과]
입력 쿼리: 안녕하세요
결과: [('안녕하세요', 'O')]

입력 쿼리: 김밥 3줄만 배달해주세요. 위치는 서울특별시 서초구 서초동 서초대로 396입니다.
결과: [('김밥', 'B_OG'), ('3', 'I'), ('줄', 'O'), ('배달', 'O'), ('주', 'O'), ('위치', 'O'), ('서울특별시', 'B_LC'), ('서초구', 'B_LC'), ('서초동', 'O'), ('서초대로', 'O'), ('396', 'O'), ('이', 'O')]

입력 쿼리: 돈까스 배달 되나요?
결과: [('돈까스', 'B_FOOD'), ('배달', 'O'), ('되', 'O')]

입력 쿼리: 오늘 3시 햄버거 세트 100개 예약
결과: [('오늘', 'B_DT'), ('3시', 'O'), ('햄버거', 'O'), ('세트', 'O'), ('100', 'O'), ('개', 'O'), ('예약', 'O')]

음식 같은 경우, 데이터가 없으면 아예 예측을 잘 못한다. 다양한 유형의 문장 학습 필요. (음식 데이터를 더 찾아볼까?)
'''

