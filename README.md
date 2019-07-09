## **Dynamo**: Mapping Vector Field of Single Cells
![Dynamo](https://www.dropbox.com/s/dvrfgo4qt5ispqs/dynamo_intro.png?raw=1)

Understanding how gene expression in single cells progress over time is vital for revealing the mechanisms governing cell fate transitions. RNA velocity, which infers immediate changes in gene expression by comparing levels of new (unspliced) versus mature (spliced) transcripts (La Manno et al. 2018), represents an important advance to these efforts. A key question remaining is whether it is possible to predict the most probable cell state backward or forward over arbitrary time-scales. To this end, we introduce an inclusive model (termed Dynamo) capable of predicting cell states over extended time periods, that incorporates promoter state switching, transcription, splicing, translation and RNA/protein degradation by taking advantage of scRNA-seq and the co-assay of transcriptome and proteome. We also implement scSLAM-seq by extending SLAM-seq to plate-based scRNA-seq (Hendriks et al. 2018; Erhard et al. 2019; Cao, Zhou, et al. 2019) and augment the model by explicitly incorporating the metabolic labelling of nascent RNA. We show that through careful design of labelling experiments and an efficient mathematical framework, the entire kinetic behavior of a cell from this model can be robustly and accurately inferred. Aided by the improved framework, we show that it is possible to analytically reconstruct the transcriptomic vector field from sparse and noisy vector samples generated by single cell experiments. The analytically reconstructed vector further enables global mapping of potential landscapes that reflects the relative stability of a given cell state, and the minimal transition time and most probable paths between any cell states in the state space This work thus foreshadows the possibility of predicting long-term trajectories of cells during a dynamic process instead of short time velocity estimates. Our methods are implemented as an open source tool, dynamo  [Github link](https://github.com/aristoteleo/dynamo-release).


## Installation

Note that this is our first alpha version of **Dynamo** (as of July 9th, 2019). Dynamo is still under active development. Stable version of Dynamo will be released when it is ready. Until then, please use **Dynamo** with caution. We welcome any bugs reports (via GitHub issue reporter) and especially code contribution  (via GitHub pull requests) of **Dynamo** from users to make it an accessible, useful and extendable tool. For discussion about different usage cases, comments or suggestions related to our manuscript and questions regarding the underlying mathematical formulation of dynamo, we provided a google group [goolge group](https://groups.google.com/forum/#!forum/dynamo-user/). Dynamo developers can be reached by <<xqiu.sc@gmail.com>. You can install this alpha version of **Dynamo** from source, using the following script:

```sh
pip install git+https://github.com:aristoteleo/dynamo-release
```
Alternatively, you can git clone our repo and then use 
```sh
pip install directory_to_dynamo_release_repo
```

## Citation

Xiaojie Qiu, Yan Zhang, Dian Yang, Shayan Hosseinzadeh, Li Wang, Ruoshi Yuan, Song Xu, Yian Ma, Joseph Replogle, Spyros Darmanis, Jianhua Xing, Jonathan S Weissman (2019): Mapping Vector Field of Single Cells. BioRxiv

biorxiv link: https://www.biorxiv.org/content/10.1101/696724v1

## Contribution 
If you want to contribute to the development of dynamo, please check out CONTRIBUTION instruction: [Contribution](https://github.com/aristoteleo/dynamo-release/blob/master/CONTRIBUTING.md)
