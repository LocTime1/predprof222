from flask import Flask, render_template, request
from parsing import raschet
from db_work import get_info_day

app = Flask(__name__)


@app.route("/")
def getdate():

    return render_template("create_house.html", datess=d)


@app.route("/housedone", methods=["POST", "GET"])
def create_house():
    date1 = request.form.get('lll')
    lst = get_info_day(date1)
    d = raschet(lst)

    print(lst)
    print(d)
    return render_template("create_house2.html", lst=lst, date1=date1, d=d)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
