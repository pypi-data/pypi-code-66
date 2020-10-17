from urllib.parse import urlparse
from typing import Tuple
import logging
import typer

logger = logging.getLogger(__name__)


def destructure_s3_url(s3_url: str, log: bool = False) -> Tuple[str, str]:
    """
    Function to parse S3 url and returns bucket and key
    :param s3_url:
    :param log: Whether to log inputs and outputs
    :return:
    """
    o = urlparse(s3_url)
    bucket = o.netloc
    key = o.path
    key = key[1:] if key.startswith("/") else key
    if log:
        typer.echo(f"S3 URL: {s3_url}, Bucket: {bucket}, Key: {key}")
    return bucket, key
