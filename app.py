from flask import Flask
# creating an object of flask which is initialized with name
app=Flask(__name__)

# home page/main page
@app.route("/")
def hello_world():
    return "hello, world"

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)