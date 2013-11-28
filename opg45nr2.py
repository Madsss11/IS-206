class Scene(object): #printer ut nivåene

	def enter(self):
		print ""
		exit(1)
		
class Engine(object): #driver spillet videre ved å skifte nivåer etter prestasjon
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self): #sørger for å starte første nivå
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
class Death(Scene): # denne scenen spilles av dersom du taper spillet

	quips = [
		"Losers go home"
	]
		
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)