## WFRDA
**Zhong Yuan**, Baiyang Chen, Jia Liu, Hongmei Chen, Dezhong Peng, Peilin Li*, [Anomaly Detection Based on Weighted Fuzzy-Rough Density](WFRDA_code/WFRDA.pdf), Applied Soft Computing, vol. 134, ID.109995, 7 January 2023, DOI: [10.1016/j.asoc.2023.109995](https://doi.org/10.1016/j.asoc.2023.109995). (Code)

## Abstract
The density-based method is a more widely used anomaly detection. However, most of the existing density-based methods mainly focus on dealing with certainty data and do not consider the problem of uncertainty and fuzziness of the data. Fuzzy rough set theory, as an important mathematical model of granular computing, provides an effective method for information processing of uncertain data. For this reason, this paper proposes an anomaly detection based on fuzzy-rough density. First, the fuzzy-rough density is defined to describe the degree of aggregation of objects. Then, fuzzy entropy is introduced to compute the weights of each attribute. Further, an anomaly score is constructed to characterize the anomaly degree of the samples, which takes into account both the density and fuzziness of the samples. Finally, extensive experiments are conducted on publicly available data with nine popular detection methods. The experimental results show that the proposed method achieves better performance on three types of datasets.

## Usage
You can run Demo_WFRDA.m or WFRDA.py:
```
clc;
clear
clear all;
format shortG;

load Example_WFRDA
Dataori=Example;

trandata=Dataori;
trandata(:,2:3)=normalize(trandata(:,2:3),'range');

sigma=0.5;
out_scores=WFRDA(trandata,sigma)

```
You can get outputs as follows:
```
out_scores =
      0.64714
      0.56629
      0.67201
      0.59316
      0.61343
```

## Citation
If you find WFRDA useful in your research, please consider citing:
```
@article{yuan2023anomaly,
title = {Anomaly detection based on weighted fuzzy-rough density},
author = {Yuan, Zhong and Chen, Bai Yang  and Liu, Jia  and Chen, Hong Mei  and Peng, De Zhong  and Li, Pei Lin },
journal = {Applied Soft Computing},
volume = {134},
pages = {109995},
year = {2023},
doi={10.1016/j.asoc.2023.109995},
publisher={Elsevier}
}
```
