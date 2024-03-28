from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/travis", methods=["POST"])
def webhook():
  # Check if the request has JSON data
  if request.is_json:
    # Get the JSON data
    data = request.get_json()
    print("Webhook request received!")
    # Pretty print the JSON data for better readability
    print(json.dumps(data, indent=4))
  else:
    print("Request is not JSON format")
    return "Please send JSON data", 400  # Bad request

  return "Success", 200

if __name__ == "__main__":
  app.run(debug=True)
