from pygments.lexer import RegexLexer
from pygments.token import *
import re


fractaKeywords = [
    "import",
    "func",
    "return",
    "var",
    "const",
    "this",
    "mut",
    "for",
    "while",
    "if",
    "else",
    "type",
    "virtual",
    "layout",
    "struct",
    "enum",
    "variant",
    "method",
    "operator",
    "generator",
    "interface",
    "auto",
    "true",
    "false",
    "switch",
    "case",
    "default",
]

fractaDefaultTypes = [
    "bool",
    "i8",
    "i16",
    "i32",
    "i64",
    "u8",
    "u16",
    "u32",
    "u64",
    "f32",
    "f64",
    "ptr"
]

fractaOperators = [
    '.',
    '+',
    '-',
    '*',
    '/',
    '%',
    '=',
    '&',
    '::',
]

fractaPunctuation = [
    '{',
    '}',
    '(',
    ')',
    '[',
    ']',
    ':',
    ';',
]

class FractaLexer(RegexLexer):
    name = "Fracta"
    flags = re.MULTILINE | re.DOTALL

    tokens = {
        'root': [
            (r'//.*?$', Comment.Single),
            (r'/\*', Comment.Multiline, 'comment'),

            (rf'({'|'.join([re.escape(tok) for tok in fractaKeywords])})\b', Keyword),
            (rf'({'|'.join([re.escape(tok) for tok in fractaDefaultTypes])})\b', Name.Builtin),
            (rf'\b[a-zA-Z_]\w*\b', Name),
            (rf'({'|'.join([re.escape(tok) for tok in fractaPunctuation])})', Punctuation),
            (rf'({'|'.join([re.escape(tok) for tok in fractaOperators])})', Operator),

            (r'\d+(.\d+)?(f)?', Number),

            (r'"(?:\\.|[^"\\])*"', String),

            (r'\s+', Whitespace),
            (r'.', Text),
        ],

        'comment': [
            (r'[^*/]+', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ]

    }
    
    
    