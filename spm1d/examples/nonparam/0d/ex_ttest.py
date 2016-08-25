
import numpy as np
import spm1d




#(0) Create data:
y          = np.array([0.4, 0.2, 0.5, 0.3, -0.1])
mu         = 0


#(1) Conduct non-parametric test:
alpha      = 0.05
two_tailed = False
tn         = spm1d.stats.nonparam.ttest(y, mu)
tni        = tn.inference(alpha, two_tailed=two_tailed)
print( 'Non-parametric results:' )
print(tni)


#(2) Compare to parametric test:
t          = spm1d.stats.ttest(y, mu)
ti         = t.inference(alpha, two_tailed=two_tailed)
print( 'Parametric results:' )
print( ti )

