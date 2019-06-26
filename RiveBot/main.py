from rivescript import RiveScript
import os.path
import re
bot = RiveScript(utf8=True)
bot.unicode_punctuation = re.compile(r'[.,!?;:]')

file = os.path.dirname(__file__)
data = os.path.join(file, 'data')

bot = RiveScript()
bot.load_directory(data)
bot.sort_replies()

print('You are now talking to Chatty. Type \"/q\" to end the conversation. Have fun!')

while True:
    msg = input('You> ')
    if msg == '/q':
        print ('Bot>', "Bye Bye")
        quit()

    reply = bot.reply("localuser", msg)
    print ('Bot>', reply)
