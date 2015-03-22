from sock import Connection
from bot import Bot
import threading

other_bot = Bot("irc.freenode.net", "#tagprobots", "other_bot", 6667)
second_bot = Bot("irc.freenode.net", "#tagprobots", "other_other_bot", 6666)


socky = Connection(other_bot)
socky.connect()

# socky2 = Connection(second_bot)
# socky2.connect()


while 1:
	message = socky.receive()
	other_bot.respond(socky, message)
	# message2 = socky2.receive()




# def start():
# 	if __name__ == "__main__":
# 		t1 = threading.Thread(target = bot_2_thread, args = ())
# 		t1.start()

# 		t2 = threading.Thread(target = bot_1_thread, args = ())
# 		t2.start()


# def bot_1_thread():
# 	while 1:
# 		message = socky.receive()

# def bot_2_thread():
# 	while 1:
# 		message2 = socky2.receive()

# start()