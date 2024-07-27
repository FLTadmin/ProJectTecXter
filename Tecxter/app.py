from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    courses_list = [
        {'name': 'Python Programming', 'description': 'An in-depth course covering Python programming fundamentals and advanced concepts. Learn to build applications and scripts using Python.'},
        {'name': 'Java', 'description': 'A comprehensive course on Java programming. Covers basic to advanced Java concepts, including object-oriented programming and Java frameworks.'},
        {'name': 'Data Engineering with AWS & Azure', 'description': 'Learn data engineering techniques using AWS and Azure platforms. Covers data storage, ETL processes, and data pipeline construction.'},
        {'name': 'SAP', 'description': 'An introduction to SAP systems and modules. Learn about SAP ERP, SAP HANA, and how to use SAP for enterprise resource planning.'}
    ]
    return render_template('courses.html', courses=courses_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
