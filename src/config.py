from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    TOKEN = os.getenv("DISCORD_TOKEN")
    PREFIX = "/"
    intents = disnake.Intents.all()