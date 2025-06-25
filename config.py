from dotenv import load_dotenv
import os
load_dotenv()   # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from os.environ or
# os.getenv) as if they came from the actual environment.

TOKEN:str = os.getenv("TOKEN")
CMC_APL_KEY="9233a0a2-78bb-45ec-8c8d-b4119a74c3be7"