# encoding: utf-8
# module posix
# from (built-in)
# by generator 1.147
"""
This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly
disguised Unix interface).  Refer to the library manual and
corresponding Unix manual entries for more information on calls.
"""
# no imports

# Variables with simple values

CLD_CONTINUED = 6
CLD_DUMPED = 3
CLD_EXITED = 1
CLD_TRAPPED = 4

EX_CANTCREAT = 73
EX_CONFIG = 78
EX_DATAERR = 65
EX_IOERR = 74
EX_NOHOST = 68
EX_NOINPUT = 66
EX_NOPERM = 77
EX_NOUSER = 67
EX_OK = 0
EX_OSERR = 71
EX_OSFILE = 72
EX_PROTOCOL = 76
EX_SOFTWARE = 70
EX_TEMPFAIL = 75
EX_UNAVAILABLE = 69
EX_USAGE = 64

F_LOCK = 1
F_OK = 0
F_TEST = 3
F_TLOCK = 2
F_ULOCK = 0

NGROUPS_MAX = 16

O_ACCMODE = 3
O_APPEND = 8
O_ASYNC = 64
O_CLOEXEC = 16777216
O_CREAT = 512
O_DIRECTORY = 1048576
O_DSYNC = 4194304
O_EXCL = 2048
O_EXLOCK = 32
O_NDELAY = 4
O_NOCTTY = 131072
O_NOFOLLOW = 256
O_NONBLOCK = 4
O_RDONLY = 0
O_RDWR = 2
O_SHLOCK = 16
O_SYNC = 128
O_TRUNC = 1024
O_WRONLY = 1

PRIO_PGRP = 1
PRIO_PROCESS = 0
PRIO_USER = 2

P_ALL = 0
P_PGID = 2
P_PID = 1

RTLD_GLOBAL = 8
RTLD_LAZY = 1
RTLD_LOCAL = 4
RTLD_NODELETE = 128
RTLD_NOLOAD = 16
RTLD_NOW = 2

R_OK = 4

SCHED_FIFO = 4
SCHED_OTHER = 1
SCHED_RR = 2

ST_NOSUID = 2
ST_RDONLY = 1

TMP_MAX = 308915776

WCONTINUED = 16

WEXITED = 4

WNOHANG = 1
WNOWAIT = 32

WSTOPPED = 8

WUNTRACED = 2

W_OK = 2

X_OK = 1

# functions

def abort(*args, **kwargs): # real signature unknown
    """
    Abort the interpreter immediately.
    
    This function 'dumps core' or otherwise fails in the hardest way possible
    on the hosting operating system.  This function never returns.
    """
    pass

def access(*args, **kwargs): # real signature unknown
    """
    Use the real uid/gid to test for access to a path.
    
      path
        Path to be tested; can be string, bytes, or a path-like object.
      mode
        Operating-system mode bitfield.  Can be F_OK to test existence,
        or the inclusive-OR of R_OK, W_OK, and X_OK.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      effective_ids
        If True, access will use the effective uid/gid instead of
        the real uid/gid.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        access will examine the symbolic link itself instead of the file
        the link points to.
    
    dir_fd, effective_ids, and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    
    Note that most operations will use the effective uid/gid, therefore this
      routine can be used in a suid/sgid environment to test if the invoking user
      has the specified access to the path.
    """
    pass

