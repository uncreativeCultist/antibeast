from email.mime import image, text
import re
import subprocess
from urllib.parse import urlparse
import discord
from PIL import Image
import pytesseract
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('ANTIBEAST_TOKEN')
if token is None:
    print('You forgot to add the bot token to the "ANTIBEAST_TOKEN" environment variable.')
    raise SystemExit(1)

img_exts = (".png", ".jpg", ".jpeg", ".webp") # if some insane fuck uses a bitmap image to bypass this istg
def get_image_urls(message):
    urls = []

    for attachment in message.attachments:
        urls.append(attachment.url)
    # fuck this
    for match in re.findall(r"https?://\S+", message.content):
        clean_url = match.rstrip(".,;:!?\"")
        path = urlparse(clean_url).path.lower()
        if any(path.endswith(ext) for ext in img_exts):
            urls.append(clean_url)

    return urls

# and thus begins the stolen code (https://discordpy.readthedocs.io/en/stable/quickstart.html)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    rating=0
    timedout=0
    uid = message.author.id
    for image_url in get_image_urls(message):
        subprocess.run(["curl", f"{image_url}", "-o", f"{uid}"]) # this is a little better ig
        image = Image.open(f"{uid}")
        gray_image = image.convert("L")
        text = pytesseract.image_to_string(gray_image)
        clean_text = text.replace("\x0c", "").strip()
        nice_text=clean_text.lower()
        if "mrbeast" in nice_text:
            rating = rating+1
        if "joined april" in nice_text:
            rating = rating+1
        if "follow me for a" in nice_text:
            rating = rating+1
        if "beast games" in nice_text:
            rating = rating+1
        if "crypto" in nice_text:
            rating = rating+2
        if "media personality" in nice_text:
            rating = rating+1
        if "kasowin" in nice_text:
            rating = rating+2
        if "lacewin" in nice_text:
            rating = rating+2
        if "haveawin" in nice_text:
            rating = rating+2
        if "vip-club" in nice_text:
            rating = rating+2
        if "vyro" in nice_text:
            rating = rating+1
        if "gambwex" in nice_text:
            rating = rating+2
        if "bonus" in nice_text:
            rating = rating+1
        if "withdraw" in nice_text:
            rating = rating+1
        if "reward" in nice_text:
            rating = rating+1

        if rating > 5:
            duration = datetime.timedelta(minutes=30) # i dont like deltatime
            await message.author.timeout(duration, reason="MrBeast Scam Bot (AntiBeast)")
            timedout=1

        if rating > 4:
            if timedout!=1:
                duration = datetime.timedelta(minutes=10) # i dont like deltatime
                await message.author.timeout(duration, reason="MrBeast Scam Bot (AntiBeast)")
                timedout=1

        if rating > 3:
            if timedout!=1:
                duration = datetime.timedelta(minutes=1) # i dont like deltatime
                await message.author.timeout(duration, reason="MrBeast Scam Bot (AntiBeast)")

        if rating > 2:
            user = await client.fetch_user(uid)
            await user.send(f'Hi there! It looks like you tried to post one of those crypto scam images in "{message.guild}". \nIf this is incorrect, please contact the mod team <3\n\nIf you **did not** attempt to send an image in "{message.guild}" just now, **change your password, your account has been compromised.**')
            await message.delete()

        subprocess.run(["rm", f"{uid}"])
        
client.run(token)
