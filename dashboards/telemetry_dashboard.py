import matplotlib.pyplot as plt

def plot_telemetry(speed, pressure):

    plt.plot(speed, label="Speed")
    plt.plot(pressure, label="Brake Pressure")

    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.title("Vehicle Telemetry Dashboard")

    plt.legend()
    plt.show()
