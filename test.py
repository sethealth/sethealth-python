import os
import sys
import requests
import sethealth


def test_valid_request():
    try:
        client = sethealth.Client(key=os.getenv(
            'SETHEALTH_KEY'), secret=os.getenv('SETHEALTH_SECRET'))
        client.getToken()
    except requests.exceptions.RequestException:
        sys.stderr.write("Token is NOT valid")


def test_unvalid_request():
    try:
        client = sethealth.Client("", "")
        client.getToken()
        sys.stderr.write("The request should be unvalid")
    except requests.exceptions.RequestException:
        pass


if __name__ == "__main__":
    test_valid_request()
    test_unvalid_request()
