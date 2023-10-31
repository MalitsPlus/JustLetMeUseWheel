import mouse
import asyncio

def handler(event):
  if type(event).__name__ == "WheelEvent":
    if event.delta < 0:
      mouse.click(mouse.LEFT)

async def watch():
  while True:
    await asyncio.sleep(9999)

def main():
  mouse.hook(handler)
  try:
    asyncio.run(watch())
  except KeyboardInterrupt:
    print("exiting...")
  finally:
    mouse.unhook(handler)

if __name__ == "__main__":
  main()
