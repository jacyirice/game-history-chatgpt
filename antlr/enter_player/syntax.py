from antlr4 import InputStream, CommonTokenStream
from antlr.enter_player.EnterPlayerLexer import EnterPlayerLexer as ExprLexer
from antlr.enter_player.EnterPlayerParser import EnterPlayerParser as ExprParser


def valid(resposta: str) -> bool:
    input_stream = InputStream(resposta)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.mensagem()
    if parser.getNumberOfSyntaxErrors() > 0:
        print(
            "Entrada inválida! A sintaxe não está correta.",
            "\nUtilize a sintaxe:",
            "\n<NOME DO PERSONAGEM>: <AÇÃO DO PERSONAGEM>",
            "\nSentimento: <SENTIMENTO DO PERSONAGEM>",
        )
        return False
    return True
