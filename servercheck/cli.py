import click
import json
import sys

@click.command()
@click.option('--filename', '-f', default=None, help="JSON file contaning an array of IP:port to check")
@click.option('--server', '-s', default=None, multiple=True, help="Server IP and port to check")
def cli(filename, server):
    """
    Command-line interface to check servers connectivity
    """
    if not filename and not server:
        raise click.UsageError("must provide a JSON file or servers")

    # Use a set to prevent duplicates
    servers = set()

    if filename:
        try:
            f = open(filename)
            json_servers = json.load(f)
            for s in json_servers:
                servers.add(s)
        except Exception:
            print(f"Could not open or read JSON file {filename}")
            sys.exit(1)

    if server:
        for s in server:
            servers.add(s)

    print(servers)


if __name__ == "__main__":
    cli()