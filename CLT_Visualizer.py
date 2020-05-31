# This module is intended to illustrate the central limit theorem (sum and average versions) as it applies to several common distributions
# It is intended to be instructional

import matplotlib.pyplot as plt
from statistics import mean, pstdev
from RandomNumbersWithDistributions import *
from sys import argv

def HistSum(dist, n, tot):
	"""Generate tot random variables Z_j = sum(X_1, X_2, ..., X_n)
	Where X_i is an iid random variable with distribution dist for all i
	Z_j will be approximately normal(mu=n*mean(X_1), sqrt(n)*stdev(X_1)) for all 1 <= j <= tot
	The histogram plot of all Z_j's will be displayed to help the student visualize the Central Limit Theorem (sum case)"""
	dist = dist.lower()
	Z_vals = []
	if dist in ('unif', 'uniform'):
		a = float(input("Enter a value for a (lower bound): "))
		b = float(input("Enter a value for b (upper bound): "))
		for i in range(tot):
			Z_vals.append(sum([UnifNum(a, b) for _ in range(n)]))
	if dist in ('expo', 'exponential'):
		rate = float(input("Enter a value for λ (rate): "))
		for i in range(tot):
			Z_vals.append(sum([ExpoNum(rate) for _ in range(n)]))
	if dist in ('bin', 'bino', 'binomial'):
		n_ = int(input("Enter a value for n (number of trials per binomial RV): "))
		p = float(input("Enter a value for p (success probability): "))
		for i in range(tot):
			Z_vals.append(sum([BinomialNum(n_, p) for _ in range(n)]))
	if dist in ('geo', 'geom', 'geometric'):
		p = float(input("Enter a value for p (success probability): "))
		for i in range(tot):
			Z_vals.append(sum([GeometricNum(p) for _ in range(n)]))
	if dist in ('discrete uniform', 'discunif', 'disc unif', 'dunif'):
		a = int(input("Enter a value for a (lower bound): "))
		b = int(input("Enter a value for b (upper bound): "))
		for i in range(tot):
			Z_vals.append(sum([DiscUnifNum2(a, b) for _ in range(n)]))
	if dist in ('pareto',):
		alpha = float(input("Enter a value for α (scale parameter): "))
		for i in range(tot):
			Z_vals.append(sum([ParetoNum(alpha) for _ in range(n)]))
	if dist in ('weibull', 'wb', 'wbl'):
		alpha = float(input("Enter a value for α (shape parameter): "))
		lambd = float(input("Enter a value for λ (scale parameter): "))
		for i in range(tot):
			Z_vals.append(sum([WeibullNum(alpha, lambd) for _ in range(n)]))


	to_print =  (f"The mean of this collection of random variables is:  {mean(Z_vals)}"
				"\n"
				f"The standard deviation of this collection of random variables is:  {pstdev(Z_vals)}"
				"\n")
	print(to_print)
	plt.hist(Z_vals)
	plt.show()
	return

def HistAvg(dist, n, tot):
	"""Generate tot random variables Z_j = (1/n)*sum(X_1, X_2, ..., X_n)
	Where X_i is an iid random variable with distribution dist for all i
	Z_j will be approximately normal(mu=mean(X_1), stdev(X_1)/sqrt(n)) for all 1 <= j <= tot
	The histogram plot of all Z_j's will be displayed to help the student visualize the Central Limit Theorem (average case)"""
	dist = dist.lower()
	Z_vals = []
	if dist in ('unif', 'uniform'):
		a = float(input("Enter a value for a (lower bound): "))
		b = float(input("Enter a value for b (upper bound): "))
		for i in range(tot):
			Z_vals.append(sum([UnifNum(a, b) for _ in range(n)]))
	if dist in ('expo', 'exponential'):
		rate = float(input("Enter a value for λ (rate): "))
		for i in range(tot):
			Z_vals.append(sum([ExpoNum(rate) for _ in range(n)]))
	if dist in ('bin', 'bino', 'binomial'):
		n_ = int(input("Enter a value for n (number of trials per binomial RV): "))
		p = float(input("Enter a value for p (success probability): "))
		for i in range(tot):
			Z_vals.append(sum([BinomialNum(n_, p) for _ in range(n)]))
	if dist in ('geo', 'geom', 'geometric'):
		p = float(input("Enter a value for p (success probability): "))
		for i in range(tot):
			Z_vals.append(sum([GeometricNum(p) for _ in range(n)]))
	if dist in ('discrete uniform', 'discunif', 'disc unif', 'dunif'):
		a = int(input("Enter a value for a (lower bound): "))
		b = int(input("Enter a value for b (upper bound): "))
		for i in range(tot):
			Z_vals.append(sum([DiscUnifNum2(a, b) for _ in range(n)]))
	if dist in ('pareto',):
		alpha = float(input("Enter a value for α (scale parameter): "))
		for i in range(tot):
			Z_vals.append(sum([ParetoNum(alpha) for _ in range(n)]))
	if dist in ('weibull', 'wb', 'wbl'):
		alpha = float(input("Enter a value for α (shape parameter): "))
		lambd = float(input("Enter a value for λ (scale parameter): "))
		for i in range(tot):
			Z_vals.append(sum([WeibullNum(alpha, lambd) for _ in range(n)]))

	Z_vals = [_/n for _ in Z_vals]

	to_print =  (f"The mean of this collection of random variables is:  {mean(Z_vals)}"
				"\n"
				f"The standard deviation of this collection of random variables is:  {pstdev(Z_vals)}"
				"\n")
	print(to_print)
	plt.hist(Z_vals)
	plt.show()
	return

if __name__ == '__main__':
	if len(argv) == 1:
		print("\nAdditional command line argument needed to determine whether to use sum or average.")
		exit(1)
	argv[1] = argv[1].lower()
	if argv[1] in ('sum', 's'):
		use_sum = True
	elif argv[1] in ('avg', 'a', 'average'):
		use_sum = False
	else:
		print("\nInvalid command line argument for using sum or average.")
		exit(1)
	dist = input("Enter a distribution to use: ")
	n = int(input("Enter a value for n (Z = X1 + X2 + .. + Xn): "))
	tot = int(input("Enter a value for the total number of random variables to generate for the histogram: "))
	if use_sum:
		HistSum(dist, n, tot)
	else:
		HistAvg(dist, n, tot)