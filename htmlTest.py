from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


##
# Get post request page.
@app.route('/Rick-N-Morty', methods=['POST'])
def generate():
    return jsonify({'0': [['Rick', 'hey'], ['Morty', 'What?'], ['Jerry', '매롱'], ['Rick', 'stop'], ['Beth', "What? What is this? I don't wanna die! stop!"], ['Smith', "That's crazy"]]})


##
# Main page.
@app.route('/')
def main():
    return render_template('main.html'), 200


if __name__ == '__main__':
    from waitress import serve
    serve(app, port=80, host='0.0.0.0')