# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='XY Expression', kernelModule='abaqusMacros', kernelFunction='ploting', includeApplyBtn=True, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgIcon(p='DialogBox', fileName=r'icon.png')
RsgLabel(p='DialogBox', text='Insert X limits', useBoldFont=True)
RsgTable(p='DialogBox', numRows=1, columnData=[('Min X', 'Float', 120), ('Max X', 'Float', 120)], showRowNumbers=False, showGrids=True, keyword='xrange', popupFlags='AFXTable.POPUP_CLEAR_CONTENTS')
RsgTextField(p='DialogBox', fieldType='Integer', ncols=6, labelText='Number of increments', keyword='numincre', default='101')
RsgSeparator(p='DialogBox')
RsgLabel(p='DialogBox', text='Y Expression', useBoldFont=True)
RsgLabel(p='DialogBox', text='Example: X**2-exp(0.1*X)+1.0/2.0+sin(X*pi)', useBoldFont=False)
RsgTextField(p='DialogBox', fieldType='String', ncols=33, labelText='Y = ', keyword='equation', default='X**2-exp(0.1*X)+1.0/2.0+sin(X*pi)')
RsgSeparator(p='DialogBox')
RsgLabel(p='DialogBox', text='Name on Output', useBoldFont=True)
RsgTextField(p='DialogBox', fieldType='String', ncols=15, labelText='Name: ', keyword='name', default='Output1')
RsgSeparator(p='DialogBox')
RsgLabel(p='DialogBox', text='Data Type', useBoldFont=True)
RsgHorizontalFrame(name='HFrame_1', p='DialogBox', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgComboBox(name='ComboBox_1', p='HFrame_1', text='X:', keyword='Xtype', default='NONE', comboType='STANDARD', repository='', rootText='', rootKeyword=None, layout='')
RsgListItem(p='ComboBox_1', text='None')
RsgListItem(p='ComboBox_1', text='Time')
RsgListItem(p='ComboBox_1', text='Displacement')
RsgListItem(p='ComboBox_1', text='Force')
RsgListItem(p='ComboBox_1', text='Stress')
RsgListItem(p='ComboBox_1', text='Strain')
RsgListItem(p='ComboBox_1', text='Length')
RsgListItem(p='ComboBox_1', text='Position')
RsgListItem(p='ComboBox_1', text='Path')
RsgListItem(p='ComboBox_1', text='XCoord')
RsgListItem(p='ComboBox_1', text='YCoord')
RsgListItem(p='ComboBox_1', text='ZCoord')
RsgComboBox(name='ComboBox_3', p='HFrame_1', text='Y: ', keyword='Ytype', default='NONE', comboType='STANDARD', repository='', rootText='', rootKeyword=None, layout='')
RsgListItem(p='ComboBox_3', text='None')
RsgListItem(p='ComboBox_3', text='Time')
RsgListItem(p='ComboBox_3', text='Displacement')
RsgListItem(p='ComboBox_3', text='Force')
RsgListItem(p='ComboBox_3', text='Stress')
RsgListItem(p='ComboBox_3', text='Strain')
RsgListItem(p='ComboBox_3', text='Length')
RsgListItem(p='ComboBox_3', text='Position')
RsgListItem(p='ComboBox_3', text='Path')
RsgListItem(p='ComboBox_3', text='XCoord')
RsgListItem(p='ComboBox_3', text='YCoord')
RsgListItem(p='ComboBox_3', text='ZCoord')
dialogBox.show()