from flask import Flask,request



app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    a = request.json.get("a", 0)
    b = request.json.get("b", 0)
    return str(a+b)

    #data = request.json
    #a = data['b']
    #b = data['b']
    #return str(a+b)

@app.route("/add_get", methods=["GET"])
def add_get():
    a = request.args.get("a")
    b = request.args.get("b")

    return str(int(a)+int(b))

if __name__ == "__main__":
    app.run(debug=True,port=5001)