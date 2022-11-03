from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def hello_world():
    return '<h1> Guess a number between 0 and 9 </h1> <img src="https://media.giphy.com/media/SyP24XyDVsavNPECoR/giphy.gif" alt="start image ">'
    print(random_number)


@app.route('/<num>')
def show_result(num: int) -> None:
    if int(num) > random_number and int(num) < 10:
        return '<h1 style="color:red;" >  Your guess is to high<h1> <img src ="https://media.giphy.com/media/YNzg8rHljnqyoSeDqV/giphy.gif">'
    elif int(num) < random_number and int(num) > -1:
         return '<h1 style="color:blue;">  Your guess is to low<h1> <img src ="https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif">'
    elif int(num) == random_number:
         return '<h1 style="color:green;">  Your guess is good!!<h1> <img src ="https://media.giphy.com/media/3KC2jD2QcBOSc/giphy.gif">'
    else:
         return '<h1 style="color:red;">  you are try to hack liron higher lower site? <h1> <img src ="https://media.giphy.com/media/85y2gsgMQMByfpJzoN/giphy.gif">'



if __name__ == "__main__":
    app.run(debug=True)
