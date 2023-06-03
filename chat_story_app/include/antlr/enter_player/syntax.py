from antlr4 import InputStream, CommonTokenStream
from .EnterPlayerLexer import EnterPlayerLexer as ExprLexer
from .EnterPlayerParser import EnterPlayerParser as ExprParser
from ..listeners import MyErrorListener



def valid(resposta: str) -> bool:
    input_stream = InputStream(resposta)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    
    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    tree = parser.mensagem()
    if parser.getNumberOfSyntaxErrors() > 0:
        return (
            False,
            ";\n".join(error_listener.errors)
            + "\n\nEntrada inválida! A sintaxe não está correta."
            + "\nUtilize a sintaxe:"
            + "\n<NOME DO PERSONAGEM>: <AÇÃO DO PERSONAGEM>"
            + "\nSentimentos: <SENTIMENTO DO PERSONAGEM>",
        )
    return True, ""
