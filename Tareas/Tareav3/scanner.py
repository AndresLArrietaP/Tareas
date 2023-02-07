from tokens import Token, TokenType


class Scanner:
    def __init__(self,text)->None:
        self.it= iter(text)
        #self.id=''
        self.curr=None
        self.advance()

    def advance(self):
        try:
            self.curr=next(self.it)
        except StopIteration:
            self.curr=None
    
    def scan(self):
        while self.curr is not None:
            if self.curr in ('\n','\t',' '):
                self.advance()
            elif self.curr=='(':
                self.advance()
                return Token(TokenType.LPAREN,'(')
            elif self.curr==')':
                self.advance()
                return Token(TokenType.RPAREN,')')
            elif self.curr=='{':
                self.advance()
                return Token(TokenType.LKEY,'{')
            elif self.curr=='}':
                self.advance()
                return Token(TokenType.RKEY,'}')
            elif self.curr=='t':
                self.verify('true')
                return Token(TokenType.TRUE,'true')
            elif self.curr=='f':
                self.verify('false')
                return Token(TokenType.FALSE,'false')
            elif self.curr=='a':
                self.verify('and')
                return Token(TokenType.AND,'and')
            elif self.curr=='o':
                self.verify('or')
                return Token(TokenType.OR,'or')
            elif self.curr=='n':
                self.verify('not')
                return Token(TokenType.NOT,'not')
            elif self.curr=='m':
                self.verify('main')
                return Token(TokenType.MAIN,'main')
            elif self.curr=='i' or self.curr=='f' or self.curr=='d' or self.curr=='s' or self.curr=='c' or self.curr=='b' or self.curr=='v':
                if self.curr=='i':
                    self.verify('int')
                    return Token(TokenType.DTYPE,'int')
                elif self.curr=='f':
                    self.verify('float')
                    return Token(TokenType.DTYPE,'float')
                elif self.curr=='d':
                    self.verify('double')
                    return Token(TokenType.DTYPE,'double')
                elif self.curr=='s':
                    self.verify('string')
                    return Token(TokenType.DTYPE,'string')
                elif self.curr=='c':
                    self.verify('char')
                    return Token(TokenType.DTYPE,'char')
                elif self.curr=='b':
                    self.verify('bool')
                    return Token(TokenType.DTYPE,'bool')
                elif self.curr=='b':
                    self.verify('byte')
                    return Token(TokenType.DTYPE,'byte')
                elif self.curr=='v':
                    self.verify('void')
                    return Token(TokenType.DTYPE,'void')
            else:
                raise Exception('Token no reconocido')
        return None

    def ScanAll(self):
        tokens=[]
        while True:
            token=self.scan()
            if token is None:
                break
            tokens.append(token)
        return tokens

    def verify(self,text):
        for c in text:
            if self.curr is None:
                raise Exception('Token no reconocido')
            if self.curr != c:
                raise Exception('Token no reconocido')
            self.advance()