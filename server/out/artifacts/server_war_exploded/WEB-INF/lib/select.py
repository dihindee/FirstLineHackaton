# encoding: utf-8
# module select
# from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/select.cpython-37m-darwin.so
# by generator 1.147
"""
This module supports asynchronous I/O on multiple file descriptors.

*** IMPORTANT NOTICE ***
On Windows, only sockets are supported; on Unix, all file descriptors.
"""
# no imports

# Variables with simple values

KQ_EV_ADD = 1
KQ_EV_CLEAR = 32
KQ_EV_DELETE = 2
KQ_EV_DISABLE = 8
KQ_EV_ENABLE = 4
KQ_EV_EOF = 32768
KQ_EV_ERROR = 16384
KQ_EV_FLAG1 = 8192
KQ_EV_ONESHOT = 16
KQ_EV_SYSFLAGS = 61440

KQ_FILTER_AIO = -3
KQ_FILTER_PROC = -5
KQ_FILTER_READ = -1
KQ_FILTER_SIGNAL = -6
KQ_FILTER_TIMER = -7
KQ_FILTER_VNODE = -4
KQ_FILTER_WRITE = -2

KQ_NOTE_ATTRIB = 8
KQ_NOTE_CHILD = 4
KQ_NOTE_DELETE = 1
KQ_NOTE_EXEC = 536870912
KQ_NOTE_EXIT = 2147483648
KQ_NOTE_EXTEND = 4
KQ_NOTE_FORK = 1073741824
KQ_NOTE_LINK = 16
KQ_NOTE_LOWAT = 1
KQ_NOTE_PCTRLMASK = -1048576
KQ_NOTE_PDATAMASK = 1048575
KQ_NOTE_RENAME = 32
KQ_NOTE_REVOKE = 64
KQ_NOTE_TRACK = 1
KQ_NOTE_TRACKERR = 2
KQ_NOTE_WRITE = 2

PIPE_BUF = 512

POLLERR = 8
POLLHUP = 16
POLLIN = 1
POLLNVAL = 32
POLLOUT = 4
POLLPRI = 2
POLLRDBAND = 128
POLLRDNORM = 64
POLLWRBAND = 256
POLLWRNORM = 4

# functions

def poll(*args, **kwargs): # real signature unknown
    """
    Returns a polling object, which supports registering and
    unregistering file descriptors, and then polling them for I/O events.
    """
    pass

def select(rlist, wlist, xlist, timeout=None): # real signature unknown; restored from __doc__
    """
    select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)
    
    Wait until one or more file descriptors are ready for some kind of I/O.
    The first three arguments are sequences of file descriptors to be waited for:
    rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an ``exceptional condition''
    If only one kind of condition is required, pass [] for the other lists.
    A file descriptor is either a socket or file object, or a small integer
    gotten from a fileno() method call on one of those.
    
    The optional 4th argument specifies a timeout in seconds; it may be
    a floating point number to specify fractions of seconds.  If it is absent
    or None, the call will never time out.
    
    The return value is a tuple of three lists corresponding to the first three
    arguments; each contains the subset of the corresponding file descriptors
    that are ready.
    
    *** IMPORTANT NOTICE ***
    On Windows, only sockets are supported; on Unix, all file
    descriptors can be used.
    """
    pass

# classes

class error(Exception):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """second exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""



class kevent(object):
    """
    kevent(ident, filter=KQ_FILTER_READ, flags=KQ_EV_ADD, fflags=0, data=0, udata=0)
    
    This object is the equivalent of the struct kevent for the C API.
    
    See the kqueue manpage for more detailed information about the meaning
    of the arguments.
    
    One minor note: while you might hope that udata could store a
    reference to a python object, it cannot, because it is impossible to
    keep a proper reference count of the object once it's passed into the
    kernel. Therefore, I have restricted it to only storing an integer.  I
    recommend ignoring it and simply using the 'ident' field to key off
    of. You could also set up a dictionary on the python side to store a
    udata->object mapping.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, ident, filter=None, flags=None, fflags=0, data=0, udata=0): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fflags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ident = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    udata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class kqueue(object):
    """
    Kqueue syscall wrapper.
    
    For example, to start watching a socket for input:
    >>> kq = kqueue()
    >>> sock = socket()
    >>> sock.connect((host, port))
    >>> kq.control([kevent(sock, KQ_FILTER_WRITE, KQ_EV_ADD)], 0)
    
    To wait one second for it to become writeable:
    >>> kq.control(None, 1, 1000)
    
    To stop listening:
    >>> kq.control([kevent(sock, KQ_FILTER_WRITE, KQ_EV_DELETE)], 0)
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None
        
        Close the kqueue control file descriptor. Further operations on the kqueue
        object will raise an exception.
        """
        pass

    def control(self, changelist, max_events, timeout=None): # real signature unknown; restored from __doc__
        """
        control(changelist, max_events[, timeout=None]) -> eventlist
        
        Calls the kernel kevent function.
        - changelist must be an iterable of kevent objects describing the changes
          to be made to the kernel's watch list or None.
        - max_events lets you specify the maximum number of events that the
          kernel will return.
        - timeout is the maximum time to wait in seconds, or else None,
          to wait forever. timeout accepts floats for smaller timeouts, too.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> int
        
        Return the kqueue control file descriptor.
        """
        return 0

    @classmethod
    def fromfd(cls, fd): # real signature unknown; restored from __doc__
        """
        fromfd(fd) -> kqueue
        
        Create a kqueue object from a given control fd.
        """
        return kqueue

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the kqueue handler is closed"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x10914c6d8>'

__spec__ = None # (!) real value is "ModuleSpec(name='select', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x10914c6d8>, origin='/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/select.cpython-37m-darwin.so')"

