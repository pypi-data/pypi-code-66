import typer
from pegasusapp.train import run_train
import zipfile
import boto3
from pegasusapp.utils import destructure_s3_url
import os.path as osp
import subprocess

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
    s3 = boto3.client("s3")
    bucket, key = destructure_s3_url(filepath, log=True)
    code_key = osp.join(key, "code.zip")
    typer.echo(code_key)
    s3.download_file(bucket, code_key, "/tmp/code.zip")

    with zipfile.ZipFile("/tmp/code.zip", "r") as zip_ref:
        zip_ref.extractall("/tmp/extracted_code")

    subprocess.run(["ls", "/tmp/extracted_code"])

    subprocess.run("pip install -r /tmp/extracted_code/requirements.txt".split(" "))
    subprocess.run(
        ["python", "/tmp/extracted_code/train.py"], env={"S3_PREFIX": filepath}
    )

    typer.echo("Pulling code")
