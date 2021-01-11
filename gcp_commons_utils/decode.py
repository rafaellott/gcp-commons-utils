"""Decode the receiving information in Cloud Function entry point."""

import base64

import json


def decode_input_to_dict(input_request):
    """Decode input request to dict python."""
    if isinstance(input_request, dict):
        return input_request

    if isinstance(input_request, str):
        input_request = input_request.encode()

    try:
        input_request = json.loads(input_request)
        return input_request
    except UnicodeDecodeError:
        pass

    try:
        input_request = base64.decodebytes(input_request)
        return json.loads(input_request)
    except UnicodeDecodeError:
        raise ValueError(f"Invalid JSON object. {input_request} ...")
