import asyncio

async def brew(name):
  print(f"brewing {name}...")
  await asyncio.sleep(2)
  print(f"{name} is ready")


async def main():
  await asyncio.gather(
    brew("Masala chai"),
    brew("Ginger chai"),
    brew("Lemon chai")
  )


asyncio.run(main())