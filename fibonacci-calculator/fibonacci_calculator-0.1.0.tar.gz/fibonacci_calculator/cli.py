"""Console script for fibonacci_calculator."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for fibonacci_calculator."""
    click.echo("Replace this message by putting your code into "
               "fibonacci_calculator.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
