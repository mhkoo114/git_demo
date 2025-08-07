from flask import Flask, request

app = Flask(__name__)

# "/index?age=18&pwd=100"
@app.route("/index", methods=['POST','GET'])
def index():
    age = request.args.get("age")
    pwd = request.args.get("pwd")
    print(age, pwd)

    xx = request.form.get("xx")
    yy = request.form.get("yy")
    print(xx, yy)

    return "Success"

@app.route("/home")
def home():
    return "home page"

if __name__ == "__main__":
    app.run(debug=True)