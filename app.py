from flask import Flask, render_template, request

app = Flask(__name__)

def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

@app.route('/', methods=['GET', 'POST'])
def index():
    transformed_text = None
    if request.method == 'POST':
        text_to_transform = request.form['text']
        transformed_text = rot13(text_to_transform)
    
    return render_template('index.html', transformed_text=transformed_text)

if __name__ == '__main__':
    app.run(debug=True)