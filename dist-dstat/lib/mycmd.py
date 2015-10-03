import os
from subprocess import *
from excepts import CmdException
from mylogger import dr_logger

def run_cmd(cmd, quiet=True, cwd=None):
    dr_logger.debug('cmd: %s cwd: %s',cmd, cwd)
    child = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, cwd=cwd)
    output = ''
    while child.poll() is None:
        l = child.stdout.readline()  # This blocks until it receives a newline.
        if not quiet and l != '':
            sys.stdout.write(l)
        output += l
    # When the subprocess terminates there might be unconsumed output
    # that still needs to be processed.
    o = child.stdout.read()
    if not quiet and l != '':
        sys.stdout.write(o)
    output += o

    err = child.stderr.read()
    if not quiet and err != '':
        sys.stdout.write(err)

    rc = child.returncode
    if rc != 0 and rc != None:
        try:
            dr_logger.debug('%s returned %d, output=%s, error=%s' %
                        (cmd, rc, output, err))
        except:
            # logger not available
            print('%s returned %d, output=%s, error=%s' %
                        (cmd, rc, output, err))

        raise CmdException(cmd, rc, output, err)
    try:
        dr_logger.debug('res: %d',rc)
        dr_logger.debug('output: ' + output)
        dr_logger.debug('error: ' + err)
    except:
        pass

    return output + err


def run_ansible_cmd(cmd, quiet=True):
    cwd = os.path.dirname(os.path.realpath(__file__))
    env = 'PYTHONPATH=%s/../../ansible-1.9.3/lib/' % cwd

    output = run_cmd('%s %s/../../ansible-1.9.3/bin/%s' % (env, cwd, cmd), quiet)
    return output
