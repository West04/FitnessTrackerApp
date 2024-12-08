from dotenv import load_dotenv
import os

load_dotenv()

testing = os.environ.get('TEST')

print(testing)
