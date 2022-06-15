# Doccano API Client

A simple client wrapper for the doccano API.
This is a fork of doccano API Client customised to the specific needs of Okra AI 

- [Doccano API Client](#doccano-api-client)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Completion](#completion)
  - [To-Do](#to-do)
- [Doccano API BETA Client](#doccano-api-beta-client)

## Installation

To install `okra-doccano-client`, simply run:

```bash
pip install okra-doccano-client
```

## Usage

- Object instantiation takes care of session authorization.
- All methods return a `requests.models.Response` object.

```python
from doccano_api_client import DoccanoClient

# instantiate a client and log in to a Doccano instance
doccano_client = DoccanoClient(
    'http://doccano.example.com',
    'username',
    'password'
)

# get basic information about the authorized user
r_me = doccano_client.get_me()

# print the details from the above query
print(r_me)

# get the label text from project 1, label 3
label_text = doccano_client.get_label_detail(1, 3)['text']

# upload a json file to project 1. If file is in current directory, file_path is omittable
r_json_upload = doccano_client.post_doc_upload(1, 'json', 'file.json', '/path/to/file/without/filename/')
```

