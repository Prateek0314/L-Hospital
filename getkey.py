import os
from dotenv import load_dotenv
def uniquekey():
    load_dotenv()
    unikey=os.getenv('key')
    return unikey