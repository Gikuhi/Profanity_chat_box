from flask import Flask, render_template, request, jsonify
# from profanity_check import predict_prob

app = Flask(__name__)

# Simple profanity filter
profanity_list = ['mbwa', 'mafi' , 'mihadarati', 'alcohol']

banned_users = set()


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    username = request.form['username']

    # Check for profanity in the message
    for word in profanity_list:
        if word in user_message.lower():
            banned_users.add(username)
            return jsonify({'success': False, 'message': 'Profanity detected. You are banned.'})

    return jsonify({'success': True, 'message': user_message, 'username': username})


@app.route('/get_banned_users', methods=['GET'])
def get_banned_users():
    return jsonify(list(banned_users))


if __name__ == '__main__':
    app.run(debug=True)
