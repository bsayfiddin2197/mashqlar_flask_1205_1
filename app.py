from flask import Flask, render_template


app = Flask(__name__)

title = "kitoblar olami"

@app.route('/')
def home():
    return render_template('index.html', title=title)


book_name = "Python"
year = 2025

@app.route('/books')
def book():
    return render_template('books.html', book_name=book_name, year=year)


author_name = "Aliyev"

@app.route('/author')
def athor():
    return render_template('author.html', author_name=author_name)



if __name__ == '__main__':
    app.run(debug=True)
