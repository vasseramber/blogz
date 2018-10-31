from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildablog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(2000))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/main.blog', methods=['POST', 'GET'])
def index():   
    return render_template('main_blog.html') 

@app.route('/new_entry', methods=['POST', 'GET'])
def entry():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        print(body)
        new_entry = Blog(title, body) 
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/blog')
    
    return render_template('new_entry.html')

@app.route('/blog') 
def blog():
    blog_id = request.args.get('id')

    if blog_id:
        blog_id = request.args.get('id')
        blog = Blog.query.get(blog_id)

        return render_template('blog.html', blog=blog)

   
    taste = Blog.query.all()

    return render_template('main_blog.html', blog=taste)


if __name__ == '__main__':
    app.run()