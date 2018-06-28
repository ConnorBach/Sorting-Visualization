import time

def draw_barchart(plt, data):
    plt.clf()
    plt.bar(range(1,len(data)+1), data, align='center', alpha=1)
    plt.draw()
    plt.pause(0.001)
