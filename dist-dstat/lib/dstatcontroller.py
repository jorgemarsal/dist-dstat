import sys
from constants import *
from excepts import *
from mycmd import *
from mylogger import *

class DstatController:
    def __init__(self, nodes, setup=False):
        """
        :param nodes (list): list of all the nodes in the cluster
        :return:
        """
        with open('/tmp/nodes','w') as f:
            for n in nodes:
                f.write('%s\n'%(n))

        ansible_extra_options = ''
        self.playbook_cmd = '%s %s %s %s ' % (
                    'ansible-playbook',
                    '-i /tmp/nodes',
                    Constants.PLAYBOOK,
                    ansible_extra_options)

        if setup:
            log_green("Installing dstat ...")
            try:
                run_ansible_cmd(self.playbook_cmd + ' --tags setup ')
            except CmdException as e:
                log_error(e.output + e.err)
                sys.exit(1)


    def start_dstat(self):
        try:
            run_ansible_cmd(self.playbook_cmd + ' -e csv_src=%s '%(Constants.CSV_SRC) + ' --tags start ')
        except CmdException as e:
            log_error(e.output + e.err)
            sys.exit(1)

    def stop_dstat(self):
        try:
            run_ansible_cmd(self.playbook_cmd + ' --tags stop ')
        except CmdException as e:
            log_error(e.output + e.err)
            sys.exit(1)

    def fetch_csvs(self):
        """

        :return: directory where the csv files are stored
        """
        try:
            run_ansible_cmd(self.playbook_cmd + ' -e csv_src=%s -e csv_dest=%s ' %(Constants.CSV_SRC,Constants.CSV_DEST) + '--tags fetch')
        except CmdException as e:
            log_error(e.output + e.err)
            sys.exit(1)

        def get_csvs(csvdir):
            import glob
            return glob.glob('%s/*/tmp/dstat.csv'%(csvdir))

        csvs = get_csvs(Constants.CSV_DEST)
        return csvs
