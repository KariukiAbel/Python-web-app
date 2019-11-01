# importing the flask class object from the flask library
from flask import Flask

# instanciating the flask class. the  __name__ gets the name of the python script. Python assigns 
# the name __main__ to the python script
app = Flask(__name__)

#url to view the website. The slash means the home page
@app.route('/')
def home():
    return "Web content goes here!"

# if __name__ == "__.main__":
#     app.run(debug = True)


if __name__ == '__main__':
    app.run(debug=True)