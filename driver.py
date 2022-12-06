from Finance_pkg.monte_carlo_val_eu_op import monte_carlo_val_eu_call_option

s= 100
k = 105
t = 1
r = 0.05
sigma = 0.2

mceco = monte_carlo_val_eu_call_option(s,k,t,r,sigma,Print=True, currency='Euro')

