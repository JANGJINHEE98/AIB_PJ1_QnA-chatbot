import pymysql
import sys
sys.path.append('/Users/zhenxi/Desktop/for_git/AIB_PJ1/AIB_PJ1_QnA-chatbot/chatbot/config') # 절대 경로로 import 
from DatabaseConfig import * # config 디렉토리의 db 접속 정보 불러오기

db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    # 연결한 db와 상호작용하기 위햔 cursor 객체 생성
    # 그리고 테이블을 생성해준다.
    # 테이블 생성 sql 정의
    sql = '''
        CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        `intent` VARCHAR(45) NULL,
        `ner` VARCHAR(1024) NULL,
        `query` TEXT NULL,
        `answer` TEXT NOT NULL,
        `answer_image` VARCHAR(2048) NULL,
        PRIMARY KEY (`id`))
    ENGINE = InnoDB DEFAULT CHARSET=utf8
    '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()


# try:
#     # db 연결
#     db = pymysql.connect(
#         host=DB_HOST,
#         user=DB_USER,
#         passwd=DB_PASSWORD,
#         db=DB_NAME,
#         charset='utf8'
#     )

#     sql = '''
#     CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
#         `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
#         `intent` VARCHAR(45) NULL,
#         `ner` VARCHAR(1024) NULL,
#         `query` TEXT NULL,
#         `answer` TEXT NOT NULL,
#         `answer_image` VARCHAR(2048) NULL,
#         PRIMARY KEY (`id`))
#     ENGINE = InnoDB DEFAULT CHARSET=utf8
#     '''

#     # 연결한 db와 상호작용하기 위햔 cursor 객체 생성
#     # 그리고 테이블을 생성해준다.
#     with db.cursor() as cursor:
#         cursor.execute(sql)

# except Exception as e:
#     print("에러가 생겼습니다.")

# finally :
#     if db is not None:
#         db.close() # with as 절을 이용하면 이미 db는 닫혀야 하는 것 아닌가? 


'''
[note]
1. AUTO_INCREMENT : 자동으로 (순번으로) index를 부여해줌 (1, 2, 3..)
2. NULL 과 NOT NULL : 후자의 경우 NULL을 허용하지 않음
3. 백틱 `사용에 유의 (객체 명은 백틱으로 설정한다.)
4. PRIMARY KEY는 한 테이블당 하나
'''