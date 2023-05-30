# Generated from ..\antlr\enter_player\EnterPlayer.g4 by ANTLR 4.12.0
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
        4,1,11,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,0,5,0,23,8,0,10,0,12,0,26,
        9,0,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,3,37,8,3,10,3,12,3,40,
        9,3,1,4,1,4,1,4,5,4,45,8,4,10,4,12,4,48,9,4,1,5,1,5,1,5,3,24,38,
        46,0,6,0,2,4,6,8,10,0,1,1,0,5,9,49,0,15,1,0,0,0,2,27,1,0,0,0,4,31,
        1,0,0,0,6,33,1,0,0,0,8,41,1,0,0,0,10,49,1,0,0,0,12,13,3,2,1,0,13,
        14,5,1,0,0,14,16,1,0,0,0,15,12,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,
        0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,2,0,0,20,24,3,8,4,0,21,23,
        5,1,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,25,1,0,0,0,24,22,1,0,0,0,
        25,1,1,0,0,0,26,24,1,0,0,0,27,28,3,4,2,0,28,29,5,3,0,0,29,30,3,6,
        3,0,30,3,1,0,0,0,31,32,5,10,0,0,32,5,1,0,0,0,33,38,5,10,0,0,34,35,
        5,4,0,0,35,37,5,10,0,0,36,34,1,0,0,0,37,40,1,0,0,0,38,39,1,0,0,0,
        38,36,1,0,0,0,39,7,1,0,0,0,40,38,1,0,0,0,41,46,3,10,5,0,42,43,5,
        4,0,0,43,45,3,10,5,0,44,42,1,0,0,0,45,48,1,0,0,0,46,47,1,0,0,0,46,
        44,1,0,0,0,47,9,1,0,0,0,48,46,1,0,0,0,49,50,7,0,0,0,50,11,1,0,0,
        0,4,17,24,38,46
    ]

class EnterPlayerParser ( Parser ):

    grammarFileName = "EnterPlayer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "'Sentimentos:'", "':'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ALEGRIA", "TRISTEZA", "RAIVA", "NOJINHO", 
                      "MEDO", "TEXT", "WS" ]

    RULE_mensagem = 0
    RULE_personagemacao = 1
    RULE_nome = 2
    RULE_acao = 3
    RULE_sentimentos = 4
    RULE_sentimento = 5

    ruleNames =  [ "mensagem", "personagemacao", "nome", "acao", "sentimentos", 
                   "sentimento" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ALEGRIA=5
    TRISTEZA=6
    RAIVA=7
    NOJINHO=8
    MEDO=9
    TEXT=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MensagemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentimentos(self):
            return self.getTypedRuleContext(EnterPlayerParser.SentimentosContext,0)


        def personagemacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnterPlayerParser.PersonagemacaoContext)
            else:
                return self.getTypedRuleContext(EnterPlayerParser.PersonagemacaoContext,i)


        def getRuleIndex(self):
            return EnterPlayerParser.RULE_mensagem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMensagem" ):
                listener.enterMensagem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMensagem" ):
                listener.exitMensagem(self)




    def mensagem(self):

        localctx = EnterPlayerParser.MensagemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_mensagem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.personagemacao()
                self.state = 13
                self.match(EnterPlayerParser.T__0)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 19
            self.match(EnterPlayerParser.T__1)
            self.state = 20
            self.sentimentos()
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 21
                    self.match(EnterPlayerParser.T__0) 
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PersonagemacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nome(self):
            return self.getTypedRuleContext(EnterPlayerParser.NomeContext,0)


        def acao(self):
            return self.getTypedRuleContext(EnterPlayerParser.AcaoContext,0)


        def getRuleIndex(self):
            return EnterPlayerParser.RULE_personagemacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPersonagemacao" ):
                listener.enterPersonagemacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPersonagemacao" ):
                listener.exitPersonagemacao(self)




    def personagemacao(self):

        localctx = EnterPlayerParser.PersonagemacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_personagemacao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.nome()
            self.state = 28
            self.match(EnterPlayerParser.T__2)
            self.state = 29
            self.acao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NomeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(EnterPlayerParser.TEXT, 0)

        def getRuleIndex(self):
            return EnterPlayerParser.RULE_nome

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNome" ):
                listener.enterNome(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNome" ):
                listener.exitNome(self)




    def nome(self):

        localctx = EnterPlayerParser.NomeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nome)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(EnterPlayerParser.TEXT)
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

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(EnterPlayerParser.TEXT)
            else:
                return self.getToken(EnterPlayerParser.TEXT, i)

        def getRuleIndex(self):
            return EnterPlayerParser.RULE_acao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcao" ):
                listener.enterAcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcao" ):
                listener.exitAcao(self)




    def acao(self):

        localctx = EnterPlayerParser.AcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_acao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(EnterPlayerParser.TEXT)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 34
                    self.match(EnterPlayerParser.T__3)
                    self.state = 35
                    self.match(EnterPlayerParser.TEXT) 
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentimentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentimento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnterPlayerParser.SentimentoContext)
            else:
                return self.getTypedRuleContext(EnterPlayerParser.SentimentoContext,i)


        def getRuleIndex(self):
            return EnterPlayerParser.RULE_sentimentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentimentos" ):
                listener.enterSentimentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentimentos" ):
                listener.exitSentimentos(self)




    def sentimentos(self):

        localctx = EnterPlayerParser.SentimentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sentimentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.sentimento()
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 42
                    self.match(EnterPlayerParser.T__3)
                    self.state = 43
                    self.sentimento() 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentimentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALEGRIA(self):
            return self.getToken(EnterPlayerParser.ALEGRIA, 0)

        def TRISTEZA(self):
            return self.getToken(EnterPlayerParser.TRISTEZA, 0)

        def RAIVA(self):
            return self.getToken(EnterPlayerParser.RAIVA, 0)

        def NOJINHO(self):
            return self.getToken(EnterPlayerParser.NOJINHO, 0)

        def MEDO(self):
            return self.getToken(EnterPlayerParser.MEDO, 0)

        def getRuleIndex(self):
            return EnterPlayerParser.RULE_sentimento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentimento" ):
                listener.enterSentimento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentimento" ):
                listener.exitSentimento(self)




    def sentimento(self):

        localctx = EnterPlayerParser.SentimentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sentimento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





