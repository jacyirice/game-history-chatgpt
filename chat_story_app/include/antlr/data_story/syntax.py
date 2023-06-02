from antlr4 import InputStream, CommonTokenStream
from .DataStoryLexer import DataStoryLexer as ExprLexer
from .DataStoryParser import DataStoryParser as ExprParser


def valid(resposta: str) -> bool:
    input_stream = InputStream(resposta)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.json()

    if parser.getNumberOfSyntaxErrors() > 0:
        return False, "Entrada inválida! A sintaxe não está correta."
    return True, ""
