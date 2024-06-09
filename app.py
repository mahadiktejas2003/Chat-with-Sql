# from flask import Flask, jsonify
# from chatSql import ChatWithSql
# app = Flask(__name__)
# obj = ChatWithSql("root","","localhost","ahi_database")
# @app.route('/send-message', methods=['GET'])
# def send_message():
#     # message = "Hello, this is a message from the Flask API!"
#     message = obj.message("How many rows do we have in cattle table ?")
#     return jsonify({"message": message})

# if __name__ == '__main__':
#     app.run(debug=True)
# #original project file


#NEW: 
from flask import Flask, render_template, request, jsonify
import pymysql.cursors
from chatSql import ChatWithSql

app = Flask(__name__)

# Initialize ChatWithSql object
obj = ChatWithSql("root", "", "localhost", "ahi_database")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.json.get('message')

    if not message:
        return jsonify({'error': 'Message field is required.'}), 400

    try:
        response = obj.message(message)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
