# Import matplotlib library here
import matplotlib.pyplot as plt
# Let's rank some of our favorite snacks
snack_scores = [200, 100, 75]
slice_labels = ["Popcorn", "Chocolate","Nachos"]

# Let's make a pie chart!
plt.pie(snack_scores, labels=slice_labels)

# Give your pie chart a title in the quotes
plt.title("Jasmine's Fav Snacks")

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("Fav_snacks.png")

