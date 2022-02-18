from tildeathParserListener import tildeathParserListener as tildeathParserBaseListener
from tildeathParser import tildeathParser
from time import sleep

class TypedObject:
	def __init__(self, type: str) -> None:
		self.type = type

class LifetimeObject(TypedObject):
	def __init__(self, type: str, lifetime: float) -> None:
		super().__init__(type)
		self.lifetime = lifetime

class tildeathParserListener(tildeathParserBaseListener):
	def __init__(self) -> None:
		self.objects: dict[str, TypedObject] = {}
		self.types = {
			'universe': lambda: LifetimeObject('universe', 3.154e18),
			'author': lambda: LifetimeObject('being', 2.208e9),
			'meson': lambda: LifetimeObject('particle', 1e-9)
		}

	def exitImportLine(self, ctx: tildeathParser.ImportLineContext):
		print(f"Importing {ctx.varType.text} {ctx.varName.text}")
		self.objects[ctx.varName.text] = self.types[ctx.varType.text]()
	
	def exitGrave(self, ctx: tildeathParser.GraveContext):
		name: str = ctx.arguments().args[0].text
		obj: LifetimeObject = self.objects[name]

		print(f"Waiting for {name} to die in {obj.lifetime} seconds")

		period = 1
		while (obj.lifetime > 0):
			sleep(period)
			obj.lifetime -= period

		print(f"{name} died")
	
	def exitDie(self, ctx: tildeathParser.DieContext):
		if ctx.DIE == None:
			while (True):
				pass
		else:
			print("Program killed")