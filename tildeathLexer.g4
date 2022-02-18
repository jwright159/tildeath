lexer grammar tildeathLexer;

IMPORT: 'import';
IMPORT_TYPE: 'universe' | 'author' | 'meson';
GRAVE: '~ATH';
NULL: 'NULL';

DIE: 'THIS.DIE();';

ID: LETTER+;

SEMI: ';';
COMMA: ',';
OPEN_PAREN: '(';
CLOSE_PAREN: ')';
OPEN_BRACE: '{';
CLOSE_BRACE: '}';

WS: [ \t\n\r]+ -> skip;

fragment LETTER: [a-zA-Z];