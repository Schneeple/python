import numpy as np
from SolverSuite import SolverSuite
from pprint import pprint as pp
from LinAlg import BacksU

A = np.array([[0.091, 0.09814, 0.0095],[1,1,0.10]])
b = np.array([0.,0,1,-2.])

print BacksU(A,b)

exit()



LA = SolverSuite.LinearAlgebra()

A = np.array([[2.,2,5,2],[1,2,3,2],[5,2,7,4],[-5,3,-1,4]])
b = np.array([1,6,3,1.])

print "INITIAL MATRIX:"
pp(np.concatenate((A, b.reshape(-1,1)), axis=1))
print

A, b = LA.GaussU(A, b)
b_hold = b.reshape(-1,1)
print "UT MATRIX:"
pp(np.concatenate((A, b_hold), axis=1))
print 

print "RREF MATRIX:"
solns = LA.BacksU(A, b)
solns_hold = solns.reshape(-1,1)
pp(np.concatenate((np.eye(len(b)), solns_hold), axis=1))
print 

print "SOLUTIONS:"

pp(solns)