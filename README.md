# poe-api-cli

Poe-api-cli is an easy-to-use interface for [poe-api](https://github.com/ading2210/poe-api), a reverse-engineered API wrapper for Quora's Poe. With poe-api-cli, you can freely access OpenAI's ChatGPT, GPT-4, and Antropic's Claude.

For more information and help, please visit [poe-api's documentation](https://github.com/ading2210/poe-api#python-poe-api).

## Features

- The `token` environment variable is required used in poe-api-cli. If the variable is not set, poe-api-cli will prompt you to input it.
- Automatically fetches and prints the available bots and asks you to select which one you want to use.
- Use the following commands in the "Enter prompt" field:

    - `/clear`: Clears the conversation history.
    - `/changebot`: Allows you to switch between different available bots.
    - `/purge`: Deletes all conversation history.

## Usage

![usage](https://user-images.githubusercontent.com/54255074/236327161-475d07c4-c654-4ef7-a360-268d2685590a.gif)

[![Run on Repl.it](https://replit.com/badge/github/riolubruh/poe-api-cli)](https://replit.com/new/github/riolubruh/poe-api-cli)

## Conclusion

poe-api-cli is a straightforward tool for interacting with OpenAI's and Antropic's language models. By utilizing poe-api, you can quickly and easily access powerful AI chatbots without needing to set up complex API wrappers.
