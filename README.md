# Into to Python

## Healthy Gamer Discord 2022

## Setup

### Python

There are several development environments to choose from, but Visual Studio Code is one of the most popular. The latest instructions can be found here: [https://code.visualstudio.com/docs/datascience/overview](https://code.visualstudio.com/docs/datascience/overview)

You will need:

- Python 3 installed on your machine
- Python extension in Visual Studio Code
- (For the tutorial pages) Jupyter extension for Visual Studio Code. Github will allow you to view the files in the repository but not run the code blocks.

### Discord

If you want to run the bot you will need a dev API key and a Discord server to test on.

1. At [https://discord.com/developers](https://discord.com/developers) create a new application.
2. On the General Information page for your new app you'll be able to get your App ID and public key.
3. In the left nav menu open the Bot tab.
4. Choose add bot user and confirm.
5. (Optional) Turn off public bot if you don't want other people to add the bot to their servers.
6. Get your token and add it to the .env file so that you can add your bot to servers.
7. Under Permissions -> Text Permissions add "Send Messages".

#### Add the bot to your server

1. In the Dev portal choose your new app and go to the OAUTH option.
2. Navigate to the Generate Link tab.
3. Under scope add 'bot' scope.
4. Under Bot Permissions add Text Permissions -> "Send Messages".
5. Copy the link at the bottom of the page and open it in a new browser window.
6. Choose the server you want to add the bot to and complete authorization.
