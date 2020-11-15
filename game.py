import os, pygame
import pygame.midi
from settings import Settings

class Game():
	def __init__(self):
		self.font = myfont = pygame.font.SysFont('Helvetica', 15)
		self.signals = []
		self.startTime = None
		self.state = "stopped"
		pygame.midi.init()
		in_id = pygame.midi.get_default_input_id()
		if in_id != -1:
			self.midi_input = pygame.midi.Input(in_id)
		else:
			self.midi_input = None

	def start(self, t):
		self.state='recording'
		if not self.startTime:
			self.startTime = t

	def restart(self):
		self.state = "stopped"
		self.signals = []	
		self.startTime = None				

	def stop(self):
		self.state = "stopped"

	def save(self):
		self.state = "stopped"
		print('saved')

	def setState(self, midi):
		if midi != []:
			
			[[_, key, _, _], t] = midi[0]
			print(key)
			if (key == 1):
				self.start(t)
			elif key == 60:
				self.restart()
			elif key == 64:
				self.save()
			else:

				self.stop()

	def getMidi(self):
		midi = self.midi_input.read(47)
		self.setState(midi)
		
		if self.state != 'stopped':
			if midi != []:
				[[_, _, h, _], t] = midi[0]
				t = t - self.startTime
				self.signals.append((t,h))
			else:
				t, h = self.signals[-1]
				self.signals.append((t + (1000 / Settings.frameRate), h))

	def drawToScreen(self, screen):
		graphBottomY = Settings.height / 2 + 127/2
		if len(self.signals) > 0:
			screen.fill((0, 0, 0))
			text = self.font.render('.', False, (255, 255, 255))
			for signal in self.signals:
				t, h = signal
				x = t/10
				y = graphBottomY - h*2
				screen.blit(text, (x,y))

	def loop(self, screen):
		clock = pygame.time.Clock()
		signals = []

		while True:
			delta_t = clock.tick(Settings.frameRate)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			self.getMidi()
			self.drawToScreen(screen)
			pygame.display.update()

	def quit(self):
		pass