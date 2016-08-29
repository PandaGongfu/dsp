[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
```
Cohen d -0.088672927072602
```
```python
    import nsfg
    import thinkstats2
    
    preg = nsfg.ReadFemPreg()
    nsfg.CleanFemPreg(preg)
    
    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]
    
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Cohen d', d)
```