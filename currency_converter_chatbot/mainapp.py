from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()

    source_curr = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    tar_curr = data['queryResult']['parameters']['currency-name']

    print("Source Currency:", source_curr)
    print("Amount:", amount)
    print("Target Currency:", tar_curr)

    try:
        conversion_factor = fetch_conversion_factor(source_curr, tar_curr)
        final_amount = amount * conversion_factor
        final_amount = round(final_amount,2)
        print("Converted Amount:", final_amount)

        response = {
            'fulfillmentText': "{} {} is {} {}".format(amount, source_curr, final_amount, tar_curr)
        }
        return jsonify(response)
    except Exception as e:
        print("Error:", e)
        return jsonify({'fulfillmentText': "Error occurred while processing the request."})


def fetch_conversion_factor(source, target):
    url = f"https://v6.exchangerate-api.com/v6/40db387fca4f04a2889f2808/pair/{source}/{target}"
    response = requests.get(url)
    response_data = response.json()

    if response.status_code == 200 and 'conversion_rate' in response_data:
        return response_data['conversion_rate']
    else:
        raise ValueError("Invalid response from exchange rate API")


if __name__ == "__main__":
    app.run(debug=True)
