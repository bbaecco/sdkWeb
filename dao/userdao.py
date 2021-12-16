# -- coding: utf-8 --
import json
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()
#커넥션 한 번만 할 수 있게 만들어보기
def getConnection():
    return pymysql.connect(host=os.getenv('MYSQL_HOST'),
                    port=int(os.getenv('MYSQL_PORT')),
                    user=os.getenv('MYSQL_USER'),
                    passwd=os.getenv('MYSQL_PASSWORD'),
                    db=os.getenv('MYSQL_DATABASE'),
                    charset=os.getenv('MYSQL_CHARSET'),
                    cursorclass=pymysql.cursors.DictCursor)


# datetime을 포함한 데이터를 json으로 바로 바꿀 수 있도록 추가한 함수
def user_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

#Create
#name을 parameter로 받아 user 테이블에 추가
def createUser(userid, pwd):
    conn = getConnection()
    curs = conn.cursor()
    sql = "INSERT INTO user(userid, pwd) VALUES (%s, %s)"
    ok = curs.execute(sql, (userid, pwd))
    conn.commit()
    conn.close()
    return json.dumps({'rows': ok})

#Read
#user 테이블의 모든 user 읽기
def getAllUsers():
    conn = getConnection()
    curs = conn.cursor(pymysql.cursors.DictCursor)  #select한 데이터를 Dictionary 형태로 가져옴
    sql = "SELECT * FROM user"
    curs.execute(sql)  #sql 처리
    rows = curs.fetchall()  #처리된 데이터 가져옴
    conn.close()
    return json.dumps(rows, default=user_handler)  #처리된 데이터 json으로 변경

#Update
#user 테이블의 user 수정
def updateUser(userid, pwd):
    conn = getConnection()
    curs = conn.cursor()
    sql = "UPDATE user SET pwd=%s WHERE userid=%s"
    ok = curs.execute(sql, (pwd, userid))
    conn.commit()
    conn.close()
    return json.dumps({'rows': ok})

#Delete
#user 테이블의 user 삭제
def deleteUser(userid):
    conn = getConnection()
    curs = conn.cursor()
    sql = "DELETE FROM user WHERE userid=%s"
    ok = curs.execute(sql, userid)
    conn.commit()
    conn.close()
    return json.dumps({'rows': ok})


# if __name__ == "__main__":
#     createUser('rwar', 'rasaaaaaaa')