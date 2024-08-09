from flask_restful import Resource, Api
from backend.GA.llm_setup import *
from backend.GA.lecture_database import *
from flask import Flask, render_template, request, jsonify, Blueprint, url_for

# Initialize
app = Flask(__name__)

#Logout
@app.route('/api/logout' , methods=['DELETE'])
def logout_user():

    """
    ---
    delete:
      summary: Clear All User Data
      description: Clears all of the current users history and data
      responses:
        200:
          description: Success
    """       
    return render_template('starter-page.html'),200


@app.route('/', methods=['GET'])
def index():

    """
    ---
    get:
      summary: Home Page
      description: Route for home page
      responses:
        200:
          description: Success
    """       
    return render_template('starter-page.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():

    """
    ---
    get:
      summary: Dashboard
      description: Route for dashboard
      responses:
        200:
          description: Success
    """       
    return render_template('dashboard_copy.html')


@app.route('/dashboard/chatbot', methods=['GET'])
def chatbot():
       
    """
    ---
    get:
      summary: Central Chatbot 
      description: Route for chatbot interface
      responses:
        200:
          description: Success
    """           
    return render_template('chatbot.html'),200

# Register Blueprints
with app.app_context():
    from backend.lecture_routes import lec
    from backend.assignments import assgn
    from backend.chat_routes import chatt
    app.register_blueprint(lec)
    app.register_blueprint(assgn)
    app.register_blueprint(chatt)
    print(app.url_map)


if __name__ == '__main__':
    app.run(debug=True)