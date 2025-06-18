from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Pagamento recebido:")
    print(json.dumps(data, indent=2))

    if data.get("payment_status") in ("paid", "confirmed"):
        print("✅ Pagamento confirmado!")
        print("Order ID:", data.get("order_id"))
    return 'OK', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
