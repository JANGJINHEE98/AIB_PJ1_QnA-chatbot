import pymysql
import openpyxl

import sys
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/config') # 절대 경로로 import 
from DatabaseConfig import * # config 디렉토리의 db 접속 정보 불러오기


# 학습 데이터 초기화
def all_clear_train_data(db):
    # 기존 학습 데이터 삭제
    # delete from 테이블 이름 : 테이블의 모든 데이터가 삭제된다.
    sql = '''
        delete from chatbot_train_data
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)

    # auto increment 초기화 
    # alter table : 테이블 수정
    # auto_increment 를 1부터 시작하도록 다시 초기화
    sql = '''
        ALTER TABLE chatbot_train_data AUTO_INCREMENT=1
    '''
    with db.cursor() as cursor:
        cursor.execute(sql)


# db에 데이터 저장
def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url = xls_row

    sql = '''
        INSERT chatbot_train_data(intent, ner, query, answer, answer_image)
        values(
            '%s', '%s', '%s', '%s', '%s'
        )
    ''' % (intent.value, ner.value, query.value, answer.value, answer_img_url.value)

    # 엑셀에서 불러온 cell에 데이터가 없는 경우 null로 치환
    sql = sql.replace("'None'", "null")

    with db.cursor() as cursor:
        cursor.execute(sql)
        print('{} 저장'.format(query.value))
        db.commit()


train_file = '/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/train_tools/qna/train_data.xlsx'
db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    # 기존 학습 데이터 초기화
    all_clear_train_data(db)

    # 학습 엑셀 파일 불러오기
    wb = openpyxl.load_workbook(train_file)
    sheet = wb['Sheet1'] # 엑셀 파일에서 sheet1(첫번째 sheet)사용
    for row in sheet.iter_rows(min_row=2):  # 헤더는 불러오지 않음
        # 데이터 저장
        insert_data(db, row)

    wb.close()

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()




'''
[note]
values(%s들..)는 파라미터의 역할을 한다. 
intent, ner, query, answer, answer_image라는 field 안에 값들을 넣어줌
pyopenxl 관련해서는 notion 참고 (iter_row에 대한 설명 유)

[잘 모르는 부분]
insert_data 함수에서 
sql 두개를 한번에? 
'''

    