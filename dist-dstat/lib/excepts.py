class AnsibleException(Exception):
    pass

class CmdException(Exception):
    def __init__(self, cmd, rc, output, err):

        # Call the base class constructor with the parameters it needs
        message = 'cmd: %s\n rc: %d\n output: %s\n error: %s\n' %(cmd, rc, output, err)
        super(CmdException, self).__init__(message)

        # Now for your custom code...
        self.cmd = cmd
        self.rc = rc
        self.output = output
        self.err = err


