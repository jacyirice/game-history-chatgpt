from antlr4 import InputStream, CommonTokenStream
from antlr.data_story.DataStoryLexer import DataStoryLexer as ExprLexer
from antlr.data_story.DataStoryParser import DataStoryParser as ExprParser


def valid(resposta: str) -> bool:
    input_stream = InputStream(resposta)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.json()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print(
            "Entrada inválida! A sintaxe não está correta.",
        )
        return False
    return True
