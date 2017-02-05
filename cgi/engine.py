from sentiment import post_request

def process_message(message_vector):
	sent_mess = message_vector.split("(GMT)&message=")[1]
	v = sent_mess.split('+')
	sent_mess = ""
	for m in v:
		sent_mess += m
		sent_mess += ' '
	return sent_mess

class Engine:
	def __init__(self):
		self.message_vector = ""
		self.max_tot_length = 40
		self.path = "../tutorial/"
	def process_message(self, mess):
		self.message_vector += process_message(mess)
		if len(self.message_vector) > self.max_tot_length:
			sen = post_request(self.message_vector)
			sen_norm = int(100 * sen)
			print sen

			fo = open(self.path + "sentimentalert", "wb")
			fo.write(str(sen_norm))
			fo.close()

			self.message_vector = ""
