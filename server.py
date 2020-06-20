from flask import Flask, render_template, url_for, request, redirect, flash
import requests
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def name():
	return render_template('index.html')

@app.route('/index')
def nam():
	return render_template('index.html')

@app.route('/message')
def names():
	return render_template('message.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/submit_form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data = request.form.to_dict()

        info = trans(data)
        return render_template('message.html', value=info)
    else:
    	return 'bad'

def trans(data):	
	url = "https://sandbox.wallets.africa/transfer/bank/account"
	payload = "{\r\n    \"SecretKey\": \"ir6r2cblaj0i\",\r\n    \"BankCode\": \"058\",\r\n    \"AccountNumber\": \"0116477747\",\r\n    \"AccountName\": \"Eduvie Agada\",\r\n    \"TransactionReference\": \"9821358010\",\r\n    \"Amount\": 10,\r\n    \"Narration\": \"test narration\"\r\n}"
	headers = {
		"Authorization": "Bearer uvjqzm5xl6bw",
	    "Content-Type": "application/json"
	}
	response = requests.request("POST", url, headers=headers, data = data)
	message = response.text.encode('utf8')
	a = json.loads(message)
	info = a["Message"]
	return info
