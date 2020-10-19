import argparse
import logging
import os
import re

from bs4 import BeautifulSoup as bs
import requests

from pdf.util import request_get, working_dir, download, make_tempdir






logger = get_logger()


def main():
    pdfs = download_pdfs()
    print("\n".join(pdfs))



if __name__ == "__main__":
    main()
