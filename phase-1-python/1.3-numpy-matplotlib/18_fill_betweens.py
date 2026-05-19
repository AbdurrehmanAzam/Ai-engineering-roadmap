from matplotlib import pyplot as plt

ages = list(range(18, 56))

dev_salaries = [
    17784,
    16500,
    18012,
    20628,
    25206,
    30252,
    34368,
    38496,
    42000,
    46752,
    49320,
    53200,
    56000,
    62316,
    64928,
    67317,
    68748,
    73752,
    77232,
    78000,
    78508,
    79536,
    82488,
    88935,
    90000,
    90056,
    95000,
    90000,
    91633,
    91660,
    98150,
    98964,
    100000,
    98988,
    100000,
    108923,
    105000,
    103117,
]

py_salaries = [
    20046,
    17100,
    20000,
    24744,
    30500,
    37732,
    41247,
    45372,
    48876,
    53850,
    57287,
    45000,
    50000,
    55000,
    70000,
    71496,
    75370,
    83640,
    84666,
    84392,
    78254,
    85000,
    87038,
    91991,
    100000,
    94796,
    97962,
    93302,
    99240,
    102736,
    112285,
    100771,
    104708,
    108423,
    101407,
    112542,
    122870,
    120000,
]

plt.plot(ages, dev_salaries, color="#444444", linestyle="--", label="All Devs")
plt.plot(ages, py_salaries, label="Python")

plt.fill_between(
    ages,
    py_salaries,
    dev_salaries,
    where=[p > d for p, d in zip(py_salaries, dev_salaries)],
    interpolate=True,
    alpha=0.25,
    label="Above Avg",
)

plt.fill_between(
    ages,
    py_salaries,
    dev_salaries,
    where=[p <= d for p, d in zip(py_salaries, dev_salaries)],
    interpolate=True,
    color="red",
    alpha=0.25,
    label="Below Avg",
)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.legend()
plt.tight_layout()
plt.show()
