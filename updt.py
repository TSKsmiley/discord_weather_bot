import os
import asyncio

os.system("rm main.py")
asyncio.sleep(1)
os.system("wget https://raw.githubusercontent.com/TSKsmiley/discord_bot/master/main.py")
asyncio.sleep(1)
os.system("python3 main.py")
