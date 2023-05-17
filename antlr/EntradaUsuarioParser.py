# Generated from ..\jogo de corno\antlr\EntradaUsuario.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,21,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,
        1,2,5,2,16,8,2,10,2,12,2,19,9,2,1,2,0,0,3,0,2,4,0,0,18,0,6,1,0,0,
        0,2,10,1,0,0,0,4,12,1,0,0,0,6,7,3,2,1,0,7,8,5,1,0,0,8,9,3,4,2,0,
        9,1,1,0,0,0,10,11,5,2,0,0,11,3,1,0,0,0,12,17,5,2,0,0,13,14,5,3,0,
        0,14,16,5,2,0,0,15,13,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,
        1,0,0,0,18,5,1,0,0,0,19,17,1,0,0,0,1,17
    ]

class EntradaUsuarioParser ( Parser ):

    grammarFileName = "EntradaUsuario.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WORD", "WS" ]

    RULE_start = 0
    RULE_personagem = 1
    RULE_acao = 2

    ruleNames =  [ "start", "personagem", "acao" ]

    EOF = Token.EOF
    T__0=1
    WORD=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def personagem(self):
            return self.getTypedRuleContext(EntradaUsuarioParser.PersonagemContext,0)


        def acao(self):
            return self.getTypedRuleContext(EntradaUsuarioParser.AcaoContext,0)


        def getRuleIndex(self):
            return EntradaUsuarioParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = EntradaUsuarioParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.personagem()
            self.state = 7
            self.match(EntradaUsuarioParser.T__0)
            self.state = 8
            self.acao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PersonagemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(EntradaUsuarioParser.WORD, 0)

        def getRuleIndex(self):
            return EntradaUsuarioParser.RULE_personagem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPersonagem" ):
                listener.enterPersonagem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPersonagem" ):
                listener.exitPersonagem(self)




    def personagem(self):

        localctx = EntradaUsuarioParser.PersonagemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_personagem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(EntradaUsuarioParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(EntradaUsuarioParser.WORD)
            else:
                return self.getToken(EntradaUsuarioParser.WORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(EntradaUsuarioParser.WS)
            else:
                return self.getToken(EntradaUsuarioParser.WS, i)

        def getRuleIndex(self):
            return EntradaUsuarioParser.RULE_acao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcao" ):
                listener.enterAcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcao" ):
                listener.exitAcao(self)




    def acao(self):

        localctx = EntradaUsuarioParser.AcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_acao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(EntradaUsuarioParser.WORD)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 13
                self.match(EntradaUsuarioParser.WS)
                self.state = 14
                self.match(EntradaUsuarioParser.WORD)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





