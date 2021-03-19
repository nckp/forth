
## data
compileMode = False


stack = []

dictionary = {}


## built-in words


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
    pass

def execute(tok):
    pass


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
        except ValueError as e:
            print(e)
            return

    print('EOF; done!')
    
main()


