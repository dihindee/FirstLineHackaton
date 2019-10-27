# encoding: utf-8
# module termios
# from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/termios.cpython-37m-darwin.so
# by generator 1.147
"""
This module provides an interface to the Posix calls for tty I/O control.
For a complete description of these calls, see the Posix or Unix manual
pages. It is only available for those Unix versions that support Posix
termios style tty I/O control.

All functions in this module take a file descriptor fd as their first
argument. This can be an integer file descriptor, such as returned by
sys.stdin.fileno(), or a file object, such as sys.stdin itself.
"""
# no imports

# Variables with simple values

B0 = 0

B110 = 110
B115200 = 115200
B1200 = 1200
B134 = 134
B150 = 150
B1800 = 1800
B19200 = 19200

B200 = 200
B230400 = 230400
B2400 = 2400

B300 = 300
B38400 = 38400

B4800 = 4800

B50 = 50
B57600 = 57600

B600 = 600

B75 = 75

B9600 = 9600

BRKINT = 2

BS0 = 0
BS1 = 32768
BSDLY = 32768

CDSUSP = 25

CEOF = 4
CEOL = 255
CEOT = 4
CERASE = 127

CFLUSH = 15

CINTR = 3

CKILL = 21

CLNEXT = 22
CLOCAL = 32768

CQUIT = 28

CR0 = 0
CR1 = 4096
CR2 = 8192
CR3 = 12288
CRDLY = 12288
CREAD = 2048
CRPRNT = 18
CRTSCTS = 196608

CS5 = 0
CS6 = 256
CS7 = 512
CS8 = 768
CSIZE = 768
CSTART = 17
CSTOP = 19
CSTOPB = 1024
CSUSP = 26

CWERASE = 23

ECHO = 8
ECHOCTL = 64
ECHOE = 2
ECHOK = 4
ECHOKE = 1
ECHONL = 16
ECHOPRT = 32

EXTA = 19200
EXTB = 38400

FF0 = 0
FF1 = 16384
FFDLY = 16384

FIOASYNC = 2147772029
FIOCLEX = 536897025
FIONBIO = 2147772030
FIONCLEX = 536897026
FIONREAD = 1074030207

FLUSHO = 8388608

HUPCL = 16384

ICANON = 256
ICRNL = 256

IEXTEN = 1024

IGNBRK = 1
IGNCR = 128
IGNPAR = 4

IMAXBEL = 8192

INLCR = 64
INPCK = 16

ISIG = 128
ISTRIP = 32

IXANY = 2048
IXOFF = 1024
IXON = 512

NCCS = 20

NL0 = 0
NL1 = 256
NLDLY = 768

NOFLSH = 2147483648

OCRNL = 16

OFDEL = 131072
OFILL = 128

ONLCR = 2
ONLRET = 64
ONOCR = 32

OPOST = 1

PARENB = 4096
PARMRK = 8
PARODD = 8192

PENDIN = 536870912

TAB0 = 0
TAB1 = 1024
TAB2 = 2048
TAB3 = 4
TABDLY = 3076

TCIFLUSH = 1
TCIOFF = 3
TCIOFLUSH = 3
TCION = 4
TCOFLUSH = 2
TCOOFF = 1
TCOON = 2
TCSADRAIN = 1
TCSAFLUSH = 2
TCSANOW = 0
TCSASOFT = 16

TIOCCONS = 2147775586
TIOCEXCL = 536900621
TIOCGETD = 1074033690
TIOCGPGRP = 1074033783
TIOCGWINSZ = 1074295912
TIOCMBIC = 2147775595
TIOCMBIS = 2147775596
TIOCMGET = 1074033770
TIOCMSET = 2147775597

TIOCM_CAR = 64
TIOCM_CD = 64
TIOCM_CTS = 32
TIOCM_DSR = 256
TIOCM_DTR = 2
TIOCM_LE = 1
TIOCM_RI = 128
TIOCM_RNG = 128
TIOCM_RTS = 4
TIOCM_SR = 16
TIOCM_ST = 8

TIOCNOTTY = 536900721
TIOCNXCL = 536900622
TIOCOUTQ = 1074033779
TIOCPKT = 2147775600

TIOCPKT_DATA = 0
TIOCPKT_DOSTOP = 32
TIOCPKT_FLUSHREAD = 1
TIOCPKT_FLUSHWRITE = 2
TIOCPKT_NOSTOP = 16
TIOCPKT_START = 8
TIOCPKT_STOP = 4

TIOCSCTTY = 536900705
TIOCSETD = 2147775515
TIOCSPGRP = 2147775606
TIOCSTI = 2147578994
TIOCSWINSZ = 2148037735

TOSTOP = 4194304

VDISCARD = 15

VEOF = 0
VEOL = 1
VEOL2 = 2
VERASE = 3

VINTR = 8

VKILL = 5

VLNEXT = 14

VMIN = 16

VQUIT = 9

VREPRINT = 6

VSTART = 12
VSTOP = 13
VSUSP = 10

VT0 = 0
VT1 = 65536
VTDLY = 65536
VTIME = 17

VWERASE = 4

# functions

def tcdrain(fd): # real signature unknown; restored from __doc__
    """
    tcdrain(fd) -> None
    
    Wait until all output written to file descriptor fd has been transmitted.
    """
    pass

def tcflow(fd, action): # real signature unknown; restored from __doc__
    """
    tcflow(fd, action) -> None
    
    Suspend or resume input or output on file descriptor fd.
    The action argument can be termios.TCOOFF to suspend output,
    termios.TCOON to restart output, termios.TCIOFF to suspend input,
    or termios.TCION to restart input.
    """
    pass

def tcflush(fd, queue): # real signature unknown; restored from __doc__
    """
    tcflush(fd, queue) -> None
    
    Discard queued data on file descriptor fd.
    The queue selector specifies which queue: termios.TCIFLUSH for the input
    queue, termios.TCOFLUSH for the output queue, or termios.TCIOFLUSH for
    both queues.
    """
    pass

def tcgetattr(fd): # real signature unknown; restored from __doc__
    """
    tcgetattr(fd) -> list_of_attrs
    
    Get the tty attributes for file descriptor fd, as follows:
    [iflag, oflag, cflag, lflag, ispeed, ospeed, cc] where cc is a list
    of the tty special characters (each a string of length 1, except the items
    with indices VMIN and VTIME, which are integers when these fields are
    defined).  The interpretation of the flags and the speeds as well as the
    indexing in the cc array must be done using the symbolic constants defined
    in this module.
    """
    pass

def tcsendbreak(fd, duration): # real signature unknown; restored from __doc__
    """
    tcsendbreak(fd, duration) -> None
    
    Send a break on file descriptor fd.
    A zero duration sends a break for 0.25-0.5 seconds; a nonzero duration
    has a system dependent meaning.
    """
    pass

def tcsetattr(fd, when, attributes): # real signature unknown; restored from __doc__
    """
    tcsetattr(fd, when, attributes) -> None
    
    Set the tty attributes for file descriptor fd.
    The attributes to be set are taken from the attributes argument, which
    is a list like the one returned by tcgetattr(). The when argument
    determines when the attributes are changed: termios.TCSANOW to
    change immediately, termios.TCSADRAIN to change after transmitting all
    queued output, or termios.TCSAFLUSH to change after transmitting all
    queued output and discarding all queued input.
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x105038668>'

__spec__ = None # (!) real value is "ModuleSpec(name='termios', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x105038668>, origin='/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/termios.cpython-37m-darwin.so')"

