import matplotlib.pyplot as plt

# Training and validation accuracy values
train_acc = [0.82, 0.92, 0.96, 0.98, 0.99]
val_acc = [0.78, 0.88, 0.92, 0.95, 0.97]

# Define x-axis labels
epochs = range(1, len(train_acc) + 1)

# Plot the graph
plt.plot(epochs, train_acc, 'orange', label='Training Accuracy')
plt.plot(epochs, val_acc, 'blue', label='Validation Accuracy')

# Set the title and axis labels
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')

# Add legend to the plot
plt.legend()

# Display the graph
plt.show()
