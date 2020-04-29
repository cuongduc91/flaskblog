from flask import Flask, render_template
app = Flask(__name__)

posts =[
    {
        'author':'Cuong Duc',
        'title':'Blog post 1',
        'content':'First Post content',
        'date_posted':'April 29, 2020'
    },
    {
        'author':'Anonymous',
        'title':'Blog post 3',
        'content':'First Post content',
        'date_posted':'April 30, 2020'
    }

]
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__ == __name__:
    app.run(debug="true")