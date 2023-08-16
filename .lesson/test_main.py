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
        for i in range(1,3) :
            p = i*0.3
            rat = (1-p)/p
            prob = ( rat**5 - rat**10 ) / ( 1 - rat**10 )
            inputs.append((5,10,p,100,))
            myvar = randomvar( prob, variance=prob*(1-prob)/100, dist="conf_lim", vmin=0, vmax=1, dof=99, limit=0.9 )
            variables.append( myvar )
        assert( check_func('sample_mean',inputs, variables ) )
