import os 
import aiomysql
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

MYSQL_CONFIG = {
    k.replace("MYSQL_", ""): v for k, v in os.environ.items() if "MYSQL_" in k
}

print(MYSQL_CONFIG)


async def connect_to_db(app: FastAPI) -> None:

    """
        This function is used to connect the application with Mysql DB. 
        and then keep the global connetion into the `app.state.db`
    """
    app.state.db = await aiomysql.create_pool(**MYSQL_CONFIG)
    print("connection complete")


async def close_db_connection(app: FastAPI) -> None:
    """
        This function is used for closing the global DB connection 
    Args:
        app (FastAPI): Receives the app
    """
    app.state.db.close()
    print("connection closed")