from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print("Received Alert:", data)
        return '', 200
    else:
        return 'Webhook server is online', 200

if __name__ == '__main__':
    app.run()