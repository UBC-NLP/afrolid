<p align="center">
<a href="https://github.com/UBC-NLP/afrolid/releases">
        <img alt="GitHub release" src="https://img.shields.io/github/release/UBC-NLP/afrolid.svg">
    </a>

<a href="https://demos.dlnlp.ai/afrolid">
        <img alt="Documentation" src="https://img.shields.io/website.svg?down_color=red&down_message=offline&up_message=online&url=https://demos.dlnlp.ai/afrolid">
    </a>
<a href="https://github.com/UBC-NLP/afrolid/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/UBC-NLP/afrolid?logoColor=blue"></a>
<a href='https://afrolid.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/afrolid/badge/?version=latest' alt='Documentation Status' /></a>
<a href="https://github.com/UBC-NLP/afrolid/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/UBC-NLP/afrolid"></a>
<a href="https://github.com/UBC-NLP/afrolid/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/UBC-NLP/afrolid"></a>

</p>
 

<center><img src="./images/afrolid_logo.jpg" alt="AfroLID" width="70%" /> </center>

AfroLID, a neural LID toolkit for 517 African languages and varieties. AfroLID exploits a multi-domain web dataset manually curated from across 14 language families utilizing five orthographic systems. AfroLID is described in this paper: 
[**AfroLID: A Neural Language Identification Tool for African Languages**](https://arxiv.org/abs/2210.11744).

<br>

## Requirements
- Download AfroLID model:
```shell
    wget pip install -U afrolid
```

## Installation
- To install AfroLID and develop directly using pip:
```shell
    pip install -U afrolid
```
- To install AfroLID and develop directly GitHub repo using pip:
```shell
    pip install -U git+https://github.com/UBC-NLP/afrolid.git
```
- To install AfroLID and develop locally:
```shell
    git clone https://github.com/UBC-NLP/afrolid.git
    cd afrolid
    pip install .
```
## Getting Started
The [full documentation](https://afrolid.readthedocs.io/en/latest/) contains instructions for getting started, translation using diffrent methods, intergrate AfroLID with your code, and provides more examples.

## Colab Examples


## License
afrolid(-py) is Apache-2.0 licensed. The license applies to the pre-trained models as well.

## Citation
If you use AfroLID toolkit or the pre-trained models for your scientific publication, or if you find the resources in this repository useful, please cite our paper as follows (to be updated):
```
@article{adebara2022afrolid,
  title={AfroLID: A Neural Language Identification Tool for African Languages},
  author={Adebara, Ife and Elmadany, AbdelRahim and Abdul-Mageed, Muhammad and Inciarte, Alcides Alcoba},
  booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
  month = December,
  year = "2022",
}

```



## Acknowledgments
We gratefully acknowledge support from the Natural Sciences and Engineering Research Council of Canada (NSERC; RGPIN-2018-04267), the Social Sciences and Humanities Research Council of Canada (SSHRC; 435-2018-0576; 895-2020-1004; 895-2021-1008), Canadian Foundation for Innovation (CFI; 37771), [The Digital Research Alliance of Canada (the Alliance)](www.alliancecan.ca/en),   [UBC ARC-Sockeye](https://doi.org/10.14288/SOCKEYE) and Advanced Micro Devices, Inc. (AMD). Any opinions, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of NSERC, SSHRC, CFI, CC, AMD, or UBC ARC-Sockeye. 
