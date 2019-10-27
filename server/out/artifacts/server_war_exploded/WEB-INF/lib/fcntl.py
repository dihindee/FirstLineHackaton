# encoding: utf-8
# module fcntl
# from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/fcntl.cpython-37m-darwin.so
# by generator 1.147
"""
This module performs file control and I/O control on file 
descriptors.  It is an interface to the fcntl() and ioctl() Unix
routines.  File descriptors can be obtained with the fileno() method of
a file or socket object.
"""
# no imports

# Variables with simple values

FASYNC = 64

FD_CLOEXEC = 1

F_DUPFD = 0

F_DUPFD_CLOEXEC = 67

F_FULLFSYNC = 51
F_GETFD = 1
F_GETFL = 3
F_GETLK = 7
F_GETOWN = 5
F_NOCACHE = 48
F_RDLCK = 1
F_SETFD = 2
F_SETFL = 4
F_SETLK = 8
F_SETLKW = 9
F_SETOWN = 6
F_UNLCK = 2
F_WRLCK = 3

LOCK_EX = 2
LOCK_NB = 4
LOCK_SH = 1
LOCK_UN = 8

# functions

def fcntl(*args, **kwargs): # real signature unknown
    """
    Perform the operation `cmd` on file descriptor fd.
    
    The values used for `cmd` are operating system dependent, and are available
    as constants in the fcntl module, using the same names as used in
    the relevant C header files.  The argument arg is optional, and
    defaults to 0; it may be an int or a string.  If arg is given as a string,
    the return value of fcntl is a string of that length, containing the
    resulting value put in the arg buffer by the operating system.  The length
    of the arg string is not allowed to exceed 1024 bytes.  If the arg given
    is an integer or if none is specified, the result value is an integer
    corresponding to the return value of the fcntl call in the C code.
    """
    pass

def flock(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Perform the lock operation `operation` on file descriptor `fd`.
    
    See the Unix manual page for flock(2) for details (On some systems, this
    function is emulated using fcntl()).
    """
    pass

def ioctl(*args, **kwargs): # real signature unknown
    """
    Perform the operation `request` on file descriptor `fd`.
    
    The values used for `request` are operating system dependent, and are available
    as constants in the fcntl or termios library modules, using the same names as
    used in the relevant C header files.
    
    The argument `arg` is optional, and defaults to 0; it may be an int or a
    buffer containing character data (most likely a string or an array).
    
    If the argument is a mutable buffer (such as an array) and if the
    mutate_flag argument (which is only allowed in this case) is true then the
    buffer is (in effect) passed to the operating system and changes made by
    the OS will be reflected in the contents of the buffer after the call has
    returned.  The return value is the integer returned by the ioctl system
    call.
    
    If the argument is a mutable buffer and the mutable_flag argument is false,
    the behavior is as if a string had been passed.
    
    If the argument is an immutable buffer (most likely a string) then a copy
    of the buffer is passed to the operating system and the return value is a
    string of the same length containing whatever the operating system put in
    the buffer.  The length of the arg buffer in this case is not allowed to
    exceed 1024 bytes.
    
    If the arg given is an integer or if none is specified, the result value is
    an integer corresponding to the return value of the ioctl call in the C
    code.
    """
    pass

def lockf(*args, **kwargs): # real signature unknown
    """
    A wrapper around the fcntl() locking calls.
    
    `fd` is the file descriptor of the file to lock or unlock, and operation is one
    of the following values:
    
        LOCK_UN - unlock
        LOCK_SH - acquire a shared lock
        LOCK_EX - acquire an exclusive lock
    
    When operation is LOCK_SH or LOCK_EX, it can also be bitwise ORed with
    LOCK_NB to avoid blocking on lock acquisition.  If LOCK_NB is used and the
    lock cannot be acquired, an OSError will be raised and the exception will
    have an errno attribute set to EACCES or EAGAIN (depending on the operating
    system -- for portability, check for either value).
    
    `len` is the number of bytes to lock, with the default meaning to lock to
    EOF.  `start` is the byte offset, relative to `whence`, to that the lock
    starts.  `whence` is as with fileobj.seek(), specifically:
    
        0 - relative to the start of the file (SEEK_SET)
        1 - relative to the current buffer position (SEEK_CUR)
        2 - relative to the end of the file (SEEK_END)
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x10502b668>'

__spec__ = None # (!) real value is "ModuleSpec(name='fcntl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x10502b668>, origin='/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/fcntl.cpython-37m-darwin.so')"

