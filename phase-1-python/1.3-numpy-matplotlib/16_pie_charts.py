from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [23, 34, 12, 36, 45]
labels = ["Urdu", "English", "Islamiyat", "Biology", "Maths"]
colors = ["#020290", "#960505", "#079207", "#05AFB8", "#D108AC"]
explode = [0, 0, 0, 0.02, 0]
plt.pie(
    slices,
    labels=labels,
    colors=colors,
    explode=explode,
    shadow=True,
    startangle=90,
    autopct="%1.1f%%",
    wedgeprops={"edgecolor": "black"},
)

plt.title("Marks Percentages")

plt.tight_layout()
plt.show()
