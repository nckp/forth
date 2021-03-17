
## data

dictionary = {}

## built-in words


## parsing and execution

def parse(tok):
    if tok in dictionary:
        dictionary[tok]() 
    elif tok.replace('.', '').replace('-', '').isdigit():
        try:
            num = int(tok)
        except ValueError:
            num = float(tok)
    else:
        raise ValueError("'{0}' is not a valid word or number.".format(tok))

## read tokens from file

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
            parse(tok)
        except ValueError as e:
            print(e)
            return

    print('EOF; done!')
    
main()


