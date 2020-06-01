# CS6120_NLP_Project


## Downloading the Data Set

```
cd Toxicity
./download_data.sh # requires kaggle configuration to work
```

If you do not have kaggle configured, please refer to their [installation guide](https://github.com/Kaggle/kaggle-api#installation). This can also be performed by going to the [Kaggle competition](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification). Please reach out if you have any trouble.

## Running Top Performing Model

```
python test_model.py
```

## Running ML Models

All ML models are located in `./models`. The `test_model.py` uses [./Toxicity/Model.py](./Toxicity/Model.py) to define what is called. Updating paths can be used to see results for other models. Running the Word2Vec approach will require downloading Word2Vec embeddings from google [here](https://code.google.com/archive/p/word2vec/). It will also require adding additional code for calculating the mean since we didn't ever feel the need to run them outside of testing.

## Running BERT

<<<<<<< HEAD
Download the model [here](https://drive.google.com/open?id=1q2F-9B7ON0XDjz8mYUBPFpCGT9bmPThC). Place the file in [Toxicity/model/](Toxicity/model/). You can then run `python test_bert_model.py` from the root.# TwittertoxicityClassification
=======
Download the model [here](https://drive.google.com/open?id=1q2F-9B7ON0XDjz8mYUBPFpCGT9bmPThC). Place the file in [Toxicity/model/](Toxicity/model/). You can then run `python test_bert_model.py` from the root.

## Training

For ML refer to [models/LogisticRegression.ipynb](./models/LogisticRegression.ipynb) and [models/MachineLearningModels.ipynb](./models/MachineLearningModels.ipynb). For BERT refer to [Toxicity/gpu_bert_trainer.py](./Toxicity/gpu_bert_trainer.py) and [gpu_bert_console_test.py](./Toxicity/gpu_bert_console_test.py).

## Contact Us

If you have any questions or difficulties, please reach out.
>>>>>>> c114701b482b4b04311f0f33fce958ef75e4a5a4
