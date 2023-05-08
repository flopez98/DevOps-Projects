# OpenAI (ChatGPT) Python Code Generator

This Python script uses OpenAI's API to generate Python code based on a user-provided prompt. The generated code is then saved to a file.

## Requirements

- Python 3.x
- The `requests` library (can be installed via pip)
- An OpenAI API key. Instructions for obtaining one can be found [here](https://beta.openai.com/docs/api-reference/authentication).

## Installation

1. Clone or download this repository to your local machine.
2. Install the required libraries using pip:
   ```
   pip install requests
   ```
3. Follow the instructions in the "Requirements" section to obtain an OpenAI API key.
4. Create a file called `api_key.txt` in the same directory as the script and paste your API key into it.
5. Run the script from the command line:
   ```
   python openai_code_generator.py "your prompt here"
   ```

## Usage

The script takes a single argument, which is the prompt to send to the OpenAI API. This should be a short sentence describing what the Python code should do. For example:
```
python openai_code_generator.py "sort a list of integers"
```

The generated Python code will be saved to a file in the same directory as the script. You will be prompted to enter a name for the file.

By default, the script uses the `text-davinci-003` model to generate the code, and sets the `max_tokens` parameter to 500 and the `temperature` parameter to 0.5. You can modify these values by editing the `request_data` dictionary in the script.

### Running the script

To run the script, follow these steps:

1. Clone or download this repository to your local machine.
2. Install the required libraries using pip:
   ```
   pip install requests
   ```
3. Follow the instructions in the "Requirements" section to obtain an OpenAI API key.
4. Create a file called `api_key.txt` in the same directory as the script and paste your API key into it.
5. Run the script from the command line:
   ```
   python openai_code_generator.py "your prompt here"
   ```