def chdir(*args, **kwargs): # real signature unknown
    """
    Change the current working directory to the specified path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def chflags(*args, **kwargs): # real signature unknown
    """
    Set file flags.
    
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, chflags will change flags on the symbolic link itself instead of the
      file the link points to.
    follow_symlinks may not be implemented on your platform.  If it is
    unavailable, using it will raise a NotImplementedError.
    """
    pass

def chmod(*args, **kwargs): # real signature unknown
    """
    Change the access permissions of a file.
    
      path
        Path to be modified.  May always be specified as a str, bytes, or a path-like object.
        On some platforms, path may also be specified as an open file descriptor.
        If this functionality is unavailable, using it raises an exception.
      mode
        Operating-system mode bitfield.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        chmod will modify the symbolic link itself instead of the file
        the link points to.
    
    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def chown(*args, **kwargs): # real signature unknown
    """
    Change the owner and group id of path to the numeric uid and gid.\
    
      path
        Path to be examined; can be string, bytes, a path-like object, or open-file-descriptor int.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        stat will examine the symbolic link itself instead of the file
        the link points to.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, chown will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def chroot(*args, **kwargs): # real signature unknown
    """ Change root directory to path. """
    pass

def close(*args, **kwargs): # real signature unknown
    """ Close a file descriptor. """
    pass

def closerange(*args, **kwargs): # real signature unknown
    """ Closes all file descriptors in [fd_low, fd_high), ignoring errors. """
    pass

def confstr(*args, **kwargs): # real signature unknown
    """ Return a string-valued system configuration variable. """
    pass

def cpu_count(*args, **kwargs): # real signature unknown
    """
    Return the number of CPUs in the system; return None if indeterminable.
    
    This number is not equivalent to the number of CPUs the current process can
    use.  The number of usable CPUs can be obtained with
    ``len(os.sched_getaffinity(0))``
    """
    pass

def ctermid(*args, **kwargs): # real signature unknown
    """ Return the name of the controlling terminal for this process. """
    pass

def device_encoding(*args, **kwargs): # real signature unknown
    """
    Return a string describing the encoding of a terminal's file descriptor.
    
    The file descriptor must be attached to a terminal.
    If the device is not a terminal, return None.
    """
    pass

def dup(*args, **kwargs): # real signature unknown
    """ Return a duplicate of a file descriptor. """
    pass

def dup2(*args, **kwargs): # real signature unknown
    """ Duplicate file descriptor. """
    pass

def execv(*args, **kwargs): # real signature unknown
    """
    Execute an executable path with arguments, replacing current process.
    
      path
        Path of executable file.
      argv
        Tuple or list of strings.
    """
    pass

def execve(*args, **kwargs): # real signature unknown
    """
    Execute an executable path with arguments, replacing current process.
    
      path
        Path of executable file.
      argv
        Tuple or list of strings.
      env
        Dictionary of strings mapping to strings.
    """
    pass

def fchdir(*args, **kwargs): # real signature unknown
    """
    Change to the directory of the given file descriptor.
    
    fd must be opened on a directory, not a file.
    Equivalent to os.chdir(fd).
    """
    pass

def fchmod(*args, **kwargs): # real signature unknown
    """
    Change the access permissions of the file given by file descriptor fd.
    
    Equivalent to os.chmod(fd, mode).
    """
    pass

def fchown(*args, **kwargs): # real signature unknown
    """
    Change the owner and group id of the file specified by file descriptor.
    
    Equivalent to os.chown(fd, uid, gid).
    """
    pass

def fork(*args, **kwargs): # real signature unknown
    """
    Fork a child process.
    
    Return 0 to child process and PID of child to parent process.
    """
    pass

def forkpty(*args, **kwargs): # real signature unknown
    """
    Fork a new process with a new pseudo-terminal as controlling tty.
    
    Returns a tuple of (pid, master_fd).
    Like fork(), return pid of 0 to the child process,
    and pid of child to the parent process.
    To both, return fd of newly opened pseudo-terminal.
    """
    pass

def fpathconf(*args, **kwargs): # real signature unknown
    """
    Return the configuration limit name for the file descriptor fd.
    
    If there is no limit, return -1.
    """
    pass

def fspath(*args, **kwargs): # real signature unknown
    """
    Return the file system path representation of the object.
    
    If the object is str or bytes, then allow it to pass through as-is. If the
    object defines __fspath__(), then return the result of that method. All other
    types raise a TypeError.
    """
    pass

def fstat(*args, **kwargs): # real signature unknown
    """
    Perform a stat system call on the given file descriptor.
    
    Like stat(), but for an open file descriptor.
    Equivalent to os.stat(fd).
    """
    pass

def fstatvfs(*args, **kwargs): # real signature unknown
    """
    Perform an fstatvfs system call on the given fd.
    
    Equivalent to statvfs(fd).
    """
    pass

def fsync(*args, **kwargs): # real signature unknown
    """ Force write of fd to disk. """
    pass

def ftruncate(*args, **kwargs): # real signature unknown
    """ Truncate a file, specified by file descriptor, to a specific length. """
    pass

def getcwd(*args, **kwargs): # real signature unknown
    """ Return a unicode string representing the current working directory. """
    pass

def getcwdb(*args, **kwargs): # real signature unknown
    """ Return a bytes string representing the current working directory. """
    pass

def getegid(*args, **kwargs): # real signature unknown
    """ Return the current process's effective group id. """
    pass

def geteuid(*args, **kwargs): # real signature unknown
    """ Return the current process's effective user id. """
    pass

def getgid(*args, **kwargs): # real signature unknown
    """ Return the current process's group id. """
    pass

def getgrouplist(user, group): # real signature unknown; restored from __doc__
    """
    getgrouplist(user, group) -> list of groups to which a user belongs
    
    Returns a list of groups to which a user belongs.
    
        user: username to lookup
        group: base group id of the user
    """
    return []

def getgroups(*args, **kwargs): # real signature unknown
    """ Return list of supplemental group IDs for the process. """
    pass

def getloadavg(*args, **kwargs): # real signature unknown
    """
    Return average recent system load information.
    
    Return the number of processes in the system run queue averaged over
    the last 1, 5, and 15 minutes as a tuple of three floats.
    Raises OSError if the load average was unobtainable.
    """
    pass

def getlogin(*args, **kwargs): # real signature unknown
    """ Return the actual login name. """
    pass

