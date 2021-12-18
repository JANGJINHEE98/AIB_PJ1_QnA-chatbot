# 전처리 모듈
# 챗봇 엔진 내에서 자주 사용하기 때문에 클래스로 정의 
from konlpy.tag import Komoran

class Preprocess:
    def __init__(self, userdic=None):
        # 형태소 분석기 초기화 
        self.komoran = Komoran(userdic=userdic)

        # 제외할 품사 / 일부 품사를 불용어 처리합니다. 
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKO', 'JKB', 'JKV', 'JKQ',
            'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]

    # 형태소 분석기 POS 태거
    def pos(self, sentence):
        return self.komoran.pos(sentence)

    # 불용어 제거한 후 핵심 키워드 정보만 가져옴
    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False: # 단어가 exclusion_tags에 포함되지 않는다면! (불용어가 아니라면)
                word_list.append(p if without_tag is False else p[0])
        return word_list

    


'''
[note]
komoran pos를 쓸 경우, 
[('안녕', 'IC'), ('.', 'SF'), ('나', 'NP'), ('는', 'JX'), 
('하늘색', 'NNP'), ('과', 'JC'), ('딸기', 'NNP'), ('를', 'JKO'), 
('좋아하', 'VV'), ('아', 'EC')]
=> 단어와 형태소가 튜플 형태로 묶이고 문장이 리스트에 담겨 나옴
'''