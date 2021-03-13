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
        print(tok)
main()