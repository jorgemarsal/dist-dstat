Framework to create performance plots (CPU, memory, disk, network) across a cluster. Useful to profile distributed systems.

Usage:

To install dstat (first time):

    # python app.py --install-dstat <ip addresses of nodes>
    $ python app.py --install-dstat localhost

Once dstat is installed it's faster to just run:

    $ python app.py localhost

The script starts `dstat` on all the nodes (using Ansible) and waits for the user to press a key.
At that point it stops all the `dstat` processes, collects the CSV output and generates a plot
that aggregates all the performance numbers from all nodes.


