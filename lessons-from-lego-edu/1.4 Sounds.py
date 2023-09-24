# import the speaker
from hub import sound
from app import sound as appsound

import runloop

async def main():
    # play a song
    await sound.beep(400, 1000, 100)
    await sound.beep(450, 500, 100)
    await sound.beep(500, 1000, 100)
    await appsound.play('Cat Meow 1')

runloop.run(main())