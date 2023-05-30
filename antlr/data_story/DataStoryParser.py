# Generated from ..\antlr\data_story\DataStory.g4 by ANTLR 4.12.0
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
        4,1,12,44,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,3,1,24,8,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,
        1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,9,10,39,0,12,1,0,0,0,2,14,1,0,0,0,
        4,27,1,0,0,0,6,31,1,0,0,0,8,39,1,0,0,0,10,41,1,0,0,0,12,13,3,2,1,
        0,13,1,1,0,0,0,14,23,5,1,0,0,15,20,3,4,2,0,16,17,5,2,0,0,17,19,3,
        4,2,0,18,16,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,
        24,1,0,0,0,22,20,1,0,0,0,23,15,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,
        0,25,26,5,3,0,0,26,3,1,0,0,0,27,28,5,4,0,0,28,29,3,6,3,0,29,30,5,
        5,0,0,30,5,1,0,0,0,31,32,5,6,0,0,32,33,5,7,0,0,33,34,3,8,4,0,34,
        35,5,2,0,0,35,36,5,8,0,0,36,37,5,7,0,0,37,38,3,10,5,0,38,7,1,0,0,
        0,39,40,7,0,0,0,40,9,1,0,0,0,41,42,5,11,0,0,42,11,1,0,0,0,2,20,23
    ]

class DataStoryParser ( Parser ):

    grammarFileName = "DataStory.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "'{'", "'}'", "'\"role\"'", 
                     "':'", "'\"content\"'", "'\"user\"'", "'\"system\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "WS" ]

    RULE_json = 0
    RULE_array = 1
    RULE_object = 2
    RULE_pair = 3
    RULE_roleValue = 4
    RULE_contentValue = 5

    ruleNames =  [ "json", "array", "object", "pair", "roleValue", "contentValue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    STRING=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(DataStoryParser.ArrayContext,0)


        def getRuleIndex(self):
            return DataStoryParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = DataStoryParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataStoryParser.ObjectContext)
            else:
                return self.getTypedRuleContext(DataStoryParser.ObjectContext,i)


        def getRuleIndex(self):
            return DataStoryParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = DataStoryParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(DataStoryParser.T__0)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 15
                self.object_()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 16
                    self.match(DataStoryParser.T__1)
                    self.state = 17
                    self.object_()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 25
            self.match(DataStoryParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self):
            return self.getTypedRuleContext(DataStoryParser.PairContext,0)


        def getRuleIndex(self):
            return DataStoryParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)




    def object_(self):

        localctx = DataStoryParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_object)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(DataStoryParser.T__3)
            self.state = 28
            self.pair()
            self.state = 29
            self.match(DataStoryParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def roleValue(self):
            return self.getTypedRuleContext(DataStoryParser.RoleValueContext,0)


        def contentValue(self):
            return self.getTypedRuleContext(DataStoryParser.ContentValueContext,0)


        def getRuleIndex(self):
            return DataStoryParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = DataStoryParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(DataStoryParser.T__5)
            self.state = 32
            self.match(DataStoryParser.T__6)
            self.state = 33
            self.roleValue()
            self.state = 34
            self.match(DataStoryParser.T__1)
            self.state = 35
            self.match(DataStoryParser.T__7)
            self.state = 36
            self.match(DataStoryParser.T__6)
            self.state = 37
            self.contentValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DataStoryParser.RULE_roleValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoleValue" ):
                listener.enterRoleValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoleValue" ):
                listener.exitRoleValue(self)




    def roleValue(self):

        localctx = DataStoryParser.RoleValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_roleValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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


    class ContentValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DataStoryParser.STRING, 0)

        def getRuleIndex(self):
            return DataStoryParser.RULE_contentValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContentValue" ):
                listener.enterContentValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContentValue" ):
                listener.exitContentValue(self)




    def contentValue(self):

        localctx = DataStoryParser.ContentValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_contentValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(DataStoryParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





