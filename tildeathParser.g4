parser grammar tildeathParser;

options { tokenVocab=tildeathLexer; }

code: imports grave die EOF;

imports: importLine importLine;

importLine: 'import' varType=IMPORT_TYPE varName=ID ';';

grave: '~ATH' arguments block block;

arguments: '(' args+=ID (',' args+=ID)* ')';

block: '{' line '}' | line;

line: grave | function | ;

function: funcName=ID args=arguments ';';

die: DIE?;