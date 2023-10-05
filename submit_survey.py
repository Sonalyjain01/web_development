from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/page2.html', methods=['POST'])
def page2():
    name = request.form['name']
    return render_template('page2.html', name=name)

@app.route('/page3.html', methods=['POST'])
def page3():
    name = request.form['name']
    age = request.form['age']
    return render_template('page3.html', name=name, age=age)

@app.route('/submit_survey.py', methods=['POST'])
def submit_survey():
    name = request.form['name']
    age = request.form['age']
    feedback = request.form['feedback']

    # Save the data to a database or send it via email

    return "Thank you for submitting the survey!"

if __name__ == '__main__':
    app.run(debug=True)
