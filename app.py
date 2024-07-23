from flask import Flask, render_template, request

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.get('/')
def index():
  return render_template('index.html')


@app.get('/about')
def about():
  return render_template('about.html', location=request.args.get('location'), title='About')


@app.get('/hello')
def hello():
  return render_template('hello.html', name=request.args.get('name'))

@app.errorhandler(404)
def handle_404(e):
    return render_template('status_404.html'), 404


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)