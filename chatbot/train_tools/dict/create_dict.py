# 챗봇에서 사용하는 사전 파일 생성 
# -> 학습을 위해서 쓰는 걸까?

import sys
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot')
from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

# 말뭉치 데이터 읽는 함수
def read_corpus_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[:1] # 헤더 제거
    return data

# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/train_tools/dict/corpus.txt')

# 말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])

# ?? 키워드 추출이라고 했는데, 태거 메서드 (pos)만 사용한 이유?
# pos의 리턴값을 다시 한번 보자. 

# 사전에 사용될 word2index 생성
# 사전의 첫번째 인덱스에는 OOV사용 
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV') # Out Of Voca
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()



'''
[note]
** read_corpus_data 설명 **
with open(filename, 'r') 에서 'r'은 읽기 모드로 열겠다는 뜻 open() 함수의 옵션
f.read().splitlines() -> 파일에서 라인별로 split 해줌 
0000	헬로우		0 가 하나의 라인
['0000', '헬로우', '0']
여기서 첫번째 요소 data[0]을 제거하고 
결과는 아래와 같다.
['헬로우', '0']
'''