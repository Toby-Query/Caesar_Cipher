from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cipher', methods=['POST'])
def cipher():
    data = request.json
    text = data.get('text', '')
    shift = data.get('shift', 0)
    encrypted_text = caesar_cipher(text, shift)
    return jsonify(result=encrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
