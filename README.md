# CS6120_NLP_Project

## Training Models

Before you can run any of the scripts to train the model of your desire, you first need to run `python pre_process_data.py` to instantiate the training data in a format that is easy to read and does not have to be re-parsed.

## Running Heroku Instance

Before running make sure you have set up a twitter [api access token](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens). Then create a file named `twitter_api.json`. You'll notice that there is a file [twitter_api.template.json](./twitter_api.template.json) and that is the format that should be in the file you've created. Copy the api key in the `key` field and the api key secret in the `secret` field for the program to be able to pull from twitter.

## Running BERT

Download the model [here](https://drive.google.com/open?id=1q2F-9B7ON0XDjz8mYUBPFpCGT9bmPThC). Place the file in [Toxicity/model/](Toxicity/model/). You can then run `python test_bert_model.py` from the root.# TwittertoxicityClassification
