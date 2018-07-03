#from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

class Grapher:
	def __init__(self, data, enableGraph):
		self.win = pg.GraphicsWindow()
		self.plt = self.win.addPlot()
		self.curve = self.plt.plot(data)
		self.enableGraph = enableGraph

	def exit(self):
		pg.QtGui.QApplication.quit()

	def update(self, data):
		if self.enableGraph:
			if (self.win.isVisible()):
				self.curve.setData(data)
				pg.QtGui.QApplication.processEvents()
			else:
				self.exit()
