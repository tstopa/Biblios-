from biblios import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), index=True, unique=True)
    title = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Book {}>'.format(self.id)   