from fastapi import FastAPI
from dotenv import load_dotenv
import aiomysql
import os 
load_dotenv()

MYSQL_CONFIG = {
    k.replace("MYSQL_", ""): v for k, v in os.environ.items() if "MYSQL_" in k
}

print(MYSQL_CONFIG)


async def connect_to_db(app: FastAPI) -> None:
    
    app.state.db = await aiomysql.create_pool(**MYSQL_CONFIG)
    print(app.state.db)
    print("connection complete")


async def close_db_connection(app: FastAPI) -> None:
    print(app.state.db)
    app.state.db.close()
    print("connection closed")

