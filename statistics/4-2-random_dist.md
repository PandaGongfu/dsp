[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> ![pmf and cdf](img/random.png)   
The random function did a pretty good job because the cumulative density is approximately a straight line. I guess some peudo random number generator may do a better job.   
    import random
    
    rnums = [random.random() for _ in range(0,1000)]
    r_pmf = thinkstats2.Pmf(rnums)
    r_cdf = thinkstats2.Cdf(rnums)
    
    thinkplot.PrePlot(2, cols=2)
    thinkplot.Pmf(r_pmf)
    thinkplot.Config(ylabel='probability')
    thinkplot.SubPlot(2)
    thinkplot.Cdf(r_cdf)
    thinkplot.show()


