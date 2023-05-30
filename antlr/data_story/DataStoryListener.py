# Generated from ..\antlr\data_story\DataStory.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DataStoryParser import DataStoryParser
else:
    from DataStoryParser import DataStoryParser

# This class defines a complete listener for a parse tree produced by DataStoryParser.
class DataStoryListener(ParseTreeListener):

    # Enter a parse tree produced by DataStoryParser#json.
    def enterJson(self, ctx:DataStoryParser.JsonContext):
        pass

    # Exit a parse tree produced by DataStoryParser#json.
    def exitJson(self, ctx:DataStoryParser.JsonContext):
        pass


    # Enter a parse tree produced by DataStoryParser#array.
    def enterArray(self, ctx:DataStoryParser.ArrayContext):
        pass

    # Exit a parse tree produced by DataStoryParser#array.
    def exitArray(self, ctx:DataStoryParser.ArrayContext):
        pass


    # Enter a parse tree produced by DataStoryParser#object.
    def enterObject(self, ctx:DataStoryParser.ObjectContext):
        pass

    # Exit a parse tree produced by DataStoryParser#object.
    def exitObject(self, ctx:DataStoryParser.ObjectContext):
        pass


    # Enter a parse tree produced by DataStoryParser#pair.
    def enterPair(self, ctx:DataStoryParser.PairContext):
        pass

    # Exit a parse tree produced by DataStoryParser#pair.
    def exitPair(self, ctx:DataStoryParser.PairContext):
        pass


    # Enter a parse tree produced by DataStoryParser#roleValue.
    def enterRoleValue(self, ctx:DataStoryParser.RoleValueContext):
        pass

    # Exit a parse tree produced by DataStoryParser#roleValue.
    def exitRoleValue(self, ctx:DataStoryParser.RoleValueContext):
        pass


    # Enter a parse tree produced by DataStoryParser#contentValue.
    def enterContentValue(self, ctx:DataStoryParser.ContentValueContext):
        pass

    # Exit a parse tree produced by DataStoryParser#contentValue.
    def exitContentValue(self, ctx:DataStoryParser.ContentValueContext):
        pass



del DataStoryParser