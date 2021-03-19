## built-in words
def builtin_plus():
    num1 = stack.pop()
    num2 = stack.pop()
    stack.append(num2 + num1)


## data
compileMode = False

stack = []

dictionary = {
    '+': {'builtin': builtin_plus, 'code': []},
    'INC': {'builtin': False, 'code': [1, '+']}
}



## 

def parse(tok):
    if tok in dictionary:
        return dictionary[tok]
    elif type(tok) is int or type(tok) is float or tok.replace('.', '').replace('-', '').isdigit():
        try:
            num = int(tok)
        except ValueError:
            num = float(tok)
        return num
    else:
        raise ValueError("'{0}' is not a valid word or number.".format(tok) )

def compile(tok):
    print('shound;t be ca;;ed at a;; eyet')

def execute(tok):
    if type(tok) is int or type(tok) is float:
        stack.append(tok)
    elif not tok['builtin'] == False:
        tok['builtin']()
    else:
        for t in tok['code']:
            execute(parse(t))


## process stream of tokens

def read_chunks(file_object, chunk_size = 1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def read_tokens(file):
    with open(file) as f:
        for line in read_chunks(f):
            for tok in list(map(str.strip, line.split() ) ):
                yield tok    
    
def main():
    file = 'input.forth'
    for tok in read_tokens(file):
        try:
            result = parse(tok)
            if compileMode:
                compile(result)
            else:
                execute(result)
        except (ValueError, IndexError) as err:
            print(err)
            print(stack)
            return
    print(stack)
    print('EOF; done!')
    
main()