def getpgid(): # real signature unknown; restored from __doc__
    """ Call the system call getpgid(), and return the result. """
    pass

def getpgrp(*args, **kwargs): # real signature unknown
    """ Return the current process group id. """
    pass

def getpid(*args, **kwargs): # real signature unknown
    """ Return the current process id. """
    pass

def getppid(*args, **kwargs): # real signature unknown
    """
    Return the parent's process id.
    
    If the parent process has already exited, Windows machines will still
    return its id; others systems will return the id of the 'init' process (1).
    """
    pass

def getpriority(*args, **kwargs): # real signature unknown
    """ Return program scheduling priority. """
    pass

def getsid(pid): # real signature unknown; restored from __doc__
    """ Call the system call getsid(pid) and return the result. """
    pass

def getuid(*args, **kwargs): # real signature unknown
    """ Return the current process's user id. """
    pass

def get_blocking(fd): # real signature unknown; restored from __doc__
    """
    get_blocking(fd) -> bool
    
    Get the blocking mode of the file descriptor:
    False if the O_NONBLOCK flag is set, True if the flag is cleared.
    """
    return False

def get_inheritable(*args, **kwargs): # real signature unknown
    """ Get the close-on-exe flag of the specified file descriptor. """
    pass

def get_terminal_size(*args, **kwargs): # real signature unknown
    """
    Return the size of the terminal window as (columns, lines).
    
    The optional argument fd (default standard output) specifies
    which file descriptor should be queried.
    
    If the file descriptor is not connected to a terminal, an OSError
    is thrown.
    
    This function will only be defined if an implementation is
    available for this system.
    
    shutil.get_terminal_size is the high-level function which should 
    normally be used, os.get_terminal_size is the low-level implementation.
    """
    pass

def initgroups(username, gid): # real signature unknown; restored from __doc__
    """
    initgroups(username, gid) -> None
    
    Call the system initgroups() to initialize the group access list with all of
    the groups of which the specified username is a member, plus the specified
    group id.
    """
    pass

def isatty(*args, **kwargs): # real signature unknown
    """
    Return True if the fd is connected to a terminal.
    
    Return True if the file descriptor is an open file descriptor
    connected to the slave end of a terminal.
    """
    pass

def kill(*args, **kwargs): # real signature unknown
    """ Kill a process with a signal. """
    pass

def killpg(*args, **kwargs): # real signature unknown
    """ Kill a process group with a signal. """
    pass

def lchflags(*args, **kwargs): # real signature unknown
    """
    Set file flags.
    
    This function will not follow symbolic links.
    Equivalent to chflags(path, flags, follow_symlinks=False).
    """
    pass

def lchmod(*args, **kwargs): # real signature unknown
    """
    Change the access permissions of a file, without following symbolic links.
    
    If path is a symlink, this affects the link itself rather than the target.
    Equivalent to chmod(path, mode, follow_symlinks=False)."
    """
    pass

def lchown(*args, **kwargs): # real signature unknown
    """
    Change the owner and group id of path to the numeric uid and gid.
    
    This function will not follow symbolic links.
    Equivalent to os.chown(path, uid, gid, follow_symlinks=False).
    """
    pass

def link(*args, **kwargs): # real signature unknown
    """
    Create a hard link to a file.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    If follow_symlinks is False, and the last element of src is a symbolic
      link, link will create a link to the symbolic link itself instead of the
      file the link points to.
    src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
      platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    """
    pass

def listdir(*args, **kwargs): # real signature unknown
    """
    Return a list containing the names of the files in the directory.
    
    path can be specified as either str, bytes, or a path-like object.  If path is bytes,
      the filenames returned will also be bytes; in all other circumstances
      the filenames returned will be str.
    If path is None, uses the path='.'.
    On some platforms, path may also be specified as an open file descriptor;\
      the file descriptor must refer to a directory.
      If this functionality is unavailable, using it raises NotImplementedError.
    
    The list is in arbitrary order.  It does not include the special
    entries '.' and '..' even if they are present in the directory.
    """
    pass

def lockf(*args, **kwargs): # real signature unknown
    """
    Apply, test or remove a POSIX lock on an open file descriptor.
    
      fd
        An open file descriptor.
      command
        One of F_LOCK, F_TLOCK, F_ULOCK or F_TEST.
      length
        The number of bytes to lock, starting at the current position.
    """
    pass

def lseek(*args, **kwargs): # real signature unknown
    """
    Set the position of a file descriptor.  Return the new position.
    
    Return the new cursor position in number of bytes
    relative to the beginning of the file.
    """
    pass

def lstat(*args, **kwargs): # real signature unknown
    """
    Perform a stat system call on the given path, without following symbolic links.
    
    Like stat(), but do not follow symbolic links.
    Equivalent to stat(path, follow_symlinks=False).
    """
    pass

def major(*args, **kwargs): # real signature unknown
    """ Extracts a device major number from a raw device number. """
    pass

