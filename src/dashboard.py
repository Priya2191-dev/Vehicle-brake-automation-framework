import matplotlib.pyplot as plt

def plot(speed, pressure):
    plt.plot(speed)
    plt.plot(pressure)
    plt.savefig("plot.png")
    plt.close()
