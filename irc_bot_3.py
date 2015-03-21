from sock import Connection
from bot import Bot

dense_bot = Bot("irc.freenode.net", "#tagprobots", "other_bot")

socky = Connection(dense_bot)
socky.connect()



while 1:
	socky.receive()
	print("hue")