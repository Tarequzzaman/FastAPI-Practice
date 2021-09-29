import os 
import aiomysql
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

MYSQL_CONFIG = {
    k.replace("MYSQL_", ""): v for k, v in os.environ.items() if "MYSQL_" in k
}

async def connect_to_db(app: FastAPI) -> None:
    app.state.db = await aiomysql.create_pool(**MYSQL_CONFIG)
    print("connection complete")

async def close_db_connection(app: FastAPI) -> None:
    app.state.db.close()
    print("connection closed")
