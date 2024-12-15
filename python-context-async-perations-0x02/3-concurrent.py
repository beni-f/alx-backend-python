import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect('user.db') as db:
        print("Fetching all users...")
        async with db.execute("SELECT * FROM users") as cursor:
            result  = await cursor.fetchall()
            return result


async def async_fetch_older_users():
    async with aiosqlite.connect('user.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            print("Fetching older users...")
            result = await cursor.fetchall()
            return result

async def fetch_concurrently():
    results = await asyncio.gather(async_fetch_users(), async_fetch_older_users())

    for result in results:
        print(result)

asyncio.run(fetch_concurrently())