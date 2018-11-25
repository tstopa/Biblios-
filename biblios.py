from flask import Flask, render_template, request, flash, url_for, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#App properties:
app.debug = False

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   author = db.Column(db.String(100), unique=False, nullable=False)
   title = db.Column(db.String(200), unique=False, nullable=False)

@app.route("/")
def all_books():
    return render_template('report.html', books = Book.query.all())

@app.route("/newbook", methods = ['GET', 'POST'])
def newbook():
    if request.method == 'POST':
      if not request.form['author'] or not request.form['title']:
         flash('Please enter all the fields', 'error')
      else:
         newbook = Book(author=request.form['author'], title=request.form['title'])
         db.session.add(newbook)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('all_books'))
    return render_template('newbook.html')

@app.route("/books/<int:id>/")
def getBook(id):
    book = {'id': id}
    return render_template('book.html', book=book)

#Start: 
if __name__ == "__main__":
    db.create_all()
    app.run(host='127.0.0.1', port=80)
