from sentiment import post_request

class Engine:
	def __init__(self):
		self.message_vector = ""
		self.max_tot_length = 40
		self.path = "../tutorial/"
	def process_message(self, mess):
		self.message_vector += mess		
		if len(self.message_vector) > self.max_tot_length:
			sen = post_request(self.message_vector)

			sen_norm = int(100 * sen)

			fo = open(self.path + "sentimentalert", "wb")
			fo.write(str(sen_norm))
			fo.close()

			self.message_vector = ""
