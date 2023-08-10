from flask import Flask, render_template, request, redirect, send_file
from math import trunc
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        equation = request.form.get("equation")
        if equation[len(equation) - 1] == '=':
            equation = equation[:-1]
        new_equation = parse(equation)
        if not new_equation:
            return render_template("index.html", answer="Error")
        try:
            num1 = float(new_equation[0])
        except TypeError:
            return render_template("index.html", answer="Error")
        try:
            operator = str(new_equation[1])
        except TypeError:
            return render_template("index.html", answer="Error")
        try:
            num2 = float(new_equation[2])
        except TypeError:
            return render_template("index.html", answer="Error")
        real_num1 = new_equation[0]
        real_operator = new_equation[1]
        real_num2 = new_equation[2]
        submit_op = new_equation[3]
        if real_operator != '+' and real_operator != '-' and real_operator != '*' and real_operator != '/':
            return render_template("index.html", answer="Error")
        if real_operator == '/' and real_num2 == 0:
            return render_template("index.html", answer="Error")
        answer = calculate(num1, operator, num2)
        if answer == int(answer):
            answer = trunc(answer)
        else:
            answer = round(answer, 3)

        return render_template("index.html", num1=real_num1, num2=real_num2, operator=real_operator, answer=answer, submit_op=submit_op)
    else:
        return render_template("index.html")
def parse(equation):
    negative = False
    submit_op = ''
    index = None
    if equation[0] == '-':
        negative = True
        equation = equation[1:]
    if equation[len(equation) - 1] in ('+', '-', '*', '/'):
        submit_op += (equation[len(equation) - 1])
        equation = equation[:-1]
    for operator in ('+', '-', '*', '/'):
        try:
            index = equation.index(operator)
            break
        except ValueError:
            continue
    if not index:
        print("yes")
        return None
    try:
        num1 = float(equation[:index])
    except ValueError:
        return render_template("index.html", answer="Error")
    try:
        operator = equation[index]
    except ValueError:
        return render_template("index.html", answer="Error")
    try:
        num2 = float(equation[index+1:])
    except ValueError:
        return render_template("index.html", answer="Error")
    if negative:
        num1 *= -1
    return (num1,  operator, num2, submit_op)


def calculate(num1, op, num2):
    """
    Your task is to make code that should take two floats, num1, and num2 and an str, op

    Op can be anything. If op is one of the 4 fundimental functions ('+', '-', '*', '/'), you should return the answer accordingly
    """
    raise NotImplementedError


if __name__ == "__main__":
    app.run()