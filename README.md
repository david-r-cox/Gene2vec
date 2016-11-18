# Gene2vec: Neural word embeddigs of genetic data

## Overview
Gene2vec is an adaptation of the Word2vec model that aims to construct quasi-syntactic and semantic relationships from amino acid sequence data. Word2vec is an extension upon the continuous Skip-gram model that allows for precise representation of semantic and syntactic word relationships. Additionally, Word2vec representations exhibit additive composability such that vector arithmetic can be performed on words. Mikolov et al. illustrate this behavior by noting that the resulting vector space representation of ("Madrid" - "Spain" + "France") is closer to that of "Paris" than any other word.

We demonstrate the successful construction of such relationships from amino acid sequences by using them to perform some rudimentary protein classification.

See the [report](https://github.com/davidcox143/Gene2vec/blob/master/report/Gene2vec.ipynb) for more info. 
