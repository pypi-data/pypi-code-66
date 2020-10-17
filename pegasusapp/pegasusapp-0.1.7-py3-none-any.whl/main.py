import typer
from pegasusapp.train import run_train

app = typer.Typer()


@app.callback()
def callback():
    """
    Pegasus
    """


@app.command()
def train(path_to_zip: str):
    """
    Trains a pytorch lighting file
    """
    run_train(path_to_zip)


@app.command()
def configure():
    """
    Sets where you want to upload/host your models
    """
    typer.echo("Configuring")


@app.command()
def list_models():
    """
    Lists the models in your account
    """
    typer.echo("Listing")


@app.command()
def deploy():
    """
    Deploys a model
    """
    typer.echo("Deploying")


@app.command()
def delete():
    """
    Stops hosting a model
    """
    typer.echo("Deleting")


@app.command()
def pull_code_and_unzip(filepath: str):
    """
    Pulls code from the S3 repository and runs it
    """
    typer.echo("Pulling code")
