# encoding: utf-8
# module _signal
# from (built-in)
# by generator 1.147
"""
This module provides mechanisms to use signal handlers in Python.

Functions:

alarm() -- cause SIGALRM after a specified time [Unix only]
setitimer() -- cause a signal (described below) after a specified
               float time and the timer may restart then [Unix only]
getitimer() -- get current value of timer [Unix only]
signal() -- set the action for a given signal
getsignal() -- get the signal action for a given signal
pause() -- wait until a signal arrives [Unix only]
default_int_handler() -- default SIGINT handler

signal constants:
SIG_DFL -- used to refer to the system default handler
SIG_IGN -- used to ignore the signal
NSIG -- number of defined signals
SIGINT, SIGTERM, etc. -- signal numbers

itimer constants:
ITIMER_REAL -- decrements in real time, and delivers SIGALRM upon
               expiration
ITIMER_VIRTUAL -- decrements only when the process is executing,
               and delivers SIGVTALRM upon expiration
ITIMER_PROF -- decrements both when the process is executing and
               when the system is executing on behalf of the process.
               Coupled with ITIMER_VIRTUAL, this timer is usually
               used to profile the time spent by the application
               in user and kernel space. SIGPROF is delivered upon
               expiration.


*** IMPORTANT NOTICE ***
A signal handler function is called with two arguments:
the first is the signal number, the second is the interrupted stack frame.
"""
# no imports

# Variables with simple values

ITIMER_PROF = 2
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1

NSIG = 32

SIGABRT = 6
SIGALRM = 14
SIGBUS = 10
SIGCHLD = 20
SIGCONT = 19
SIGEMT = 7
SIGFPE = 8
SIGHUP = 1
SIGILL = 4
SIGINFO = 29
SIGINT = 2
SIGIO = 23
SIGIOT = 6
SIGKILL = 9
SIGPIPE = 13
SIGPROF = 27
SIGQUIT = 3
SIGSEGV = 11
SIGSTOP = 17
SIGSYS = 12
SIGTERM = 15
SIGTRAP = 5
SIGTSTP = 18
SIGTTIN = 21
SIGTTOU = 22
SIGURG = 16
SIGUSR1 = 30
SIGUSR2 = 31
SIGVTALRM = 26
SIGWINCH = 28
SIGXCPU = 24
SIGXFSZ = 25

SIG_BLOCK = 1
SIG_DFL = 0
SIG_IGN = 1
SIG_SETMASK = 3
SIG_UNBLOCK = 2

# functions

def alarm(*args, **kwargs): # real signature unknown
    """ Arrange for SIGALRM to arrive after the given number of seconds. """
    pass

def default_int_handler(*more): # real signature unknown; restored from __doc__
    """
    default_int_handler(...)
    
    The default handler for SIGINT installed by Python.
    It raises KeyboardInterrupt.
    """
    pass

def getitimer(*args, **kwargs): # real signature unknown
    """ Returns current value of given itimer. """
    pass

def getsignal(*args, **kwargs): # real signature unknown
    """
    Return the current action for the given signal.
    
    The return value can be:
      SIG_IGN -- if the signal is being ignored
      SIG_DFL -- if the default action for the signal is in effect
      None    -- if an unknown handler is in effect
      anything else -- the callable Python object used as a handler
    """
    pass

def pause(*args, **kwargs): # real signature unknown
    """ Wait until a signal arrives. """
    pass

def pthread_kill(*args, **kwargs): # real signature unknown
    """ Send a signal to a thread. """
    pass

def pthread_sigmask(*args, **kwargs): # real signature unknown
    """ Fetch and/or change the signal mask of the calling thread. """
    pass

def setitimer(*args, **kwargs): # real signature unknown
    """
    Sets given itimer (one of ITIMER_REAL, ITIMER_VIRTUAL or ITIMER_PROF).
    
    The timer will fire after value seconds and after that every interval seconds.
    The itimer can be cleared by setting seconds to zero.
    
    Returns old values as a tuple: (delay, interval).
    """
    pass

def set_wakeup_fd(fd, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_wakeup_fd(fd, *, warn_on_full_buffer=True) -> fd
    
    Sets the fd to be written to (with the signal number) when a signal
    comes in.  A library can use this to wakeup select or poll.
    The previous fd or -1 is returned.
    
    The fd must be non-blocking.
    """
    pass

def siginterrupt(*args, **kwargs): # real signature unknown
    """
    Change system call restart behaviour.
    
    If flag is False, system calls will be restarted when interrupted by
    signal sig, else system calls will be interrupted.
    """
    pass

def signal(): # real signature unknown; restored from __doc__
    """
    Set the action for the given signal.
    
    The action can be SIG_DFL, SIG_IGN, or a callable Python object.
    The previous action is returned.  See getsignal() for possible return values.
    
    *** IMPORTANT NOTICE ***
    A signal handler function is called with two arguments:
    the first is the signal number, the second is the interrupted stack frame.
    """
    pass

def sigpending(*args, **kwargs): # real signature unknown
    """
    Examine pending signals.
    
    Returns a set of signal numbers that are pending for delivery to
    the calling thread.
    """
    pass

def sigwait(*args, **kwargs): # real signature unknown
    """
    Wait for a signal.
    
    Suspend execution of the calling thread until the delivery of one of the
    signals specified in the signal set sigset.  The function accepts the signal
    and returns the signal number.
    """
    pass

# classes

class ItimerError(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x10dd30048>, 'find_spec': <classmethod object at 0x10dd30080>, 'find_module': <classmethod object at 0x10dd300b8>, 'create_module': <classmethod object at 0x10dd300f0>, 'exec_module': <classmethod object at 0x10dd30128>, 'get_code': <classmethod object at 0x10dd30198>, 'get_source': <classmethod object at 0x10dd30208>, 'is_package': <classmethod object at 0x10dd30278>, 'load_module': <classmethod object at 0x10dd302b0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_signal', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

