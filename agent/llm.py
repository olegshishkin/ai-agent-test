import os
from getpass import getpass

from dotenv import load_dotenv
from langchain_gigachat import GigaChat

load_dotenv()

if "GIGACHAT_CREDENTIALS" not in os.environ:
    os.environ["GIGACHAT_CREDENTIALS"] = getpass()

llm = GigaChat(
        model="GigaChat-Max",
        scope="GIGACHAT_API_PERS",
        verify_ssl_certs=False,
        temperature=0
)
