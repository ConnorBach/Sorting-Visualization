import time

def draw_barchart(plt, data):
    bars = plt.bar(range(1,len(data)+1), data, align='center', alpha=1, color='steelblue')
    #plt.scatter(range(1,len(data)+1), data)
    plt.draw()
    plt.pause(0.001)
    bars.remove()
