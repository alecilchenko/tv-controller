class TVController:
	current_ch = 0
	
	def __init__(self, *args):
		self.channels = args[0]

	def first_channel(self):
		TVController.current_ch = 0
		return self.channels[0]
		
	def last_channel(self):
		TVController.current_ch = len(self.channels) - 1
		return self.channels[-1]
	
	def turn_channel(self, N):
		if N > len(self.channels[0]) or N == 0:
			TVController.current_ch = 0
			print("We don't have so much channels, so let's turn on first challel")
			return self.channels[0]
		else:
			TVController.current_ch = N-1
			return self.channels[N-1]
		
	def next_channel(self):
		if TVController.current_ch == len(self.channels) - 1:
			TVController.current_ch = 0
			return self.channels[0]
		else:
			TVController.current_ch += 1
			return self.channels[TVController.current_ch]
	
	def previous_channel(self):
		if TVController.current_ch == 0:
			TVController.current_ch = len(self.channels) - 1
			return self.channels[-1]
		else:
			TVController.current_ch -= 1
			return self.channels[TVController.current_ch]

	def current_channel(self):
		return self.channels[TVController.current_ch]
		
	def is_exist(self, name):
		if name in range(1, len(self.channels) + 1) or name in self.channels:
			print('Yes')
		else:
			print('No')
		
	
		
		
CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

'''print(controller.channels)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.current_channel())
print(controller.previous_channel())
print(controller.next_channel())
controller.is_exist(N = 5)'''

