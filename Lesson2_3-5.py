def primes():
    current =1

    while True:
        current +=1
        simple = True
        for i in range(1,current):
            if current%i ==0 and i!=1 and i!=current :
                simple = False
        if (simple == True):
            yield current
