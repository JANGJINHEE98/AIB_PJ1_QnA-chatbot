# 적절한 답변을 검색하는 모듈
# rule base로 답변을 검색한다. 

class FindAnswer:
    def __init__(self, db):
        self.db = db

    # 검색 쿼리 생성
    def _make_query(self, intent_name, ner_tags):
        sql = "select * from chatbot_train_data" # chatbot_train_data는 나의 db에 저장된 테이블명
        if intent_name is not None and ner_tags is None: # 만약 intent가 있고, 개체 인식된 tag가 없으면?
            sql = sql + " where intent='{}' ".format(intent_name) # intent로만 검색해준다. 예) 만약 그냥 인사를 했을 경우에는 intent로만 검색 

        elif intent_name is not None and ner_tags is not None: # intent 있고, 개체 인식된 tag도 있음
            where = " where intent='%s' " % intent_name
            if len(ner_tags) > 0:
                where += "and ("
                for ne in ner_tags:
                    where += " ner like '%{}%' or ".format(ne)
                where = where[:-3] + ')' # [:-3]은 'or '을 제외시키기 위함
            sql = sql + where

        # 동일한 답변이 2개 이상인 경우 랜덤으로 선택
        sql = sql + " order by rand() limit 1"
        return sql

    # 답변 검색
    def search(self, intent_name, ner_tags):
        # 의도명과 개체명으로 답변 검색
        sql = self._make_query(intent_name, ner_tags)
        answer = self.db.select_one(sql)

        # 검색되는 답변이 없으면 의도명만 검색
        if answer is None:
            sql = self._make_query(intent_name, None)
            answer = self.db.select_one(sql) # database에서 의도에 맞는 한줄만 뽑아옴

        return answer['answer'], answer['answer_image']

    # NER 태그를 실제 입력된 단어로 변환
    def tag_to_word(self, ner_predicts, answer):
        for word, tag in ner_predicts:

            # 변환해야 하는 태그가 있는 경우 추가
            # 예) {B_FOOD} 주문 처리 완료되었습니다. 주문해주셔서 감사합니다.
            if tag == 'B_FOOD':
                answer = answer.replace(tag, word)

        answer = answer.replace('{', '')
        answer = answer.replace('}', '')
        return answer