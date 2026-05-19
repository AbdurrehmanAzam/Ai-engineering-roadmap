import csv
from matplotlib import pyplot as plt

plt.style.use("ggplot")
months = []
profit = []

with open(r"C:\Users\Abdurrehman_Azam\Downloads\company_sales_data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        months.append(int(row["month_number"]))
        profit.append(int(row["total_profit"]))

months.reverse()
profit.reverse()

plt.barh(months, profit, color="#0320FD")

plt.title("Company profit per month")

plt.xlabel("Total profit")
plt.ylabel("Month number")
plt.grid(True)
plt.show()
