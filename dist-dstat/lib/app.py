import argparse

from constants import *
from datareader import *
from dstatcontroller import *
from mylogger import *
from plot import *

def parse_command_line_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "nodes", metavar='node', nargs='+', help="List of nodes to install DR on.")

    parser.add_argument("-i", "--install-dstat", type=bool,
                        help="Install dstat on all the nodes", required=False, default=False)

    parser.add_argument("-d", "--drop-caches", type=bool,
                        help="Drop caches to make sure we read from disk", required=False, default=False)

    args = parser.parse_args()
    return args


'''
Layout is:
  node1-cpu
  node2-cpu
  ..
  noden-cpu

  node1-mem
  node2-mem
  ..
  noden-mem

  node1-disk
  node2-disk
  ..
  noden-disk

  node1-net
  node2-net
  ..
  noden-net
'''

args = parse_command_line_args()
dc = DstatController(args.nodes, args.install_dstat, args.drop_caches)

log_green("Starting monitoring ...")
dc.start_dstat()
raw_input('Press any key to stop monitoring ...')
dc.stop_dstat()
log_green("Fetching results ...")
csvs = dc.fetch_csvs()

log_green("Plotting results ...")
#c = Canvas()
c = CategoryCanvas()
plots = []

def add_plots(canvas, csvs, category, ymax=None,ylabel=None, scale=1.0, lines = []):
    """

    :param canvas: object that creates the plot
    :param csvs: CSV files, one for each host in the cluster
    :param type: Just a name like 'CPU' or 'Memory'. Used to group the plots together and for titles
    :param ymax: Maximum value in the Y axis
    :param ylabel: Label for the Y axis
    :param scale: Divide the dstat output by this value (e.g. to convert bytes to MBs scale=1024.0*1024)
    :param lines (tuple): line in the plot.Each tuple contains the column indices, an optional operator and an optional label.
                          the column indices point to the columns of the CSV file. We can sum or multiply colums together
                          by specifying the + and * operators respectively. Label adds a label for that line in the plot.
    :return:
    """
    for csv in csvs:
        try:
            import re
            host = re.findall(r'%s(.*?)/tmp/dstat.csv' %(Constants.CSV_DEST),csv)[0]
        except Exception:
            log_warning("Unable to determine host")
            host = 'unknown'

        dr = DataReader(csv, scale)
        plot = Plot(host,category)
        plot.ymax = ymax
        plot.ylabel = ylabel

        for col_indices,operator,label in lines:
            if len(col_indices) > 1 and operator != '+' and operator != '*':
                raise Exception('Operator %s is not supported' %(operator))
            cols = []
            for col in col_indices:
                c = dr.get_col(col)
                cols.append(c)
            finalcol = []

            for i,row in enumerate(cols[0]):
                acc = 1 if operator == '*' else 0
                for col in cols:
                    item = col[i]
                    if operator == '+' or not operator:
                        acc += item
                    elif operator == '*':
                        acc *= item
                finalcol.append(acc)

            plot.addline(finalcol,label)

        canvas.add_plot(plot,category)

add_plots(canvas=c,csvs=csvs,category='CPU',ymax=100,ylabel='CPU %',scale=1.0,lines=[([Name2Col.CPU_USR,Name2Col.CPU_SYS], '+','CPU %')])
add_plots(canvas=c,csvs=csvs,category='MEM',ymax=None,ylabel='MEM GB',scale=1024.0*1024.0*1024.0,lines=[([Name2Col.MEM_USED], None, 'MEM GB')])
add_plots(canvas=c,csvs=csvs,category='DISK',ymax=None,ylabel='DISK MB/S',scale=1024.0*1024.0,lines=[([Name2Col.DISK_READ], None, 'DISK READ MB/S'),([Name2Col.DISK_WRIT], None, 'DISK WRITE MB/S')])
add_plots(canvas=c,csvs=csvs,category='NET',ymax=None,ylabel='NET Mbps',scale=1024*1024,lines=[([Name2Col.NET_RECV], None, 'NET RECV Mbps'),([Name2Col.NET_SEND], None, 'NET SEND Mbps')])

def get_date():
    import datetime
    return datetime.datetime.now().strftime("%I:%M%p_%B_%d_%Y")


filename = '/tmp/dist-dstat-%s.png' %(get_date().replace(' ','_'))
c.save_fig(filename)
log_green('Saved plot in %s'%(filename))