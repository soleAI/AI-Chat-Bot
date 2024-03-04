from fastapi import FastAPI
from services.openai import OpenAIService
from keys.key import open_ai_key
import os

os.environ['OPENAI_API_KEY'] = open_ai_key
open_ai = OpenAIService(temp=0.6)

app = FastAPI()
