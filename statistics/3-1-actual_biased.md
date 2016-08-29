[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> ```
actual mean:  1.02420515504
biased mean:  2.40367910066
```
![Actual vs Biased](biased.png)
    import chap01soln
    import thinkplot
    
    def BiasedPmf( pmf, label):
        new_pmf = pmf.Copy(label=label)
    
        for x, p in pmf.Items():
            new_pmf.Mult(x, x)
    
        new_pmf.Normalize()
        return new_pmf
    
    resp = chap01soln.ReadFemResp()
    pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
    biased = BiasedPmf(pmf, label='biased')
    
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased])
    thinkplot.Show()
    
    print('actual mean: ', pmf.Mean())
    print('biased mean: ', biased.Mean())


