# poe-api-cli

**`poe-api-cli`** is an easy-to-use interface for [poe-api](https://github.com/ading2210/poe-api), a reverse-engineered API wrapper for Quora's Poe. With poe-api-cli, you can freely access OpenAI's ChatGPT, GPT-4, Antropic's Claude, and more.

For more information and help, please visit [poe-api's documentation](https://github.com/ading2210/poe-api#python-poe-api).

## Features

- The `token` environment variable is used in poe-api-cli. If the variable is not set, poe-api-cli will prompt you to input it.
- Automatically fetches and prints the available bots and asks you to select which one you want to use.
- Use the following commands in the "Enter prompt" field:
    - `/clear`: Clears the conversation history.
    - `/changebot`: Allows you to switch between different available bots.
    - `/purge`: Deletes all conversation history.

## Usage

![usage](https://user-images.githubusercontent.com/54255074/236327161-475d07c4-c654-4ef7-a360-268d2685590a.gif)

To get started, please follow the steps below:

To get started, I recommend you visit [poe-api's documentation](https://github.com/ading2210/poe-api#finding-your-token) on how to get your token. Once done, simply run the CLI tool.

1. Clone the repository using `git clone https://github.com/riolubruh/poe-api-cli.git` or download and extract the ZIP file.
2. Open a terminal window and navigate to the project directory.
3. Install the dependencies by running `pip install -r requirements.txt`.
4. Set the `token` environment variable using `export token=YOUR_TOKEN_HERE` (on Linux/macOS) or `set token=YOUR_TOKEN_HERE` (on Windows).
5. Run the CLI tool using `python3 main.py`.

You can also try out poe-api-cli on Repl.it.

[![Run on Repl.it](https://replit.com/badge/github/riolubruh/poe-api-cli)](https://replit.com/new/github/riolubruh/poe-api-cli)

---

poe-api-cli is a straightforward tool for interacting with OpenAI's and Antropic's language models.
