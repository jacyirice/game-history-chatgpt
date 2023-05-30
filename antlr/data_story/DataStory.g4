grammar DataStory;

json: array;

array: '[' (object (',' object)*)? ']';

object: '{' pair '}';

pair: '"role"' ':' roleValue ',' '"content"' ':' contentValue;

roleValue: '"user"' | '"system"';

contentValue: STRING;

STRING: '"' (ESC | ~["\\])* '"';

fragment ESC: '\\' (["\\/bfnrt] | UNICODE);

fragment UNICODE: 'u' HEX HEX HEX HEX;

fragment HEX: [0-9a-fA-F];

WS: [ \t\r\n]+ -> skip;
