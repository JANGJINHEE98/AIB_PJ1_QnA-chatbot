# 전처리 함수를 테스트 해봅니다.
import sys
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot')
from utils.Preprocess import Preprocess

sent = "내일 오전 10시에 탕수육 주문하고 싶어!!!"

p = Preprocess(userdic='/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/utils/user_dic.tsv')

pos = p.pos(sent)

# 품사 태그와 같이 키워드 출력 
ret = p.get_keywords(pos, without_tag=False)
print(ret)

# 품사 태그 없이 키워드 출력
ret = p.get_keywords(pos, without_tag=True)
print(ret)

'''
[테스트 결과]
[('내일', 'NNG'), ('오전', 'NNP'), ('10', 'SN'), ('시', 'NNB'), ('탕수육', 'NNP'), ('주문', 'NNG'), ('싶', 'VX'), ('!!', 'NNP')]
['내일', '오전', '10', '시', '탕수육', '주문', '싶', '!!']

[보완 할 점]
불용어 사전을 만들어서 !!라던가 특수문자 등은 뺄 수 있도록 해야겠다. 
'''


