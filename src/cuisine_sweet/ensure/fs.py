"""
Fabfile functions for ensuring the state the filesystem
"""

import cuisine
from fabric.api import run, sudo
from cuisine_sweet.utils import completed_ok


@completed_ok(arg_output=[0])
def dir_created(path, recursive=False, mode=None, owner=None, group=None):
    """
    Ensure that the directory is created and with proper permissions.

    Wraps ``cuisine.dir_ensure`` function

    :param path: *required* str; path to the directory
    :param recursive: bool; recursively create if not present
    :param mode: int; octal mode passed to chmod (e.g. 755, 600)
    :param owner: str; user/uid that should own the file, as passed to chown
    :param group: str; user/uid that should own the file, as passed to chgrp

    """
    cuisine.dir_ensure(name, **kwargs)


@completed_ok(arg_output=[0,1])
def dir_symlink_created(src, dest):
    """
    Ensure that a symlink at `dest` pointing to `src` is created.

    :param src: *required* str; path to the source real directory
    :param dest: *required* str; path to the destination symlink
    """
    run('ln -s %s %s >& /dev/null; true' % (src, dest))
    run('test -L %s && test -d %s' % (dest, dest))

