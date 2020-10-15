#!/usr/bin/env python3
from __future__ import print_function
import os
import json
import shutil
import glob
import logging
from typing import List
from hashlib import blake2b
from signal import signal, SIGPIPE, SIGINT, SIG_DFL
signal(SIGPIPE, SIG_DFL)
signal(SIGINT, SIG_DFL)

SUFFIXES = ['.nsq', '.nin', '.nhr', '.nto', '.not', '.ndb', '.ntf']


def remove_intermediates(runid: str, intermediates: List[str], protect: bool)\
        -> None:
    logger = logging.getLogger(__name__)
    if protect:
        msg = 'One or more intermediates of {} type need to be removed'
        logger.info(msg.format(','.join(intermediates)))
        msg = 'Delete the "protect" flag in the config.json file or restart '\
            'your analysis with another runid to continue.'
        logger.info(msg)
        end_program(1)

    genome_tmpfiles = ['blast_results.tsv', 'keepsidx.json',
                       'single_copy.json', 'blast_filtered.tsv',
                       'expected_filt.json']
    if 'genome' in intermediates:
        for deldir in ['unaligned', 'aligned']:
            if os.path.exists(deldir):
                shutil.rmtree(deldir)
        for fullname in [os.path.join('.autoMLSA', fn) for
                         fn in genome_tmpfiles]:
            if os.path.exists(fullname):
                os.remove(fullname)
    for delfile in glob.iglob(runid + '.nex*'):
        os.remove(delfile)


def end_program(code):
    """
    Program message including success or failure of the program.
    """
    logger = logging.getLogger(__name__)
    if code == 1:
        msg = 'Program was stopped at an intermediate stage.'
        logger.info(msg)
    elif code == 0:
        msg = 'Program was a success! Congratulations!'
        logger.info(msg)
    else:
        msg = 'Program exiting with code ({}) indicating failure.'
        logger.info(msg.format(code))
        msg = 'Check error messages to resolve the problem.'
        logger.info(msg)
    exit(code)


def check_if_fasta(fa):
    """
    Checks first line of file for '>' to determine if FASTA, returns bool
    """
    for suffix in SUFFIXES:
        if suffix in fa:
            return False
    with open(fa, 'r') as fah:
        if fah.readline().startswith('>'):
            return True
        else:
            return False


def json_writer(fn, x):
    """
    Writes object to file as json format.
    """
    with open(fn, 'w') as fh:
        json.dump(x, fh, indent=4)
        fh.write('\n')


def sanitize_path(s):
    """
    Turns string into filename without symbols
    """
    s = s.replace(' ', '_')
    filename = ''.join(x for x in s if (x.isalnum() or x in '._-'))
    return filename


def generate_hash(s):
    """
    Generates blake2b hash for sequence
    input  - nucleotide sequence
    return - blake2b hash digest
    """
    seqhash = blake2b(s.encode(), digest_size=16)
    return seqhash.hexdigest()


def checkpoint_reached(stage):
    logger = logging.getLogger(__name__)
    msg = 'Checkpoint reached {}. Stopping...'
    logger.info(msg.format(stage))
    end_program(1)


def checkpoint_tracker(fn_name):
    checkpath = os.path.join('.autoMLSA', 'checkpoint', fn_name)
    if not os.path.exists(checkpath):
        open(os.path.join(checkpath), 'w').close()


def exit_successfully(rundir: str, treefile: str) -> None:
    """Temporary command

    input  - rundir and treefile to print to log
    return - None
    """
    logger = logging.getLogger(__name__)

    msg = 'Your treefile is ready: {}/{}'
    logger.info(msg.format(rundir, treefile))
    end_program(0)
