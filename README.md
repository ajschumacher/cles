# Common-Language Effect Size

The Common-Language Effect Size (CLES) is the probability that a sample from one group is greater than a sample from another group. It's used sometimes as the effect size accompanying a [Mann–Whitney U test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test). If the two groups are positive and negative examples for a classifier, it's the same thing as [AUC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic).

This is a Python implementation that calculates the exact (non-parametric) value. It enforces the strict inequality (no half-credit when equal).

```python
from cles import cles
cles([1, 2], [2, 3])
## 0.75
```

---

 * [It's the Effect Size, Stupid: What effect size is and why it is important](https://www.leeds.ac.uk/educol/documents/00002182.htm)
 * [McGraw and Wong (1992) A common language effect size measure](https://www.researchgate.net/publication/232493691_A_common_language_effect_size_measure)
 * [Kerby, D. S. (2014) The simple difference formula: an approach to teaching nonparametric correlation](http://journals.sagepub.com/doi/pdf/10.2466/11.IT.3.1)
