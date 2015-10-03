Framework to create performance plots (CPU, memory, disk, network) across a cluster. Useful to profile distributed systems.

### Instructions
1. Install matplotlib

    pip install matplotlib

2. Unpack ansible

    tar xf ansible-1.9.3.tar.gz

3. To install `dstat` (first time):

    # python app.py --install-dstat <ip addresses of nodes>
    $ python app.py --install-dstat localhost

4. Once dstat is installed it's faster to just run:

    $ python app.py localhost

5. To drop the disk caches in the remote nodes specify --drop-caches:

    $ python app.py --drop-caches localhost

### Design 

The script starts `dstat` on all the nodes (using Ansible) and waits for the user to press a key.
At that point it stops all the `dstat` processes, collects the CSV output and generates a plot
that aggregates all the performance numbers from all nodes.


