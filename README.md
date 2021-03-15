
  

# Introduction

  

This repository contains code and data for my article "[Build Your Own GraphQL GenBank in AWS](https://dgg32.medium.com/build-your-own-graphql-genbank-in-aws-a9e9eaeb712a)".
1. The data folder contains three GBK files. They were used in the tutorial

2. The scripts are for import and demo client.

  

# Prerequisite
requests

genome2json (https://github.com/gamcil/genome2json, MIT license)

requests_aws4auth

boto3 (You also need to configure your Boto3 [credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) beforehand, best with AWS CLI)

  
  

# Scripts
gbk_to_dynamodb.py is used to import GBK files into DynamoDB. Change the "table_name" if you named your DynamoDB differently. Usage:

    python gbk_to_dynamodb.py [GBK_file]

query.py and config.py are our demo client. First fill in the endpoint and api key in config.py as stated in my article. Then run:

    python query.py

 ## Authors

* **Sixing Huang** - *Concept and Coding*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
  
