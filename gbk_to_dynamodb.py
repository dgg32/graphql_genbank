from g2j import genbank
import sys
import json
import boto3

input_file = sys.argv[1]

client = boto3.client('dynamodb')
table_name = "genbank"

with open(input_file) as gbk:
    record = genbank.parse(gbk)
    for s in record.to_dict()["scaffolds"]:

        feature_key = ["isolation_source", "country", "lat_lon", "db_xref"]

        features = {}

        for f in feature_key:
            try:
                features[f] = {"S": s["features"][0]["qualifiers"][f]}
            except:
                pass

        putItemObject = {
            table_name: [
                {
                    "PutRequest": {
                        "Item": {
                            "accession": {"S": s["accession"]},
                            "sequence": {"S": s["sequence"]},
                            "features": {"M": features}
                        }
                    }
                }
            ]
            
        }
        response = client.batch_write_item(RequestItems=putItemObject)
        print (response)