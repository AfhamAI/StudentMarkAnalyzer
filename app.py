from flask import Flask , render_template , request

app = Flask(__name__)


def gradeFunc(x):
    if x >= 90:
        return "A+"
    elif x >= 80:
        return "A"
    elif x >= 70:
        return "B"
    elif x >= 60:
        return "C"
    else:
        return "Fail"
    
def remarkFunc(x):
    if x >= 90:
        return "Outstanding"
    elif x >= 80:
        return "Excellent"
    elif x >= 70:
        return "Good"
    elif x >= 60:
        return "Average"
    else:
        return "Need improvement"
    


@app.route('/', methods = ['POST' , 'GET'])

def home():
    if request.method == "POST":
        name = request.form.get('name')
        mathMark = int(request.form.get('math'))
        englishMark = int(request.form.get('english'))
        scienceMark = int(request.form.get('science'))
        Total = mathMark + englishMark + scienceMark
        avg = round(Total/3 ,2)
        grade = gradeFunc(avg)
        remark = remarkFunc(avg)
        if mathMark < 0 or englishMark < 0 or scienceMark < 0:
            return "Marks Cant Be Less Than Zero"
        if mathMark > 100 or englishMark > 100 or scienceMark > 100:
            return "Marks Cant Be Above 100"
        if avg >= 60:
            status = "Pass"
            color = "rgba(20, 220, 87, 0.647)"
        else:
            status = "Fail"
            color = "rgba(220, 20, 20, 0.647)"
        return render_template('result.html', name = name , mathMark = mathMark , scienceMark = scienceMark , englishMark = englishMark, avg = avg , Total = Total , grade = grade , remark = remark, color = color, status = status)
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')
    


if __name__ == "__main__":
    app.run(debug=True)