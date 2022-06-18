from flask import Flask

app=Flask(__name__)

@app.route("",method=["POST","GET"])
def fun():
    return "hello naveen"


if __name__ == "__main__":
    app.run()