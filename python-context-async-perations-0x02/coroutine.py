import asyncio

async def fetch_data(delay, id):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(delay)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    task1 = asyncio.create_task(fetch_data(2, 1))
    task2 = asyncio.create_task(fetch_data(2, 2))
    task3 = asyncio.create_task(fetch_data(2, 3))

    results = await asyncio.gather(task1, task2, task3)

    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())