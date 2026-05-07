import mnist
import numpy as np
import matplotlib.pyplot as plt

def load_mnist_samples(num_samples=5):
    X_train, y_train = mnist.train_images(), mnist.train_labels()

    # Select random samples from the MNIST dataset
    indices = np.random.choice(len(X_train), num_samples, replace=False)
    samples = X_train[indices]
    labels = y_train[indices]

    return samples, labels

def plot_mnist_samples(samples, labels, num_cols=5):
    num_samples = samples.shape[0]
    num_rows = int(np.ceil(num_samples / num_cols))

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 3 * num_rows))

    for i in range(num_samples):
        row = i // num_cols
        col = i % num_cols
        ax = axes[row, col] if num_rows > 1 else axes[col]
        ax.imshow(samples[i], cmap='gray')
        ax.set_title(f"Label: {labels[i]}", fontsize=10)
        ax.axis('off')

    plt.show()

if __name__ == "__main__":
    # Example usage:
    mnist_samples, mnist_labels = load_mnist_samples(num_samples=10)
    plot_mnist_samples(mnist_samples, mnist_labels)
