# sethealth py-client

Sethealth py client allows to access the backend sethealth API from a server. The unique use case of this library today is to provide a authentication schema to delegate the "frontend" javascript library to communicate safely with the sethealth backend.

This is accomplish by the generation of a service account in sethealth. A service account is a long-living account for non-human users, like servers. Once a service account is created, a api key and a api secret are generated, this credentials **MUST be kept private, never exposed in a client side application**.

This "long-living" credentials can be used instead to create short-living credentials in the shape of access tokens in order to call the upload/download medical data from the client.

## Install

```
pip install --upgrade sethealth
```
If you have permission problems try adding "--user" option to pip.

## Usage

```python
import sethealth

#import your credentials
apiKey = 'HERE THE API KEY'
apiSecret = 'HERE THE API SECRET'
client = sethealth.Client(apiKey, apiSecret)

# Ask for a short-living access token
token = client.getToken()
print("ACCESS TOKEN: " + token)
```


## Release

1. Update version in setup.py
2. Commit all changes
3. Run `make release`
4. Create git tag vX.X.X
5. Create commit with the following name `X.X.X`
6. Run `git push origin`
7. Run `gin push --tags`
