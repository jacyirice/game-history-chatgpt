from antlr4 import InputStream, CommonTokenStream
from antlr.EntradaUsuarioLexer import EntradaUsuarioLexer as ExprLexer
from antlr.EntradaUsuarioParser import EntradaUsuarioParser as ExprParser

def validar_sintaxe_entrada(resposta: str) -> bool:
    input_stream = InputStream(resposta)
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.start()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Entrada inválida! A sintaxe não está correta.", "\nUtilize a sintaxe <NOME DO PERSONAGEM>: <AÇÃO DO PERSONAGEM>")
        return False
    return True
