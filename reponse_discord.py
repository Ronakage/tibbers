import random
import aiohttp

async def getAnswer(preds, message):
    if preds:
        partial_answer = message.author.mention + "\nIt seems that your message '" + message.content + "' is " + str(str(preds)[1:-1])
        partial_answer = partial_answer + "\n"
        await chooseAnswer(partial_answer,message)

async def chooseAnswer(partial_answer,message):
    choice = random.randint(1, 4)
    if choice == 1:
        await getBoredAnswer(partial_answer,message)
    if choice == 2:
        await getEvilAnswer(partial_answer,message)
    if choice == 3:
        await getStoicAnswer(partial_answer, message)
    if choice == 4:
        await getAdviceAnswer(partial_answer, message)

async def getBoredAnswer(partial_answer, message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.boredapi.com/api/activity/') as r:
            if r.status == 200:
                js = await r.json()
                answer = partial_answer + "You seem B O R E D as hell 🥱...How about you " + str(js['activity']).lower() +" ?"
                await message.channel.send(answer)

async def getEvilAnswer(partial_answer, message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://evilinsult.com/generate_insult.php?lang=en&type=json') as r:
            if r.status == 200:
                js = await r.json()
                answer = partial_answer + "So, " + str(js['insult']).lower() + " 😈"
                await message.channel.send(answer)

async def getStoicAnswer(partial_answer, message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.themotivate365.com/stoic-quote') as r:
            if r.status == 200:
                js = await r.json()
                answer = partial_answer + "Instead of going around spreading hate around like a coward, here's a stoic quote 😎 for you :\n" + str(js['quote'])
                await message.channel.send(answer)

async def getAdviceAnswer(partial_answer, message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.adviceslip.com/advice') as r:
            if r.status == 200:
                js = await r.json(content_type='text/html')
                answer = partial_answer + "Let's say you were forgiven for what you just said, here's an advice 💡 for your life moving forward :\n" + str(js['slip']['advice'])
                await message.channel.send(answer)