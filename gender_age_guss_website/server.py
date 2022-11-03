from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/home/guess/<name>')
def show_result(name: str) -> None:
    url_gender = f"https://api.genderize.io?name={name}"
    url_age =f"https://api.agify.io?name={name}"
    gender_data = requests.get(url_gender)
    age_data = requests.get(url_age)
    gender_user = gender_data.json()["gender"]
    age_user = age_data.json()["age"]
    if gender_user == "male" and int(age_user) > 50:
        return render_template('index1.html', name_user=name, gender=gender_user, age=age_user, gender_gif="https://media.giphy.com/media/ZjKPPIMAJ56UM/giphy.gif", age_gif="https://media.giphy.com/media/gv5JHx4troBPHOobKW/giphy.gif")
    elif gender_user == "male" and int(age_user) <= 50:
        return render_template('index1.html', name_user=name, gender=gender_user, age=age_user, gender_gif="https://media.giphy.com/media/ZjKPPIMAJ56UM/giphy.gif", age_gif="https://media.giphy.com/media/Kv4RBakx16vVifmjr6/giphy.gif")
    elif gender_user == "female" and int(age_user) > 50:
        return render_template('index1.html', name_user=name, gender=gender_user, age=age_user, gender_gif="https://media.giphy.com/media/3oKIPyRuDfitoVWPWE/giphy.gif", age_gif="https://media.giphy.com/media/akUKPkS4Bz7xc7jKTx/giphy.gif")
    elif gender_user == "female" and int(age_user) <= 50:
        return render_template('index1.html', name_user=name, gender=gender_user, age=age_user, gender_gif="https://media.giphy.com/media/3oKIPyRuDfitoVWPWE/giphy.gif", age_gif="https://giphy.com/clips/AnimationOnFOX-the-simpsons-fox-foxtv-qTG5qaFim8X9cw09SH")
if __name__ == "__main__":
    app.run(debug=True)
