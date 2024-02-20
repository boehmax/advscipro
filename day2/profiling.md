# Answers to the Profiling Question from Day 2

## matmult.py

From running 
```
python -m cProfile matmult.py
```
I got:

  Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/1    0.000    0.000    3.299    3.299 {built-in method builtins.exec}
        1    3.106    3.106    3.299    3.299 matmult.py:1(<module>)
   125250    0.026    0.000    0.163    0.000 random.py:358(randint)
   125250    0.068    0.000    0.138    0.000 random.py:284(randrange)
      250    0.011    0.000    0.093    0.000 matmult.py:14(<listcomp>)
      250    0.011    0.000    0.092    0.000 matmult.py:9(<listcomp>)
   125250    0.041    0.000    0.055    0.000 random.py:235(_randbelow_with_getrandbits)
   375750    0.015    0.000    0.015    0.000 {built-in method _operator.index}


From which I conclude that all is very fast, but if one would like to imporve even more, they should go to line 14 and 9, since the total time devided by their n calls is the heighest here. Alternatively, go to random.py lines 358 and 284, and figure out a way, that the function doesnt need to be called 125250 times.

## euler72.py

From 
```
 kernprof -l -v euler72.py
```
I got: 
Total time: 0.00199792 s
File: euler72.py
Function: gen_primes at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def gen_primes(n):
     6         1          1.4      1.4      0.1      l = range(2,n)
     7         1          0.2      0.2      0.0      primes = []
     8       999        126.8      0.1      6.3      for j in range(0,len(l)):
     9       998         90.8      0.1      4.5          p = True
    10      2968        297.4      0.1     14.9          for d in primes:
    11      2967        654.4      0.2     32.8              if(d > sqrt(l[j])):
    12       167         16.7      0.1      0.8                  break
    13      2800        507.1      0.2     25.4              if(l[j] % d == 0):
    14       830         73.1      0.1      3.7                  p = False
    15       830         82.5      0.1      4.1                  break;
    16       998        111.9      0.1      5.6          if(p):
    17       168         35.8      0.2      1.8              primes.append(l[j])
    18                                           
    19         1          0.2      0.2      0.0      return primes

Total time: 0.06736 s
File: euler72.py
Function: factorize at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def factorize(n,primes):
    23      9999       1175.4      0.1      1.7      factors = []
    24      9999       1111.4      0.1      1.6      init_n = n
    25     96347      10687.2      0.1     15.9      for p in primes:
    26    118736      22132.2      0.2     32.9          while(n%p == 0):
    27     22389       3256.2      0.1      4.8              n = n/p
    28     22389       4166.5      0.2      6.2              factors.append(p)
    29     96347      19405.7      0.2     28.8          if(p > sqrt(n)):
    30      9999       1284.1      0.1      1.9              break
    31      9999       1341.8      0.1      2.0      if(n > 1):
    32      9596       1730.6      0.2      2.6          factors.append(n)
    33      9999       1068.9      0.1      1.6      return factors

Total time: 0.152619 s
File: euler72.py
Function: fast_phi at line 50

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    50                                           @profile
    51                                           def fast_phi(n,primes):
    52      9999     135219.0     13.5     88.6      factors = factorize(n,primes)
    53      9999       1506.6      0.2      1.0      phi = factors[0]-1
    54     31985       5905.7      0.2      3.9      for i in range(1,len(factors)):
    55     21986       4135.6      0.2      2.7          if(factors[i] == factors[i-1]):
    56      7685       2140.0      0.3      1.4              phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    57                                                   else:
    58     14301       2722.1      0.2      1.8              phi *= (factors[i]-1)
    59      9999        990.5      0.1      0.6      return phi

I therefore would start optimzing this code in line 52 first and formost.

## Improving matmult.py
By implementing NumPy (was this allowed?) I could increase performance from 3.299s to 0.254s.
 
 Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       15    0.001    0.000    0.436    0.029 __init__.py:1(<module>)
    117/1    0.001    0.000    0.254    0.254 {built-in method builtins.exec}
        1    0.012    0.012    0.254    0.254 matmult.py:1(<module>)
    155/1    0.001    0.000    0.235    0.235 <frozen importlib._bootstrap>:1165(_find_and_load)
    155/1    0.001    0.000    0.235    0.235 <frozen importlib._bootstrap>:1120(_find_and_load_unlocked)
    143/1    0.000    0.000    0.234    0.234 <frozen importlib._bootstrap>:666(_load_unlocked)
    115/1    0.000    0.000    0.234    0.234 <frozen importlib._bootstrap_external>:934(exec_module)
    380/2    0.000    0.000    0.233    0.117 <frozen importlib._bootstrap>:233(_call_with_frames_removed)
    375/9    0.000    0.000    0.227    0.025 {built-in method builtins.__import__}
   250/40    0.000    0.000    0.226    0.006 <frozen importlib._bootstrap>:1207(_handle_fromlist)
        1    0.000    0.000    0.101    0.101 _distributor_init.py:1(<module>)
        1    0.075    0.075    0.075    0.075 {built-in method mkl._py_mkl_service.get_version}
   
