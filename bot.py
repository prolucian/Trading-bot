import asyncio, os

async def main():
    while True:
        print("Scanning markets...")
        await asyncio.sleep(int(os.getenv("SCAN_INTERVAL", 120)))

if __name__ == "__main__":
    asyncio.run(main())
