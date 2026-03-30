import matplotlib.pyplot as plt

def plot(speed, pressure):
    if len(speed) != len(pressure):
        raise ValueError("Speed and pressure must have same length")

    plt.figure()

    plt.plot(speed, label="Speed")
    plt.plot(pressure, label="Brake Pressure")

    plt.title("Vehicle Brake Dashboard")
    plt.xlabel("Time")
    plt.ylabel("Values")

    plt.legend()

    plt.savefig("plot.png")
    plt.close()
