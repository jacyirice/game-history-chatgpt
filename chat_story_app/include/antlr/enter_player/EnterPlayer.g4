grammar EnterPlayer;

mensagem: (personagemacao '\n')+ 'Sentimentos:' sentimentos ('\n')*?;
personagemacao: nome ':' acao;
nome: TEXT;
acao: TEXT (' ' TEXT)*?;
sentimentos: sentimento (', ' sentimento)*?;
sentimento: ALEGRIA | TRISTEZA | RAIVA | NOJINHO | MEDO;

ALEGRIA: [Aa][Ll][Ee][Gg][Rr][Ii][Aa];
TRISTEZA: [Tt][Rr][Ii][Ss][Tt][Ee][Zz][Aa];
RAIVA: [Rr][Aa][Ii][Vv][Aa];
NOJINHO: [Nn][Oo][Jj][Ii][Nn][Hh][Oo];
MEDO: [Mm][Ee][Dd][Oo];

TEXT: [a-zA-Z]+;
WS: [ \t\r]+ -> skip;
