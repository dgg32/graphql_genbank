import requests
from requests_aws4auth import AWS4Auth
import boto3
import config


session = requests.Session()

APPSYNC_API_ENDPOINT_URL = config.endpoint_url
API_KEY = config.api_key

query = """
query getAllSequences {
  getAllSequences(count: 5) {
    sequences {
      accession
      features {
        country
      }
    }
    nextToken
  }
}
"""

response = session.request(
    url=APPSYNC_API_ENDPOINT_URL,
    method='POST',
    headers={'x-api-key': API_KEY},
    json={'query': query}
)

print(response.json()['data'])