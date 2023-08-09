from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    input_text = request.json.get('inputText')
    # ここで文字の確認や検証を行うことができます。
    # 簡単な例として、指定した文字が"hello"であるかを確認します。
    if input_text == "hello":
        return jsonify({"result": "正解"})
    else:
        return jsonify({"result": "不正解"})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9000)
