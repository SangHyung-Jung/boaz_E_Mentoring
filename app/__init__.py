from flask import Flask
import sys
sys.path.append("../helper/")
from db_helper import DB_HELPER
import time

now = time.gmtime(time.time())
db = DB_HELPER()
app = Flask(__name__) ## 플라스크를 생성하고 app 변수에 flask 초기화 하여 실행

@app.route("/") # 사용자에게 ( ) 에 있는 경로를 안내 해준다고 생각하면 쉬움
def show():
    while 1:
        min = now.tm_min
        if min != min:
            db.update_tables()
        return db.read_tables()
