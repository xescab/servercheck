## servercheck

We frequently have to check whether one of our servers has access to other servers on our internal network. To make this a little easier for ourselves, we've decided to use Python to write a CLI that can either take a JSON file with servers and ports to check or a list of host/port combinations to make requests to. The team has decided that we should use click to create our CLI, so we're going to kick off the project and lay out the CLI using click.

```
$ servercheck -f servers.json
Successful Connections
----------------------
IP1:port
IP2:port

Failed Connections
------------------
IP3:port
```

Or it can be used like this if we pass in host/port combination(s):

```
$ servercheck -s IP1:port -s IP2:port -s IP3:port
Successful Connections
----------------------
IP1:port
IP2:port

Failed Connections
------------------
IP3:port
```

If both styles are used, then combine the results but make sure not to allow duplicates.

If neither option is provided, then an error should be shown like this:

```
$ servercheck
Usage: servercheck [OPTIONS]

Error: must provide a JSON file or servers
```

### First stage

Show info parsed:

```
$ servercheck -s IP1:port -s IP2:port -s IP3:port
{'IP1:port', 'IP2:port', 'IP3:port'}
```

Or like this:

```
$ servercheck -f servers.json
{'IP1:port', 'IP1:port2', 'IP2:port'}
```

In this case, the servers.json file would look like this:

```
[
    "IP1:port",
    "IP1:port2",
    "IP2:port"
]
```