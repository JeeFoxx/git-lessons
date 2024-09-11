from dotenv import load_dotenv
import os
load_dotenv()
login=os.getenv('LOGIN')
print(login)