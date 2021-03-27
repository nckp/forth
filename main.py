## built-in words
def builtin_plus():
    print('plus called')
    num1 = stack.pop()
    num2 = stack.pop()
    stack.append(num2 + num1)

def builtin_colon():
    global compileMode
    compileMode = True
    global expectIdentifier
    expectIdentifier = True

# : ; immediate and : immediate ; should give same result but i guess ; will push address to stack anyway?
def builtin_immediate(): # could we use this to unify execute and compile functions?
    # parse each word for additional header option like 'immediate' and execute it if found,
    # use that to implement immediate word
    global compileMode
    if compileMode:
        if len(dictionary[addresses[-1]]['code']) > 2:
            execute(parse(dictionary[addresses[-1]]['code'][-2])) # execute second to last word in word's code section, second to last because last item is the IMMEDIATE word
        else:
            execute(parse(dictionary[addresses[-1]]['address'])) # address should get appened to the stack
    else:
        pass # we insert to definition rather than stack
        

def builtin_semicolon():
    global compileMode
    compileMode = False
    # push address onto stack?

## 
expectIdentifier = False
compileMode = False
immediate = False 

def check_conditions():
    pass 


stack = []
addresses = []

## 
dictionary = {}

def init_dictionary():
    new_word('+', builtin=builtin_plus)
    new_word('INC', code=[1, '+'])
    new_word(':', builtin=builtin_colon)
    new_word('immediate', builtin=builtin_immediate)
    new_word(';', builtin=builtin_semicolon)

def new_word(idname, code=[], builtin=False):
    dictionary[idname] = {'builtin': builtin, 'code': code, 'idname': idname} # in future implement word header with bit shifts instead of python dictionary/list     
    addresses.append(idname)
    dictionary[addresses[-1]]['address'] = addresses.index(idname)


## 
def parse(tok):
    global expectIdentifier

    if expectIdentifier:
        return tok 
    elif tok in dictionary:
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
    global expectIdentifier

    if expectIdentifier:
        new_word(tok)
        expectIdentifier = False
    elif 
        

def execute(tok):
    if type(tok) is int or type(tok) is float:
        stack.append(tok)
    elif not tok['builtin'] == False:
        tok['builtin']()
    elif len(tok['code']) > 0:
        for t in tok['code']:
            evaluate(t)
    else:
        stack.append(tok['address'])

def evaluate(tok):
    t = parse(tok)
    compile(t) if compileMode else execute(t)


## 
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
    init_dictionary()

    input_file = 'input.forth'

    for tok in read_tokens(input_file):
        try:
            evaluate(tok)
        except (ValueError, IndexError) as err:
            print(err)
            print(stack)
            return
    print(stack)
    print('EOF; done!')
    

main()


