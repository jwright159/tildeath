from tildeathParserListener import tildeathParserListener as tildeathParserBaseListener
from tildeathParser import tildeathParser

class tildeathParserListener(tildeathParserBaseListener):
	def __init__(self):
		pass

	def exitImportLine(self, ctx: tildeathParser.ImportLineContext):
		print("Imported", ctx.varType.text, ctx.varName.text)
	
	def exitGrave(self, ctx: tildeathParser.GraveContext):
		print(ctx.arguments().args[0].text, "died")
	
	def exitDie(self, ctx: tildeathParser.DieContext):
		if ctx.DIE == None:
			while (True):
				pass
		else:
			print("Program killed")