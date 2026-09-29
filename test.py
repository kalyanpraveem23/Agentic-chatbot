import os
from dotenv import load_dotenv

load_dotenv(override=True)

print("LANGSMITH_TRACING =", os.getenv("LANGSMITH_TRACING"))
print("LANGSMITH_PROJECT =", os.getenv("LANGSMITH_PROJECT"))
print("LANGSMITH_API_KEY =", bool(os.getenv("LANGSMITH_API_KEY")))













