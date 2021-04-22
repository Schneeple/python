import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import IntProgress
from IPython.display import display

class IdealGas(object):
    def __init__(self , T = None , P = None , V = None , n = None , Z = 1 , R = 8.3145):
        self.R = R
        self.T = T
        self.n = n
        self.V = V
        self.P = P
        self.Z = Z
        
    def solve4Pressure(self):
        return self.Z*self.n*self.R * self.T / self.V
    
    def solve4MolarVolume(self):
        return self.P / ( self.Z * self.R * self.T )


class PengRobinson(object):
    def __init__(self  , T , p , Tc , Pc , w , P = 1e6 , R = 8.3145 ):
        self.R = R
        self.T = T
        self.p = p
        self.Tc = Tc
        self.Pc = Pc
        self.w = w
        self.Tr = T / Tc
        self.P = P
         
    def a(self):
        return self.ac() * self.alpha()
    
    def ac(self):
        return 0.45723553 * (self.R**2 * self.Tc**2) / self.Pc
    
    def b(self):
        return 0.07779607 * self.R * (self.Tc / self.Pc)
        
    def alpha(self):
        return ( 1 + ( self.K() * ( 1 - self.Tr**0.5 ) ) ) ** 2
    
    def K(self):
        return 0.37464 + ( 1.54226 * self.w ) - ( 0.26992 * self.w**2 )
    
    def Psat(self):
        left =  ( ( self.R * self.T * self.p ) / ( 1 - ( self.b() * self.p ) ) ) 
        right = ( ( self.a() * self.p**2 ) / ( 1 + ( 2 * self.b() * self.p ) - ( self.b()**2 * self.p**2 ) ) )
        return left - right
    
    def solve4molarDensity(self , p_step = 0.001 ,  e = 100):
        p_guess = self.p
        f = IntProgress(min=0, max=100) # instantiate the bar
        display(f) # display the bar
        while e > 0.1:
            p_guess += p_step
            P_calc = PengRobinson(self.T , p_guess , self.Tc , self.Pc , self.w).Psat()
            e = ( self.P - P_calc) / self.P * 100
            f.value += 1
            
        self.p = p_guess
        return p_guess
    
    def ZEquation(self):
        Z = sym.Symbol('Z' , positive=True)
        equation = Z**3 - ( ( 1- self.B() )*Z**2 ) + ( ( self.A() - 3 * self.B()**2 - 2 * self.B() ) * Z ) - ( self.A()*self.B() - self.B()**2 - self.B()**3 )
        return equation
    
    def ZSolver(self):
        Z = sym.Symbol('Z')
        return np.array( list(sym.solveset( self.ZEquation() , domain=sym.S.Reals ) ) )
        
        
    def A(self):
        return ( self.a() * self.P ) / ( self.R**2 * self.T**2 )
    
    def B(self):
        return ( self.P * self.b() ) / ( self.R * self.T )
    
    def fugacity(self):
        A = self.A()
        B = self.B()
        Z = float( self.ZSolver()[0] )
        return np.exp( -1* np.log( Z - B ) - ( A / (B * (8**0.5) ) ) * np.log( ( Z + ((1+(2**0.5))* B) ) / (( Z + ((1-(2**0.5))* B) ) ) ) + Z - 1 ) * self.P
  
    def RackettEquation(self):
        Zc = float( self.ZSolver()[0] )
        Vc = Zc * self.R * self.Tc / self.Pc
        return Vc * Zc**((1-self.Tr)**0.2857)
    

if __name__ == "__main__":
    
    init = PengRobinson(T = 338.15 , p = 35.67 , Tc = 154.6 , Pc = 5.043e6 , w = 0.022 , P = 8.7e5)
    f = init.fugacity()
    print( init.ZSolver() )
    
    # Poynting Equation f^L = Psat of a liquid
    PSAT = f
    init = PengRobinson(T = 338.15 , p = 35.67 , Tc = 647.3 , Pc = 22.12e6 , w = 0.022 , P = PSAT)
#     print( 32* init.solve4molarDensity() )
    print( init.RackettEquation()**-1 / 32 / 1000 )
    
    