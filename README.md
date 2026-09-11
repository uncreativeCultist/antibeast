![antibeast - rudimentary discord bot to stop crypto scams in your server](https://github.com/uncreativeCultist/antibeast/blob/9a38a5a318cd21030849f69c048cddeaf4779e79/.github/repo%20assets/antibeastpromo.png)


    
# how to use
if you can't be bothered to host antibeast yourself, you can use [my instance](https://discord.com/oauth2/authorize?client_id=1547661427521622146).  
otherwise, look below for selfhosting instructions

## hosting
this has only been tested on a linux system under a [venv](https://www.w3schools.com/python/python_virtualenv.asp), no clue if it will work properly on windows.
1. run `git clone https://github.com/uncreativeCultist/antibeast.git`
2. run `pip install -r requirements.txt`
3. set the environment variable `ANTIBEAST_TOKEN` to your discord bot token
4. run `python3 antibeast.py`  
make sure to run `git pull` frequently to get any updates for the bot.
