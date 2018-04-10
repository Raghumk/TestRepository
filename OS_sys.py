

#OS_sys

import os, sys


ret = os.access('OS_sys.py', os.F_OK)
print(ret)
ret = os.access('OS_sys.py', os.R_OK)
print(ret)


#functions
#os.access(path, mode)
#os.chflags(path, flags)  -- Set the flags of path to the numeric flags
#os.chmod(path, mode)     -- Change the mode of path to the numeric mode.
#os.chown(path, uid, gid)  -- Change the owner and group id of path to the numeric uid and gid.
#os.chroot(path)         	-- Change the root directory of the current process to path.
#os.close(fd) 			-- Close file descriptor fd.
#os.closerange(fd_low, fd_high) 	--	Close all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring
errors.
