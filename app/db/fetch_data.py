import aiomysql


async def fetch(pool, query):
    """ The fetch function is responsible for fetching the data from the database. It receives two args.

    Args:
        pool (Connection):  The pool is the DB connection pool paramiter 
        query (String): The query parms is actually the raw query string 

    Returns:
        result [list]: The result is a list which contains one or multiple object data fetched from Database 
    """
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            result = await cur.fetchall()
            return result