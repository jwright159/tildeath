lexer grammar tildeathLexer;

IMPORT: 'import';
IMPORT_TYPE: 'universe' | 'author';
GRAVE: '~ATH';

ID: LETTER+;

DIE: 'THIS.DIE();';

SEMI: ';';
COMMA: ',';
OPEN_PAREN: '(';
CLOSE_PAREN: ')';
OPEN_BRACE: '{';
CLOSE_BRACE: '}';

WS: [ \t\n\r]+ -> skip;

fragment LETTER: [a-zA-Z];