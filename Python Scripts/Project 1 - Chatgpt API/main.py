import requests
import argparse

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
args = parser.parse_args()

# Set the API endpoint
api_endpoint = "https://api.openai.com/v1/completions"

# Read the API key from a file
with open("api_key.txt", "r") as key:
    global api_key
    api_key = str(key.readlines())

# Set the headers and request data for the API request
request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key[2:-2],
}

request_data = {
    "model": "text-davinci-003", # The name of the OpenAI model to use
    "prompt": f"Write a python script to {args.prompt}. Privde only code, no text.", # The prompt to send to the API
    "max_tokens": 500, # The maximum number of tokens to generate
    "temperature": 0.5 # The "creativity" of the generated text (higher values = more creative)
}

# Send the API request
response = requests.post(api_endpoint, headers=request_headers, json=request_data)

# If the API request is successful, save the generated code to a file
if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(input("Write the name of your file: ") + '.py', "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")