try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func 
           
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class check_class :
   def first_arg(s,n,p,m) :
      low, mean, up = sample_mean(s,n,p,m)
      return (( low - mean) / scipy.stats.norm.ppf(0.05) )**2

   def second_arg(s,n,p,m) :
      low, mean, up = sample_mean(s,n,p,m)
      return mean

   def third_arg(s,n,p,m) :
      low, mean, up = sample_mean(s,n,p,m)
      return (( up - mean) / scipy.stats.norm.ppf(0.95) )**2

class UnitTests(unittest.TestCase) :
    def test_random_walker(self) : 
        inputs, variables = [], []
        for s in range(1,4) : 
            for n in range(6,9) :
                for i in range(1,3) :
                    p = i*0.2
                    rat = (1-p)/p
                    prob = ( rat**s - rat**n ) / ( 1 - rat**n )
                    inputs.append((s,n,p,))
                    myvar = randomvar( prob, variance=prob*(1-prob), vmin=0, vmax=1, isinteger=True )
                    variables.append( myvar )
        assert( check_func('random_walker',inputs, variables ) )

    def test_mean(self) : 
        inputs, variables = [], []
        for m in range(1,3) :
            for s in range(1,4) :
                for n in range(6,9) :
                    for i in range(1,3) :
                        p = i*0.2
                        rat = (1-p)/p
                        prob = ( rat**s - rat**n ) / ( 1 - rat**n )
                        inputs.append((s,n,p,100*m,))
                        myvar = randomvar( prob, variance=prob*(1-prob)/(m*100), vmin=0, vmax=1, isinteger=False )
                        variables.append( myvar )
        assert( check_func('second_arg',inputs, variables, modname=check_class) )

    def test_lower(self) :
        inputs, variables = [], []
        for m in range(1,3) :
            for s in range(1,4) :
                for n in range(6,9) :
                    for i in range(1,3) :
                        p = i*0.2
                        rat = (1-p)/p
                        prob = ( rat**s - rat**n ) / ( 1 - rat**n )
                        inputs.append((s,n,p,100*m,))
                        myvar = randomvar( prob, dist="chi2", variance=prob*(1-prob)/(m*100), isinteger=False )
                        variables.append( myvar )
        assert( check_func('first_arg',inputs, variables, modname=check_class) )

    def test_upper(self) :
        inputs, variables = [], []
        for m in range(1,3) :
            for s in range(1,4) :
                for n in range(6,9) :
                    for i in range(1,3) :
                        p = i*0.2
                        rat = (1-p)/p
                        prob = ( rat**s - rat**n ) / ( 1 - rat**n )
                        inputs.append((s,n,p,100*m,))
                        myvar = randomvar( prob, dist="chi2", variance=prob*(1-prob)/(m*100), isinteger=False )
                        variables.append( myvar )
        assert( check_func('third_arg',inputs, variables, modname=check_class) )    
