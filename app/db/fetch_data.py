import aiomysql
async def fetch(pool, query):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            result = await cur.fetchall()
            return result