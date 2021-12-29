from abaqus import *
from abaqusConstants import *
import __main__
import __future__
import numpy as np
import visualization
import collections
from numpy import sin,cos,tan,pi,arcsin,arccos,arctan,exp,log

def ploting(xrange,equation,numincre,name,Xtype,Ytype):
	equation = check_eq_strin(equation)
	X = np.linspace(xrange[0][0],xrange[0][1],numincre)
	Y = eval(compile(equation, '<string>', 'eval', __future__.division.compiler_flag))
	xQuantity = visualization.QuantityType(type=abaqusConstant(Xtype))
	yQuantity = visualization.QuantityType(type=abaqusConstant(Ytype))
	data = [(x,y) for x,y in zip(X,Y)]
	session.XYData(name=name, data=tuple(data),sourceDescription='Entered from keyboard', axis1QuantityType=xQuantity, axis2QuantityType=yQuantity, )	
	
	session.viewports['Viewport: 1'].setValues(displayedObject=None)
	if 'XYPlot-1' not in session.xyPlots.keys():
		xyp = session.XYPlot('XYPlot-1')
	else:
		xyp = session.xyPlots['XYPlot-1']
	
	chartName = xyp.charts.keys()[0]
	chart = xyp.charts[chartName]
	xy1 = session.xyDataObjects[name]
	c1 = session.Curve(xyData=xy1)
	chart.setValues(curvesToPlot=(c1, ), )
	session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
	session.mdbData.summary()

def abaqusConstant(const):
	if const == 'Time':
		return TIME
	if const == 'Displacement':
		return DISPLACEMENT
	if const == 'Force':
		return FORCE
	if const == 'Stress':
		return STRESS
	if const == 'Strain':
		return STRAIN
	if const == 'Length':
		return LENGTH
	if const == 'Position':
		return POSITION
	if const == 'Path':
		return PATH
	if const == 'XCoord':
		return X_COORD
	if const == 'YCoord':
		return Y_COORD
	if const == 'ZCoord':
		return Z_COORD
	else:
		return NONE

def check_eq_strin(str):
	startpara = 0
	endpara = 0
	stroutput = ''

	for s in str:
		if s is '(':
			startpara +=1
		if s is ')':
			endpara +=1
		if s is '^':
			print('NOTE: ^ changed to **')
			stroutput += '**'
		elif s is 'x' and s.islower():
			print('NOTE: x chaged to X')
			stroutput += 'X'
		else:
			stroutput += s
	
	stroutput = stroutput.replace("eXp", "exp")

	if endpara != startpara:
		print('ERROR: Check parentheses')
	print('Equation: '+stroutput)
	return stroutput
