# encoding: utf-8
# module math
# from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/math.cpython-37m-darwin.so
# by generator 1.147
"""
This module is always available.  It provides access to the
mathematical functions defined by the C standard.
"""
# no imports

# Variables with simple values
e = 2.718281828459045

inf = inf

nan = nan

pi = 3.141592653589793

tau = 6.283185307179586

# functions

def acos(*args, **kwargs): # real signature unknown
    """ Return the arc cosine (measured in radians) of x. """
    pass

def acosh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic cosine of x. """
    pass

def asin(*args, **kwargs): # real signature unknown
    """ Return the arc sine (measured in radians) of x. """
    pass

def asinh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic sine of x. """
    pass

def atan(*args, **kwargs): # real signature unknown
    """ Return the arc tangent (measured in radians) of x. """
    pass

def atan2(*args, **kwargs): # real signature unknown
    """
    Return the arc tangent (measured in radians) of y/x.
    
    Unlike atan(y/x), the signs of both x and y are considered.
    """
    pass

def atanh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic tangent of x. """
    pass

def ceil(*args, **kwargs): # real signature unknown
    """
    Return the ceiling of x as an Integral.
    
    This is the smallest integer >= x.
    """
    pass

def copysign(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return a float with the magnitude (absolute value) of x but the sign of y.
    
    On platforms that support signed zeros, copysign(1.0, -0.0)
    returns -1.0.
    """
    pass

def cos(*args, **kwargs): # real signature unknown
    """ Return the cosine of x (measured in radians). """
    pass

def cosh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic cosine of x. """
    pass

def degrees(*args, **kwargs): # real signature unknown
    """ Convert angle x from radians to degrees. """
    pass

def erf(*args, **kwargs): # real signature unknown
    """ Error function at x. """
    pass

def erfc(*args, **kwargs): # real signature unknown
    """ Complementary error function at x. """
    pass

def exp(*args, **kwargs): # real signature unknown
    """ Return e raised to the power of x. """
    pass

def expm1(*args, **kwargs): # real signature unknown
    """
    Return exp(x)-1.
    
    This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    """
    pass

def fabs(*args, **kwargs): # real signature unknown
    """ Return the absolute value of the float x. """
    pass

def factorial(*args, **kwargs): # real signature unknown
    """
    Find x!.
    
    Raise a ValueError if x is negative or non-integral.
    """
    pass

def floor(*args, **kwargs): # real signature unknown
    """
    Return the floor of x as an Integral.
    
    This is the largest integer <= x.
    """
    pass

def fmod(x, y): # real signature unknown; restored from __doc__
    """
    Return fmod(x, y), according to platform C.
    
    x % y may differ.
    """
    pass

def frexp(*args, **kwargs): # real signature unknown
    """
    Return the mantissa and exponent of x, as pair (m, e).
    
    m is a float and e is an int, such that x = m * 2.**e.
    If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    """
    pass

def fsum(*args, **kwargs): # real signature unknown
    """
    Return an accurate floating point sum of values in the iterable seq.
    
    Assumes IEEE-754 floating point arithmetic.
    """
    pass

def gamma(*args, **kwargs): # real signature unknown
    """ Gamma function at x. """
    pass

def gcd(*args, **kwargs): # real signature unknown
    """ greatest common divisor of x and y """
    pass

def hypot(*args, **kwargs): # real signature unknown
    """ Return the Euclidean distance, sqrt(x*x + y*y). """
    pass

def isclose(*args, **kwargs): # real signature unknown
    """
    Determine whether two floating point numbers are close in value.
    
      rel_tol
        maximum difference for being considered "close", relative to the
        magnitude of the input values
      abs_tol
        maximum difference for being considered "close", regardless of the
        magnitude of the input values
    
    Return True if a is close in value to b, and False otherwise.
    
    For the values to be considered close, the difference between them
    must be smaller than at least one of the tolerances.
    
    -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
    is, NaN is not close to anything, even itself.  inf and -inf are
    only close to themselves.
    """
    pass

def isfinite(*args, **kwargs): # real signature unknown
    """ Return True if x is neither an infinity nor a NaN, and False otherwise. """
    pass

def isinf(*args, **kwargs): # real signature unknown
    """ Return True if x is a positive or negative infinity, and False otherwise. """
    pass

def isnan(*args, **kwargs): # real signature unknown
    """ Return True if x is a NaN (not a number), and False otherwise. """
    pass

def ldexp(*args, **kwargs): # real signature unknown
    """
    Return x * (2**i).
    
    This is essentially the inverse of frexp().
    """
    pass

def lgamma(*args, **kwargs): # real signature unknown
    """ Natural logarithm of absolute value of Gamma function at x. """
    pass

def log(x, base=None): # real signature unknown; restored from __doc__
    """
    log(x, [base=math.e])
    Return the logarithm of x to the given base.
    
    If the base not specified, returns the natural logarithm (base e) of x.
    """
    pass

def log10(*args, **kwargs): # real signature unknown
    """ Return the base 10 logarithm of x. """
    pass

def log1p(*args, **kwargs): # real signature unknown
    """
    Return the natural logarithm of 1+x (base e).
    
    The result is computed in a way which is accurate for x near zero.
    """
    pass

def log2(*args, **kwargs): # real signature unknown
    """ Return the base 2 logarithm of x. """
    pass

def modf(*args, **kwargs): # real signature unknown
    """
    Return the fractional and integer parts of x.
    
    Both results carry the sign of x and are floats.
    """
    pass

def pow(*args, **kwargs): # real signature unknown
    """ Return x**y (x to the power of y). """
    pass

def radians(*args, **kwargs): # real signature unknown
    """ Convert angle x from degrees to radians. """
    pass

def remainder(*args, **kwargs): # real signature unknown
    """
    Difference between x and the closest integer multiple of y.
    
    Return x - n*y where n*y is the closest integer multiple of y.
    In the case where x is exactly halfway between two multiples of
    y, the nearest even value of n is used. The result is always exact.
    """
    pass

def sin(*args, **kwargs): # real signature unknown
    """ Return the sine of x (measured in radians). """
    pass

def sinh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic sine of x. """
    pass

def sqrt(*args, **kwargs): # real signature unknown
    """ Return the square root of x. """
    pass

def tan(*args, **kwargs): # real signature unknown
    """ Return the tangent of x (measured in radians). """
    pass

def tanh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic tangent of x. """
    pass

def trunc(*args, **kwargs): # real signature unknown
    """
    Truncates the Real x to the nearest Integral toward 0.
    
    Uses the __trunc__ magic method.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x102c0b668>'

__spec__ = None # (!) real value is "ModuleSpec(name='math', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x102c0b668>, origin='/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/math.cpython-37m-darwin.so')"

