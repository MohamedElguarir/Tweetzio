import requests

def send_email(name, email, message):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox06c040759620447ba8d29f6ae810ef0b.mailgun.org/messages",
		auth=("api", "2b21a99792d8532539225b7d3413a557-75cd784d-68831c23"),
		data={"from": "MOHAMED ELGUARIR <mohamed@elguarir.me>",
			"to": ["mehdi.zerdi@gmail.com", "mohaelguarir@gmail.com"],
			"subject": f"New message received from {name}",
			"text": f"name : {name}\nemail : {email}\nmessage: {message}"
	}
)