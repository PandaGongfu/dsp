[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> ```
Percentage is 34.27
```
    import scipy
    
    hi = scipy.stats.norm.cdf((6*12+1)/39.3700787*100, 178, 7.7)
    low = scipy.stats.norm.cdf((5*12+10)/39.3700787*100, 178, 7.7)
    
    print('Percentage is %4.2f' % ((hi - low) * 100))


