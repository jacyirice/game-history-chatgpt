from antlr4 import InputStream, CommonTokenStream
from .EnterPlayerLexer import EnterPlayerLexer as ExprLexer
from .EnterPlayerParser import EnterPlayerParser as ExprParser
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Erro de sintaxe na linha {line}, coluna {column}: {msg}")


def valid(resposta: str) -> bool:
    error_listener = MyErrorListener()
    input_stream = InputStream(resposta)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.mensagem()
    print(1, error_listener.errors)
    if parser.getNumberOfSyntaxErrors() > 0:
        return (
            False,
            ';\n'.join(error_listener.errors)
            + "\n\nEntrada inválida! A sintaxe não está correta."
            + "\nUtilize a sintaxe:"
            + "\n<NOME DO PERSONAGEM>: <AÇÃO DO PERSONAGEM>"
            + "\nSentimentos: <SENTIMENTO DO PERSONAGEM>",
        )
    return True, ""
