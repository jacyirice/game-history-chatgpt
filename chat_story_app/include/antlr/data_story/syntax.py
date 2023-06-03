from antlr4 import InputStream, CommonTokenStream
from .DataStoryLexer import DataStoryLexer as ExprLexer
from .DataStoryParser import DataStoryParser as ExprParser
from ..listeners import MyErrorListener


def valid(resposta: str) -> bool:
    input_stream = InputStream(resposta)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.json()

    if parser.getNumberOfSyntaxErrors() > 0:
        return (
            False,
            ";\n".join(error_listener.errors)
            + "\n\nEntrada inválida! A sintaxe do arquivo não está correta.",
        )
    return True, ""
