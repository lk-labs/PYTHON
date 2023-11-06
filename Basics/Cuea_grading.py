from tabulate import tabulate

units = ["CMT 210", "CMT 208", "CMT 205", "CMT 203", "CMT 212"]
data = []

for index, unit in enumerate(units):
    data.append([index, unit])

table = tabulate(data, headers=["Index", "Value"], tablefmt="pretty")

print(table)
