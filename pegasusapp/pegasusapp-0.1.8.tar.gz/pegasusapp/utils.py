from urllib.parse import urlparse
from typing import Tuple


def destructure_s3_url(s3_url: str) -> Tuple[str, str]:
    """
    Function to parse S3 url and returns bucket and key
    :param s3_url:
    :return:
    """
    o = urlparse(s3_url)
    bucket = o.netloc
    key = o.path
    return bucket, key
