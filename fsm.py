import re
from inspect import getmembers

STATE_NAME = re.compile('^[A-Z0-9]+$')

class FSM(object):
	def __init__(self):

		self.state_name = 'START'
		members = getmembers(self)
		self.possible_states ={}

		for k,v in members:
			if STATE_NAME.match(k):
				self.possible_states[k] = v

	def handle(self, event):
		state_handler = self.lookup_state()
		self.state_name = state_handler(event)


	def lookup_state(self):
		return self.possible_states.get(self.state_name)

	def START(self,event):
		return self.LISTENING

	def LISTENING(self,event):
		if event == 'CONNECTED':
			return self.CONNECTED
		elif event == 'error':
			return self.LISTENING
		else:
			return ERROR

	def CONNECTED(self,event):
		if event == 'accept':
			return self.ACCEPTED
		elif event == 'close':
			return self.CLOSED
		else:
			return ERROR

	def ACCEPTED(self,event):
		if event == 'read':
			return self.READING(event)
		elif event == 'close':
			return self.CLOSED
		elif event == 'write':
			return self.WRITING(event)
		else:
			return ERROR

	def READING(self,event):
		if event == 'read':
			return self.READING(event)
		elif event == 'close':
			return self.CLOSED
		elif event == 'write':
			return self.WRITING(event)
		else:
			return ERROR

	def WRITING(self,event):
		if event == 'read':
			return self.READING(event)
		elif event == 'close':
			return self.CLOSED
		elif event == 'write':
			return self.WRITING(event)
		else:
			return ERROR

	def CLOSED(event):
		return self.LISTENING(event)

	def ERROR(event):
		return self.ERROR

fsm = FSM()
state = fsm.START("start")
script = ["connect","accept","read","write","close","connect"]

for event in script:
	print(event+">>>",state)
	state = fsm.handle(event)
	