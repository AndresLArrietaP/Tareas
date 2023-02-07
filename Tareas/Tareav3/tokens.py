from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    TRUE=1
    FALSE=2
    AND=3
    OR=4
    NOT=5
    LPAREN=6
    RPAREN=7
    LKEY=8
    RKEY=9
    MAIN=10
    DTYPE=11
    ID=12
    END=13

    def __str__(self) -> str:
        return self.name

@dataclass
class Token:
    token_type: TokenType
    lexeme: str

    def __repr__(self) -> str:
        return f'"{self.lexeme}"'
