grammar EntradaUsuario;

start: personagem ':' acao;

personagem: WORD;
acao: WORD (WS WORD)*;

WORD: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
