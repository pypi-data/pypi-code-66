from awsutils.s3 import S3
from dirutility import SystemCommand
from flask import jsonify
from flask_restful import Resource
from synfo import Synfo

from FlaskSSL._version import __version__ as version
from FlaskSSL.api.arguments import parse_args


def domain_args(domains):
    """Return a string of domain arguments to pass to certbot."""
    return ' ' + ' '.join(['-d {0}'.format(domain) for domain in domains])


def staging_arg(staging):
    """Retrieve an appropriate staging command flag based on the input value."""
    return '--staging --dry-run' if int(staging) > 0 else ''


class Cert(Resource):
    @staticmethod
    def get():
        # Parse arguments
        args = parse_args()

        print('Retrieving certificate for the {}'.format(args['domain']))

        # Construct certbot command
        cmd = [
            'certbot certonly --webroot',
            '-w /webroot/certbot',
            '{domain}',
            '--email {email}',
            '{staging}',
            '--rsa-key-size 4096',
            '--keep-until-expiring',
            '--agree-tos',
            '--non-interactive'
        ]
        cmd = ' '.join(cmd).format(domain=domain_args(args['domain']),
                                   email=args['email'],
                                   staging=staging_arg(args['staging']))
        output = SystemCommand(cmd).output

        # Upload SSL certs to AWS S3
        upload_success = False
        if int(args['staging']) < 1:
            print('Uploading SSL certs to AWS S3')
            S3('hpa-ssl-certs').upload('/etc/letsencrypt/')

            if S3('hpa-ssl-certs').exists('live/{}'.format(args['domain'])):
                print('The file /etc/letsencrypt/live/{} exists in S3 bucket'.format(args['domain']))
            upload_success = True

        return jsonify({'upload_success': upload_success, 'output': output})


class Help(Resource):
    @staticmethod
    def get():
        return SystemCommand('certbot --help').output


# Test responses
class Test(Resource):
    @staticmethod
    def get():
        return jsonify({'response': 'HPA SSL Validation API is up and running!',
                        'args': parse_args(),
                        'version': version,
                        'python version': Synfo().python.info(),
                        'system info': Synfo().system.info(),
                        'hardware': Synfo().hardware.info()})


__all__ = ['Test', 'Help', 'Cert']
