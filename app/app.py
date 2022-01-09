# sample application
from flask import Flask

app = Flask(__name__)
@app.route('/')
def basic_route():
  return 'Just a basic route, nothing here!';

if __name__ == '__main__':
  app.run()
