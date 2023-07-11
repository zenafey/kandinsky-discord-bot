# Kandinsky discord bot
Here is tutorial and code of Kandinsky discord bot
#


# Installation

1. First we need to check that Python is installed and have 3.11 version(its important)
```
python -V
```
if running this command in command line giver error like "python is not recognized bla bla bla" or it have not 3.11 version we need to install 3.11 version from [official website](https://www.python.org/downloads/release/python-3110/)

Right result should be:
```
python -V
Python 3.11.0
```

2. Now lets clone repository with bot by command below, if git isnt installed, install [it](https://git-scm.com/downloads)
```
git clone https://github.com/yoou3-cyber/kandinsky-discord-bot
cd kandinsky-discord-bot
```

3. To install needed modules lets run this command:
```
pip install -r requirements.txt
```

4. IMPORTANT!! If you used libraries such as nextcord, disnake, discord, discord.py, DiscordUtils, etc... before, you need to uinstall them after uninstallation of them or if you didnt used them, you should run command to install py-cord:
```
pip install py-cord
```

5.After all of this actions we need to get discord api bot token:

to get it enter [Discord Application page](https://discord.com/developers/applications), create new application or use another that is exist, enter bot category and copy its token, if bot isnt created - create, save your bot token somewhere
IMPORTANT!!! All intents on discord bot page should be enabled

6. Create new file in directory `kandinsky-discord-bot` with name `.env`, content of this file should be:
```
DISCORD_TOKEN=<paste here your discord bot token instead of this text and ><>
```

7. Run bot by command:
```
python main.py
```
wait some minutes after this to sync commands

8. Enjoy bot!!!!

# How to use this command of bot?
![image](https://github.com/zenafey/kandinsky-discord-bot/assets/118455214/e3918a9a-e47f-4ae2-aab8-d37962718675)


This bot will have slash command /create that have options:
`prompt`(required) - text of what should be on picture
`style` - one of 24 styles
`scale` - scale varioable is float and can be from 1 to 20
Generation time depends on steps and scale value

# Contact
Discord tag: xeon-m#7477
Discord server: https://discord.gg/qX5dwV3HEp 