def makedev(*args, **kwargs): # real signature unknown
    """ Composes a raw device number from the major and minor device numbers. """
    pass

def minor(*args, **kwargs): # real signature unknown
    """ Extracts a device minor number from a raw device number. """
    pass

def mkdir(*args, **kwargs): # real signature unknown
    """
    Create a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    
    The mode argument is ignored on Windows.
    """
    pass

def mkfifo(*args, **kwargs): # real signature unknown
    """
    Create a "fifo" (a POSIX named pipe).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def mknod(*args, **kwargs): # real signature unknown
    """
    Create a node in the file system.
    
    Create a node in the file system (file, device special file or named pipe)
    at path.  mode specifies both the permissions to use and the
    type of node to be created, being combined (bitwise OR) with one of
    S_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO.  If S_IFCHR or S_IFBLK is set on mode,
    device defines the newly created device special file (probably using
    os.makedev()).  Otherwise device is ignored.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def nice(*args, **kwargs): # real signature unknown
    """ Add increment to the priority of process and return the new priority. """
    pass

def open(*args, **kwargs): # real signature unknown
    """
    Open a file for low level IO.  Returns a file descriptor (integer).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def openpty(*args, **kwargs): # real signature unknown
    """
    Open a pseudo-terminal.
    
    Return a tuple of (master_fd, slave_fd) containing open file descriptors
    for both the master and slave ends.
    """
    pass

def pathconf(*args, **kwargs): # real signature unknown
    """
    Return the configuration limit name for the file or directory path.
    
    If there is no limit, return -1.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def pipe(*args, **kwargs): # real signature unknown
    """
    Create a pipe.
    
    Returns a tuple of two file descriptors:
      (read_fd, write_fd)
    """
    pass

def pread(*args, **kwargs): # real signature unknown
    """
    Read a number of bytes from a file descriptor starting at a particular offset.
    
    Read length bytes from file descriptor fd, starting at offset bytes from
    the beginning of the file.  The file offset remains unchanged.
    """
    pass

def putenv(*args, **kwargs): # real signature unknown
    """ Change or add an environment variable. """
    pass

def pwrite(*args, **kwargs): # real signature unknown
    """
    Write bytes to a file descriptor starting at a particular offset.
    
    Write buffer to fd, starting at offset bytes from the beginning of
    the file.  Returns the number of bytes writte.  Does not change the
    current file offset.
    """
    pass

def read(*args, **kwargs): # real signature unknown
    """ Read from a file descriptor.  Returns a bytes object. """
    pass

