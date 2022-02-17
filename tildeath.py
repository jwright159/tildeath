import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from tildeathLexer import tildeathLexer
from tildeathParser import tildeathParser
from tildeathConsoleListener import tildeathParserListener

def main(filename: str):
	file_stream = FileStream(filename)
	lexer = tildeathLexer(file_stream)
	token_stream = CommonTokenStream(lexer)
	parser = tildeathParser(token_stream)
	tree = parser.code()

	listener = tildeathParserListener()
	walker = ParseTreeWalker()
	walker.walk(listener, tree)

if __name__ == '__main__':
	main(sys.argv[1])