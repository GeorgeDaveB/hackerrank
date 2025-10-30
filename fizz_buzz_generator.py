def gen(n): 
    for i in n:
         yield i

def fizzBuzz(n):
    for x in gen(n):
        fb = ''
        print(x)
        if (x % 3 == 0):
            fb += 'fizz'
        if (x % 5 == 0):
            fb += 'Buzz'
        print(fb)

if __name__ == '__main__':
    n = [3,3,3,3,30]
    fizzBuzz(n)
    