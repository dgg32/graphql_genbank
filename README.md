
  

# Introduction

  

This repository contains code and data for my article "Build Your Own GraphQL GenBank in AWS".
1. The data folder contains three GBK files. They were used in the tutorial

  

# Prerequisite
requests

genome2json (https://github.com/gamcil/genome2json, MIT license)

requests_aws4auth

boto3

  
  

# Scripts
gbk_to_dynamodb.py is used to import GBK files into DynamoDB. Change the "table_name" if you named your DynamoDB differently. Usage:

      python gbk_to_dynamodb.py [GBK_file]

query.py and config.py are our demo client. First fill in the endpoint and api key in config.py as stated in my article. Then run:

    python query.py

 ## Authors

* **Sixing Huang** - *Concept and Coding*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
  
