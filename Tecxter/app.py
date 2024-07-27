from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    courses_list = [
        {'name': 'Python for Beginners', 'description': 'An introductory course to Python programming.'},
        {'name': 'Web Development with Flask', 'description': 'Learn how to build web applications using Flask.'},
        {'name': 'Data Analysis with Pandas', 'description': 'A course on data analysis using the Pandas library.'},
        {'name': 'Introduction to Machine Learning', 'description': 'A beginner\'s guide to machine learning concepts and techniques.'}
    ]
    return render_template('courses.html', courses=courses_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
