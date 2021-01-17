from flask import Flask

app = Flask(__name__) ## 플라스크를 생성하고 app 변수에 flask 초기화 하여 실행
@app.route("/") # 사용자에게 ( ) 에 있는 경로를 안내 해준다고 생각하면 쉬움
def test():
    return "test"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=80)

