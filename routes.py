from biblios import app

@app.route("/")
def index():
    return "Welcome page and menu"
 
@app.route("/newbook")
def hello():
    return "New book adding here"
 
@app.route("/books")
def members():
    return "All books here!"
 
@app.route("/books/<int:id>/")
def getBook(id):
    return "Book number: " + str(id)