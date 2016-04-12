# Gene2vec: Neural word embeddigs of genetic data

## Update 1:
Finding the optimal way to represent nucleotide data as “words” has proven to be the most challenging issue of the project.

Long nucleotide sequences (several hundred base pairs) often result in training data that contains no duplicate “words”. While it would be ideal to consider genes as words, Word2vec performs very poorly when each word is only used once. Not having any “context” for these long words prevents the construction of useful models. 

Shorter sequences also proved to be problematic. While there was much more context for Word2vec to pull from, we found that short sequences produced meaningless results -- sequences such as AAAAT, AAAGTT, etc are extremely common. We are currently settling for an uncomfortable middle ground of 27 bp sequences. 

Traditional genetic similarity evaluation is done through common substring analysis. Using 260905 27-grams, we were able to successfully generate 500 distinct clusters. Most notably, we observed that the contents of clusters was not determined by substring similarity, meaning Word2vec was successful in modeling our training data.

The following snippit contains sequences from two clusters. Note that the Triticum aestivum and Ovis canadensis samples have better alignment than those from the Triticum aestivum cluster. 


## Preliminary Results

```
        AAAAATAGTATAAAAAGTTGCCAAAAG ->  Triticum aestivum chromosome 3B
(11/27) ||||| |    | |||   |         
        AAAAACATGCAACAAACAGGAACTGGC ->  Triticum aestivum chromosome 3B
(10/27) |||||||          |  |     |  
        AAAAACAGAATCTGTCTAAAACAGAAC ->  Triticum aestivum chromosome 3B 
(14/27) |||||||||  |  |  |   |  |    
        AAAAACAGAGACATTACTTTGCCAACA ->  Ovis canadensis canadensis isolate 43U chromosome 26 
```
[Project Page](https://davidcox143.github.io/Gene2vec/)
