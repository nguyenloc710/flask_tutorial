from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#
# @app.route('/')
# def hello():
#     return render_template('index.html', content = "LOC DZ", cars=["Vin", "BWV", "MEC"])

@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    return f"<H1>Hello {name}!</H1>"


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return f"<H2>Block {blog_id}<H2>"


@app.route('/admin')
def hello_admin():
    return f"<H2>Hello Admin<H2>"


if __name__ == '__main__':
    app.run(debug=True)
