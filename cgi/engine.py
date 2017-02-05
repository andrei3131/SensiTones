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
		self.file_path = "../tutorial/resources/"
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
	def process_files(self, filename):
		filename=filename[0:-1]
		content = ""
		with open(self.file_path + filename, 'r') as content_file:
			content = content_file.read()
			content_file.close()
		
		my_file = self.path + "input.txt"

		fo = open(my_file, "wb")
		fo.write(content)
		fo.close()

