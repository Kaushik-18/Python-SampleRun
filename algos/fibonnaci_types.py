# function or expression for x in iterable if condition if required

# matix  = [[numberGen(itemid) for itemid in range(0,5) if itemid%2 == 0] for rowid in range(0,4) ]
# print(matix)

# dictionary comprehension
# metadata_dict = {f:os.stat(f) for f in glob.glob('*test*.py')}

# generators return iterators .. a better way of writing than custom

def gen_fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


_fib_cache = {}


def fib(n):
    if n in _fib_cache:
        return _fib_cache[n]
    else:
        _fib_cache[n] = n if n < 2 else fib(n - 2) + fib(n - 1)
        return _fib_cache[n]


fibsList = [x for x in gen_fib(5)]

N = int(input())

cubesfunc = lambda a: a * a * a


def gen_fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


sequence = [x for x in gen_fib(N)]
final_seq = list(map(cubesfunc, sequence))
print(final_seq)

print(fibsList)
