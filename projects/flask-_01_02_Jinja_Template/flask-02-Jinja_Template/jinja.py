from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def head():
    number1 = 42
    number2 = 73
    return render_template("index.html", number1=number1, number2=number2)


@app.route('/sum')
def number():
    num1 = 10
    num2 = 20
    sum = num1 + num2
    return render_template("body.html", num1=num1, num2=num2, sum=sum)


if __name__ == "__main__":
    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)
