from flask import Flask, request
import logging

app = Flask(__name__)

# Logging aktivieren
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json(force=True, silent=True)
        app.logger.info(f"📩 Received POST: {data}")
        return '', 200
    else:
        return 'Webhook server is online', 200

if __name__ == '__main__':
    app.run()