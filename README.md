<img align="right" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg">

# Mistral AI Telegram Bot

mistral-ai-telegram-bot - A simple telegram bot that answer using Mistral AI

```
        .__          __                .__                   .__            __         .__                                               ___.           __   
  _____ |__| _______/  |_____________  |  |           _____  |__|         _/  |_  ____ |  |   ____   ________________    _____           \_ |__   _____/  |_ 
 /     \|  |/  ___/\   __\_  __ \__  \ |  |    ______ \__  \ |  |  ______ \   __\/ __ \|  | _/ __ \ / ___\_  __ \__  \  /     \   ______  | __ \ /  _ \   __\
|  Y Y  \  |\___ \  |  |  |  | \// __ \|  |__ /_____/  / __ \|  | /_____/  |  | \  ___/|  |_\  ___// /_/  >  | \// __ \|  Y Y  \ /_____/  | \_\ (  <_> )  |  
|__|_|  /__/____  > |__|  |__|  (____  /____/         (____  /__|          |__|  \___  >____/\___  >___  /|__|  (____  /__|_|  /          |___  /\____/|__|  
      \/        \/                   \/                    \/                        \/          \/_____/            \/      \/               \/             

```

## Description

**mistral-ai-telegram-bot** is a simple telegram bot that answer using [Mistral AI](https://mistral.ai/). For the sake of simplicity, the model used is [Mistral 7B](https://docs.mistral.ai/models/mistral-7b-0-3), which is public available and smaller to download (4Gb instead of 26Gb, from some more complex models like [Mixtral 8x7B](https://docs.mistral.ai/models/mixtral-8x7b-0-1)).

## Usage

### Before you Start

You will need a valid [Telegram](https://telegram.org/) account. It will be necessary to create and obtain a Telegram Bot API key.

#### Obtaining a Telegram Bot API Key

To create a Telegram bot and obtain an API key, open Telegram App, using your mobile device or desktop application.
Next, search for the bot named `@BotFather`. This is the official bot for creating and managing other bots. Type `/newbot` and follow the instructions.

After successfully creating your bot, the BotFather will provide you with an API token. This token is essential for accessing the Telegram Bot API.

> Keep your API token secure. Do not share it publicly, as it allows control over your bot.

### Installation

Please, certify to have all the [requirements](#requirements) installed. Then, clone this repository.

### Running

The easier way to run this bot is using [docker compose plug-in](https://docs.docker.com/compose/). But first, create a file `telegram-bot/.env` adding your API key to the variable `TELEGRAM_API_TOKEN`. The file content should be similar to this:

```bash
TELEGRAM_API_TOKEN="insert the api token here"	# add your telegram API token inside the double quotes
```

Now, enter the root path where you cloned this repository and bring your stack up with:

```bash
cd mistral-ai-telegram-bot/
docker compose up --detach
```

In the first execution, you must download the [Mistral 7B](https://docs.mistral.ai/models/mistral-7b-0-3) model. This is a one-time only execution.

```bash
cd ollama/
mise run pull-mistral
```

Make sure that you have [trusted mise first](https://mise.jdx.dev/cli/trust.html). Alternatively, you can run:

```bash
curl --request POST http://localhost:11434/api/pull --data '{"name": "mistral"}'
```

### Have Fun!

Now, find your bot on Telegram and start asking questions!

![Mistral AI Telegram Bot](https://github.com/lfromanini/mistral-ai-telegram-bot/blob/main/docs/screenshots/telegram-bot.png?raw=true)

Mine is running [here](https://t.me/mistral_ai_telegram_bot), but I keep my services down while I'm not using it, so chances are it will not reply to you.

#### Requirements

* [docker](https://hub.docker.com/)
* [docker compose plug-in](https://docs.docker.com/compose/)
* [mise-en-place](https://mise.jdx.dev/)
* A [Telegram](https://telegram.org/) account

## LICENSE

The [MIT License](https://github.com/lfromanini/mistral-ai-telegram-bot/blob/main/LICENSE) (MIT)
