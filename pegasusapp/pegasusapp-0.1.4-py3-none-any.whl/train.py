import typer
import boto3
from datetime import datetime
import os
import zipfile


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def run_train(path_to_zip: str):
    filepath = f"ml-training/{__file__}/{datetime.now()}/"
    s3_code_path = f"{filepath}/code.zip"
    typer.echo(f"Compressing {path_to_zip}")

    zipf = zipfile.ZipFile("/tmp/code.zip", "w", zipfile.ZIP_DEFLATED)
    zipdir(path_to_zip, zipf)
    zipf.close()

    typer.echo(f"Uploading to s3 {path_to_zip}")
    s3 = boto3.resource("s3")
    s3.meta.client.upload_file(f"/tmp/code.zip", "gene", s3_code_path)

    path_for_docker = f"s3://gene/{filepath}"
    typer.echo(f"Would now call docker container with env var {path_for_docker}")

    batch = boto3.client("batch")
    command = "pip install pegasusapp && pegasus pull_code_and_unzip".split(" ")
    command.append(f"{filepath}")
    batch.submit_job(
        jobName=filepath,
        jobQueue="general-job-queue",
        jobDefinition="ml-training",
        command=command,
    )
