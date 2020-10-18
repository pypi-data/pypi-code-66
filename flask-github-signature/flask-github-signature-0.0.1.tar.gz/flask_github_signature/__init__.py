"""
A Flask view decorator to verify Github's webhook signatures.

For more details see https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/securing-your-webhooks
"""

import os
import hmac
from functools import wraps
from flask import request


def compute_signature(secret, payload):
    """Returns hmac's hexdigest using SHA256"""
    computed = hmac.new(secret.encode("utf-8"), payload, "SHA256")
    return computed.hexdigest()


def get_github_signature(req):
    """Extracts Github's payload signature from request's headers."""
    gh_signature_header = req.headers.get("X-Hub-Signature-256")
    if req.method == "POST" and gh_signature_header is not None:
        return gh_signature_header.replace("sha256=", "")
    return None


def signature_is_valid(a, b):
    """Compares 2 signature hashes."""
    return hmac.compare_digest(a, b)


def verify_signature(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        gh_webhook_secret = os.environ.get("GH_WEBHOOK_SECRET")
        if not gh_webhook_secret:
            raise ValueError("No GH_WEBHOOK_SECRET configured.")
        payload = request.get_data()
        signature = compute_signature(gh_webhook_secret, payload)
        signature_gh = get_github_signature(request)
        if signature_gh is not None and signature_is_valid(signature, signature_gh):
            return f(*args, **kwargs)
        else:
            return "Signatures didn't match!", 400

    return decorated_function