def readlink(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    readlink(path, *, dir_fd=None) -> path
    
    Return a string representing the path to which the symbolic link points.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def readv(*args, **kwargs): # real signature unknown
    """
    Read from a file descriptor fd into an iterable of buffers.
    
    The buffers should be mutable buffers accepting bytes.
    readv will transfer data into each buffer until it is full
    and then move on to the next buffer in the sequence to hold
    the rest of the data.
    
    readv returns the total number of bytes read,
    which may be less than the total capacity of all the buffers.
    """
    pass

def register_at_fork(*args, **kwargs): # real signature unknown
    """
    Register callables to be called when forking a new process.
    
      before
        A callable to be called in the parent before the fork() syscall.
      after_in_child
        A callable to be called in the child after fork().
      after_in_parent
        A callable to be called in the parent after fork().
    
    'before' callbacks are called in reverse order.
    'after_in_child' and 'after_in_parent' callbacks are called in order.
    """
    pass

def remove(*args, **kwargs): # real signature unknown
    """
    Remove a file (same as unlink()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def rename(*args, **kwargs): # real signature unknown
    """
    Rename a file or directory.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def replace(*args, **kwargs): # real signature unknown
    """
    Rename a file or directory, overwriting the destination.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def rmdir(*args, **kwargs): # real signature unknown
    """
    Remove a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def scandir(*args, **kwargs): # real signature unknown
    """
    Return an iterator of DirEntry objects for given path.
    
    path can be specified as either str, bytes, or a path-like object.  If path
    is bytes, the names of yielded DirEntry objects will also be bytes; in
    all other circumstances they will be str.
    
    If path is None, uses the path='.'.
    """
    pass

def sched_get_priority_max(*args, **kwargs): # real signature unknown
    """ Get the maximum scheduling priority for policy. """
    pass

def sched_get_priority_min(*args, **kwargs): # real signature unknown
    """ Get the minimum scheduling priority for policy. """
    pass

def sched_yield(*args, **kwargs): # real signature unknown
    """ Voluntarily relinquish the CPU. """
    pass

def sendfile(out, in_, offset, count): # real signature unknown; restored from __doc__
    """
    sendfile(out, in, offset, count) -> byteswritten
    sendfile(out, in, offset, count[, headers][, trailers], flags=0)
                -> byteswritten
    Copy count bytes from file descriptor in to file descriptor out.
    """
    pass

def setegid(*args, **kwargs): # real signature unknown
    """ Set the current process's effective group id. """
    pass

def seteuid(*args, **kwargs): # real signature unknown
    """ Set the current process's effective user id. """
    pass

def setgid(*args, **kwargs): # real signature unknown
    """ Set the current process's group id. """
    pass

def setgroups(*args, **kwargs): # real signature unknown
    """ Set the groups of the current process to list. """
    pass

def setpgid(pid, pgrp): # real signature unknown; restored from __doc__
    """ Call the system call setpgid(pid, pgrp). """
    pass

def setpgrp(*args, **kwargs): # real signature unknown
    """ Make the current process the leader of its process group. """
    pass

def setpriority(*args, **kwargs): # real signature unknown
    """ Set program scheduling priority. """
    pass

def setregid(*args, **kwargs): # real signature unknown
    """ Set the current process's real and effective group ids. """
    pass

def setreuid(*args, **kwargs): # real signature unknown
    """ Set the current process's real and effective user ids. """
    pass

def setsid(): # real signature unknown; restored from __doc__
    """ Call the system call setsid(). """
    pass

def setuid(*args, **kwargs): # real signature unknown
    """ Set the current process's user id. """
    pass

def set_blocking(fd, blocking): # real signature unknown; restored from __doc__
    """
    set_blocking(fd, blocking)
    
    Set the blocking mode of the specified file descriptor.
    Set the O_NONBLOCK flag if blocking is False,
    clear the O_NONBLOCK flag otherwise.
    """
    pass

def set_inheritable(*args, **kwargs): # real signature unknown
    """ Set the inheritable flag of the specified file descriptor. """
    pass

def stat(*args, **kwargs): # real signature unknown
    """
    Perform a stat system call on the given path.
    
      path
        Path to be examined; can be string, bytes, a path-like object or
        open-file-descriptor int.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be a relative string; path will then be relative to
        that directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        stat will examine the symbolic link itself instead of the file
        the link points to.
    
    dir_fd and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    
    It's an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    """
    pass

def statvfs(*args, **kwargs): # real signature unknown
    """
    Perform a statvfs system call on the given path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def strerror(*args, **kwargs): # real signature unknown
    """ Translate an error code to a message string. """
    pass

def symlink(*args, **kwargs): # real signature unknown
    """
    Create a symbolic link pointing to src named dst.
    
    target_is_directory is required on Windows if the target is to be
      interpreted as a directory.  (On Windows, symlink requires
      Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
      target_is_directory is ignored on non-Windows platforms.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def sync(*args, **kwargs): # real signature unknown
    """ Force write of everything to disk. """
    pass

def sysconf(*args, **kwargs): # real signature unknown
    """ Return an integer-valued system configuration variable. """
    pass

def system(*args, **kwargs): # real signature unknown
    """ Execute the command in a subshell. """
    pass

def tcgetpgrp(*args, **kwargs): # real signature unknown
    """ Return the process group associated with the terminal specified by fd. """
    pass

def tcsetpgrp(*args, **kwargs): # real signature unknown
    """ Set the process group associated with the terminal specified by fd. """
    pass

def times(*args, **kwargs): # real signature unknown
    """
    Return a collection containing process timing information.
    
    The object returned behaves like a named tuple with these fields:
      (utime, stime, cutime, cstime, elapsed_time)
    All fields are floating point numbers.
    """
    pass

def truncate(*args, **kwargs): # real signature unknown
    """
    Truncate a file, specified by path, to a specific length.
    
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def ttyname(*args, **kwargs): # real signature unknown
    """
    Return the name of the terminal device connected to 'fd'.
    
      fd
        Integer file descriptor handle.
    """
    pass

def umask(*args, **kwargs): # real signature unknown
    """ Set the current numeric umask and return the previous umask. """
    pass

def uname(*args, **kwargs): # real signature unknown
    """
    Return an object identifying the current operating system.
    
    The object behaves like a named tuple with the following fields:
      (sysname, nodename, release, version, machine)
    """
    pass

def unlink(*args, **kwargs): # real signature unknown
    """
    Remove a file (same as remove()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def unsetenv(*args, **kwargs): # real signature unknown
    """ Delete an environment variable. """
    pass

def urandom(*args, **kwargs): # real signature unknown
    """ Return a bytes object containing random bytes suitable for cryptographic use. """
    pass

def utime(*args, **kwargs): # real signature unknown
    """
    Set the access and modified time of path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    
    If times is not None, it must be a tuple (atime, mtime);
        atime and mtime should be expressed as float seconds since the epoch.
    If ns is specified, it must be a tuple (atime_ns, mtime_ns);
        atime_ns and mtime_ns should be expressed as integer nanoseconds
        since the epoch.
    If times is None and ns is unspecified, utime uses the current time.
    Specifying tuples for both times and ns is an error.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, utime will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path
      as an open file descriptor.
    dir_fd and follow_symlinks may not be available on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def wait(*args, **kwargs): # real signature unknown
    """
    Wait for completion of a child process.
    
    Returns a tuple of information about the child process:
        (pid, status)
    """
    pass

def wait3(*args, **kwargs): # real signature unknown
    """
    Wait for completion of a child process.
    
    Returns a tuple of information about the child process:
      (pid, status, rusage)
    """
    pass

def wait4(*args, **kwargs): # real signature unknown
    """
    Wait for completion of a specific child process.
    
    Returns a tuple of information about the child process:
      (pid, status, rusage)
    """
    pass

def waitpid(*args, **kwargs): # real signature unknown
    """
    Wait for completion of a given child process.
    
    Returns a tuple of information regarding the child process:
        (pid, status)
    
    The options argument is ignored on Windows.
    """
    pass

def WCOREDUMP(*args, **kwargs): # real signature unknown
    """ Return True if the process returning status was dumped to a core file. """
    pass

def WEXITSTATUS(*args, **kwargs): # real signature unknown
    """ Return the process return code from status. """
    pass

def WIFCONTINUED(*args, **kwargs): # real signature unknown
    """
    Return True if a particular process was continued from a job control stop.
    
    Return True if the process returning status was continued from a
    job control stop.
    """
    pass

def WIFEXITED(*args, **kwargs): # real signature unknown
    """ Return True if the process returning status exited via the exit() system call. """
    pass

def WIFSIGNALED(*args, **kwargs): # real signature unknown
    """ Return True if the process returning status was terminated by a signal. """
    pass

def WIFSTOPPED(*args, **kwargs): # real signature unknown
    """ Return True if the process returning status was stopped. """
    pass

def write(*args, **kwargs): # real signature unknown
    """ Write a bytes object to a file descriptor. """
    pass

def writev(*args, **kwargs): # real signature unknown
    """
    Iterate over buffers, and write the contents of each to a file descriptor.
    
    Returns the total number of bytes written.
    buffers must be a sequence of bytes-like objects.
    """
    pass

def WSTOPSIG(*args, **kwargs): # real signature unknown
    """ Return the signal that stopped the process that provided the status value. """
    pass

def WTERMSIG(*args, **kwargs): # real signature unknown
    """ Return the signal that terminated the process that provided the status value. """
    pass

def _exit(*args, **kwargs): # real signature unknown
    """ Exit to the system with specified status, without normal exit processing. """
    pass

# classes

class DirEntry(object):
    # no doc
    def inode(self, *args, **kwargs): # real signature unknown
        """ Return inode of the entry; cached per entry. """
        pass

    def is_dir(self, *args, **kwargs): # real signature unknown
        """ Return True if the entry is a directory; cached per entry. """
        pass

    def is_file(self, *args, **kwargs): # real signature unknown
        """ Return True if the entry is a file; cached per entry. """
        pass

    def is_symlink(self, *args, **kwargs): # real signature unknown
        """ Return True if the entry is a symbolic link; cached per entry. """
        pass

    def stat(self, *args, **kwargs): # real signature unknown
        """ Return stat_result object for the entry; cached per entry. """
        pass

    def __fspath__(self, *args, **kwargs): # real signature unknown
        """ Returns the path for the entry. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the entry's base filename, relative to scandir() "path" argument"""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the entry's full path name; equivalent to os.path.join(scandir_path, entry.name)"""



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



class statvfs_result(tuple):
    """
    statvfs_result: Result from statvfs or fstatvfs.
    
    This object may be accessed either as a tuple of
      (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
    or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
    
    See os.statvfs for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    f_bavail = property(lambda self: 0)
    """:type: int"""

    f_bfree = property(lambda self: 0)
    """:type: int"""

    f_blocks = property(lambda self: 0)
    """:type: int"""

    f_bsize = property(lambda self: 0)
    """:type: int"""

    f_favail = property(lambda self: 0)
    """:type: int"""

    f_ffree = property(lambda self: 0)
    """:type: int"""

    f_files = property(lambda self: 0)
    """:type: int"""

    f_flag = property(lambda self: 0)
    """:type: int"""

    f_frsize = property(lambda self: 0)
    """:type: int"""

    f_fsid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_namemax = property(lambda self: 0)
    """:type: int"""


    n_fields = 11
    n_sequence_fields = 10
    n_unnamed_fields = 0


class stat_result(tuple):
    """
    stat_result: Result from stat, fstat, or lstat.
    
    This object may be accessed either as a tuple of
      (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
    
    Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
    or st_flags, they are available as attributes only.
    
    See os.stat for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    st_atime = property(lambda self: 0)
    """time of last access

    :type: int
    """

    st_atime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last access in nanoseconds"""

    st_birthtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of creation"""

    st_blksize = property(lambda self: 0)
    """blocksize for filesystem I/O

    :type: int
    """

    st_blocks = property(lambda self: 0)
    """number of blocks allocated

    :type: int
    """

    st_ctime = property(lambda self: 0)
    """time of last change

    :type: int
    """

    st_ctime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last change in nanoseconds"""

    st_dev = property(lambda self: 0)
    """device

    :type: int
    """

    st_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user defined flags for file"""

    st_gen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """generation number"""

    st_gid = property(lambda self: 0)
    """group ID of owner

    :type: int
    """

    st_ino = property(lambda self: 0)
    """inode

    :type: int
    """

    st_mode = property(lambda self: 0)
    """protection bits

    :type: int
    """

    st_mtime = property(lambda self: 0)
    """time of last modification

    :type: int
    """

    st_mtime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last modification in nanoseconds"""

    st_nlink = property(lambda self: 0)
    """number of hard links

    :type: int
    """

    st_rdev = property(lambda self: 0)
    """device type (if inode device)

    :type: int
    """

    st_size = property(lambda self: 0)
    """total size, in bytes

    :type: int
    """

    st_uid = property(lambda self: 0)
    """user ID of owner

    :type: int
    """


    n_fields = 22
    n_sequence_fields = 10
    n_unnamed_fields = 3


class terminal_size(tuple):
    """ A tuple of (columns, lines) for holding terminal window size """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """width of the terminal window in characters"""

    lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """height of the terminal window in characters"""


    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0


class times_result(tuple):
    """
    times_result: Result from os.times().
    
    This object may be accessed either as a tuple of
      (user, system, children_user, children_system, elapsed),
    or via the attributes user, system, children_user, children_system,
    and elapsed.
    
    See os.times for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    children_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time of children"""

    children_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time of children"""

    elapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """elapsed time since an arbitrary point in the past"""

    system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time"""

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


class uname_result(tuple):
    """
    uname_result: Result from os.uname().
    
    This object may be accessed either as a tuple of
      (sysname, nodename, release, version, machine),
    or via the attributes sysname, nodename, release, version, and machine.
    
    See os.uname for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    machine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """hardware identifier"""

    nodename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of machine on network (implementation-defined)"""

    release = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system release"""

    sysname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system name"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system version"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


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

confstr_names = {
    'CS_PATH': 1,
    'CS_XBS5_ILP32_OFF32_CFLAGS': 20,
    'CS_XBS5_ILP32_OFF32_LDFLAGS': 21,
    'CS_XBS5_ILP32_OFF32_LIBS': 22,
    'CS_XBS5_ILP32_OFF32_LINTFLAGS': 23,
    'CS_XBS5_ILP32_OFFBIG_CFLAGS': 24,
    'CS_XBS5_ILP32_OFFBIG_LDFLAGS': 25,
    'CS_XBS5_ILP32_OFFBIG_LIBS': 26,
    'CS_XBS5_ILP32_OFFBIG_LINTFLAGS': 27,
    'CS_XBS5_LP64_OFF64_CFLAGS': 28,
    'CS_XBS5_LP64_OFF64_LDFLAGS': 29,
    'CS_XBS5_LP64_OFF64_LIBS': 30,
    'CS_XBS5_LP64_OFF64_LINTFLAGS': 31,
    'CS_XBS5_LPBIG_OFFBIG_CFLAGS': 32,
    'CS_XBS5_LPBIG_OFFBIG_LDFLAGS': 33,
    'CS_XBS5_LPBIG_OFFBIG_LIBS': 34,
    'CS_XBS5_LPBIG_OFFBIG_LINTFLAGS': 35,
}

environ = {} # real value of type <class 'dict'> skipped

pathconf_names = {
    'PC_ALLOC_SIZE_MIN': 16,
    'PC_ASYNC_IO': 17,
    'PC_CHOWN_RESTRICTED': 7,
    'PC_FILESIZEBITS': 18,
    'PC_LINK_MAX': 1,
    'PC_MAX_CANON': 2,
    'PC_MAX_INPUT': 3,
    'PC_NAME_MAX': 4,
    'PC_NO_TRUNC': 8,
    'PC_PATH_MAX': 5,
    'PC_PIPE_BUF': 6,
    'PC_PRIO_IO': 19,
    'PC_REC_INCR_XFER_SIZE': 20,
    'PC_REC_MAX_XFER_SIZE': 21,
    'PC_REC_MIN_XFER_SIZE': 22,
    'PC_REC_XFER_ALIGN': 23,
    'PC_SYMLINK_MAX': 24,
    'PC_SYNC_IO': 25,
    'PC_VDISABLE': 9,
}

sysconf_names = {
    'SC_2_CHAR_TERM': 20,
    'SC_2_C_BIND': 18,
    'SC_2_C_DEV': 19,
    'SC_2_FORT_DEV': 21,
    'SC_2_FORT_RUN': 22,
    'SC_2_LOCALEDEF': 23,
    'SC_2_SW_DEV': 24,
    'SC_2_UPE': 25,
    'SC_2_VERSION': 17,
    'SC_AIO_LISTIO_MAX': 42,
    'SC_AIO_MAX': 43,
    'SC_AIO_PRIO_DELTA_MAX': 44,
    'SC_ARG_MAX': 1,
    'SC_ASYNCHRONOUS_IO': 28,
    'SC_ATEXIT_MAX': 107,
    'SC_BC_BASE_MAX': 9,
    'SC_BC_DIM_MAX': 10,
    'SC_BC_SCALE_MAX': 11,
    'SC_BC_STRING_MAX': 12,
    'SC_CHILD_MAX': 2,
    'SC_CLK_TCK': 3,
    'SC_COLL_WEIGHTS_MAX': 13,
    'SC_DELAYTIMER_MAX': 45,
    'SC_EXPR_NEST_MAX': 14,
    'SC_FSYNC': 38,
    'SC_GETGR_R_SIZE_MAX': 70,
    'SC_GETPW_R_SIZE_MAX': 71,
    'SC_IOV_MAX': 56,
    'SC_JOB_CONTROL': 6,
    'SC_LINE_MAX': 15,
    'SC_LOGIN_NAME_MAX': 73,
    'SC_MAPPED_FILES': 47,
    'SC_MEMLOCK': 30,
    'SC_MEMLOCK_RANGE': 31,
    'SC_MEMORY_PROTECTION': 32,
    'SC_MESSAGE_PASSING': 33,
    'SC_MQ_OPEN_MAX': 46,
    'SC_MQ_PRIO_MAX': 75,
    'SC_NGROUPS_MAX': 4,
    'SC_NPROCESSORS_CONF': 57,
    'SC_NPROCESSORS_ONLN': 58,
    'SC_OPEN_MAX': 5,
    'SC_PAGESIZE': 29,
    'SC_PAGE_SIZE': 29,
    'SC_PASS_MAX': 131,
    'SC_PRIORITIZED_IO': 34,
    'SC_PRIORITY_SCHEDULING': 35,
    'SC_REALTIME_SIGNALS': 36,
    'SC_RE_DUP_MAX': 16,
    'SC_RTSIG_MAX': 48,
    'SC_SAVED_IDS': 7,
    'SC_SEMAPHORES': 37,
    'SC_SEM_NSEMS_MAX': 49,
    'SC_SEM_VALUE_MAX': 50,
    'SC_SHARED_MEMORY_OBJECTS': 39,
    'SC_SIGQUEUE_MAX': 51,
    'SC_STREAM_MAX': 26,
    'SC_SYNCHRONIZED_IO': 40,
    'SC_THREADS': 96,
    'SC_THREAD_ATTR_STACKADDR': 82,
    'SC_THREAD_ATTR_STACKSIZE': 83,
    'SC_THREAD_DESTRUCTOR_ITERATIONS': 85,
    'SC_THREAD_KEYS_MAX': 86,
    'SC_THREAD_PRIORITY_SCHEDULING': 89,
    'SC_THREAD_PRIO_INHERIT': 87,
    'SC_THREAD_PRIO_PROTECT': 88,
    'SC_THREAD_PROCESS_SHARED': 90,
    'SC_THREAD_SAFE_FUNCTIONS': 91,
    'SC_THREAD_STACK_MIN': 93,
    'SC_THREAD_THREADS_MAX': 94,
    'SC_TIMERS': 41,
    'SC_TIMER_MAX': 52,
    'SC_TTY_NAME_MAX': 101,
    'SC_TZNAME_MAX': 27,
    'SC_VERSION': 8,
    'SC_XBS5_ILP32_OFF32': 122,
    'SC_XBS5_ILP32_OFFBIG': 123,
    'SC_XBS5_LP64_OFF64': 124,
    'SC_XBS5_LPBIG_OFFBIG': 125,
    'SC_XOPEN_CRYPT': 108,
    'SC_XOPEN_ENH_I18N': 109,
    'SC_XOPEN_LEGACY': 110,
    'SC_XOPEN_REALTIME': 111,
    'SC_XOPEN_REALTIME_THREADS': 112,
    'SC_XOPEN_SHM': 113,
    'SC_XOPEN_UNIX': 115,
    'SC_XOPEN_VERSION': 116,
    'SC_XOPEN_XCU_VERSION': 121,
}

_have_functions = [
    'HAVE_FCHDIR',
    'HAVE_FCHMOD',
    'HAVE_FCHOWN',
    'HAVE_FPATHCONF',
    'HAVE_FSTATVFS',
    'HAVE_FTRUNCATE',
    'HAVE_FUTIMES',
    'HAVE_LCHFLAGS',
    'HAVE_LCHMOD',
    'HAVE_LCHOWN',
    'HAVE_LSTAT',
    'HAVE_LUTIMES',
]

__spec__ = None # (!) real value is "ModuleSpec(name='posix', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

