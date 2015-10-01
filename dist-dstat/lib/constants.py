import os
class Constants:
    CWD = os.path.dirname(os.path.realpath(__file__))
    ANSIBLE_BIN_PATH = '%s/../ansible/bin/ansible'%(CWD)
    ANSIBLE_PLAYBOOK_BIN_PATH = '%s/../ansible/bin/ansible-playbook'%(CWD)

    # csv first lines are comments
    CSV_STARTING_INDEX = 7
    CSV_SRC = '/tmp/dstat.csv'
    CSV_DEST = '/tmp/dstatout/'
    PLAYBOOK = '%s/../playbooks/dist-dstat.yml' %(CWD)

    PLOT_WIDTH_INCHES = 12
    PLOT_HEIGHT_INCHES = 5

    TITLE_Y = 1.40




class Name2Col:
    '''
    ----total-cpu-usage---- ------memory-usage----- -dsk/total- -net/total-
usr sys idl wai hiq siq| used  buff  cach  free| read  writ| recv  send
'''
    CPU_USR  =  0
    CPU_SYS  =  1
    CPU_IDL  =  2
    CPU_WAI  =  3
    CPU_HIQ  =  4
    CPU_SIQ =  5

    MEM_USED =  6
    MEM_BUFF =  7
    MEM_CACH =  8
    MEM_FREE =  9

    DISK_READ = 10
    DISK_WRIT = 11

    NET_SEND = 12
    NET_RECV = 13


