import matplotlib.pyplot as plt

def plot_speed(speed_data):

    plt.plot(speed_data)

    plt.title("Vehicle Speed During Braking")

    plt.xlabel("Time")
    plt.ylabel("Speed")

    plt.show()
