# DeepCAT Project - Benchmarking <img  align="left" src="https://github.com/s175573/DeepCAT/blob/master/Figures/Cat.png" width="35" height="45" > 

### Deep CNN Model for Cancer Associated TCRs

DeepCAT is a computational method based on convolutional neural network to exclusively identify cancer-associated beta chain TCR hypervariable CDR3 sequences. The input data were generated from tumor RNA-seq data and TCR repertoire sequencing data of healthy donors.
Out aim is to compare DeepCAT results with other machine learing methods. 


### Training DeepCAT models

To train DeepCAT from scratch, we first used the example data in TrainingData folder.
This folder contains two files, each is a list of CDR3s coming from either cancer or healthy individuals.



```python
python
>>> from DeepCAT import *
>>> PredictClassList,PredictLabelList,AUCDictList = batchTrain(ftumor='TrainingData/TumorCDR3.txt',n=10, feval_tumor='TrainingData/TumorCDR3_test.txt', feval_normal='TrainingData/NormalCDR3_test.txt', STEPs=20000, rate=0.33, fnormal='TrainingData/NormalCDR3.txt', mymodel=False)
>>> print(AUCDictList)
```
This function performs n (=10 here) times 3-fold cross-validation by subsampling 1-rate (67%) of the data for training, and the remaining 33% for validation. The number of training steps in each run is equal 20000.

We added a flag "mymodel" to be able to run the code by applying different models. There is an example file called "run_with_svm.ipynb".

### Data
The original data comes in txt files. To create a csv of the healthy/sick donors, use "txt_to_csv.ipynb".

