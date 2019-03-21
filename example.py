import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import numpy as np
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from IPython.display import display
import os
import string
import shutil
import wfdb
from wfdb import processing

class mainMenu(QDialog):
  def __init__(self, parent=None):
    super (mainMenu, self).__init__(parent)

    layout = QVBoxLayout()
 
    self.b = QPushButton("Open bin file")
    self.b.setDefault(True)
    self.b.clicked.connect(self.Open_bin_file)
    layout.addWidget(self.b)

    self.b1 = QPushButton("Open xml file")
    self.b1.setDefault(True)
    self.b1.clicked.connect(self.Open_file)
    layout.addWidget(self.b1)

    self.b2 = QPushButton("New xml file")
    self.b2.setDefault(True)
    self.b2.clicked.connect(self.New_file)
    layout.addWidget(self.b2)

    self.setLayout(layout)
    self.setWindowTitle("Hl7")

  def New_file(self):
    ebx = NewFile()
    ebx.show()
       
  def Open_file(self):
    ecx = combodemo()
    ecx.show()

  def Open_bin_file(self):
    s = QFileDialog.getOpenFileName(self, 'Select file')
    _plot_(str(s))


class NewFile(QWidget):
  def __init__(self, parent = None):
    super(NewFile, self).__init__(parent)

    layout = QFormLayout()
    self.b = QLabel()
    self.b.setText("Clinic")
    layout.addRow(self.b)

    self.btn0 = QPushButton("Get Start Time")
    self.btn0.clicked.connect(self.getTime1)
    self.le0 = QLineEdit()
    layout.addRow(self.btn0, self.le0)

    self.btn1 = QPushButton("Get Finish Time")
    self.btn1.clicked.connect(self.getTime2)
    self.le1 = QLineEdit()
    layout.addRow(self.btn1, self.le1)

    self.btn2 = QPushButton("Clinical Trial")
    self.btn2.clicked.connect(self.getClinc)
    self.le2 = QLineEdit()
    layout.addRow(self.btn2, self.le2)

    self.btn3 = QPushButton("Country")
    self.btn3.clicked.connect(self.getCountry)
    self.le3 = QLineEdit()
    layout.addRow(self.btn3,self.le3)

    self.btn4 = QPushButton("Sity")
    self.btn4.clicked.connect(self.getSity)
    self.le4 = QLineEdit()
    layout.addRow(self.btn4,self.le4)

    self.b0 = QLabel()
    self.b0.setText("Personal data")
    layout.addRow(self.b0)

    self.btn5 = QPushButton("Full name")
    self.btn5.clicked.connect(self.getName)
    self.le5 = QLineEdit()
    layout.addRow(self.btn5,self.le5)

    self.btn6 = QPushButton("Race")
    self.btn6.clicked.connect(self.getRace)
    self.le6 = QLineEdit()
    layout.addRow(self.btn6,self.le6)

    self.b1 = QLabel()
    self.b1.setText("Birthday")
    layout.addRow(self.b1)

    self.birthdayEdit = QDateEdit(self)
    self.le7 = QLineEdit()
    self.birthdayEdit.setDateTime(QDateTime.currentDateTime())
    self.birthdayEdit.setMaximumDate(QDate(2222, 12, 22))
    self.birthdayEdit.setCalendarPopup(True)
    layout.addRow(self.birthdayEdit, self.le7)
    self.connect(self.birthdayEdit, SIGNAL("dateChanged(QDate)"), self.updateDate)


    self.b1 = QRadioButton("Male")
    self.b1.setChecked(True)
    self.b1.toggled.connect(lambda:self.getGendr(self.b1))
    layout.addWidget(self.b1)

    self.b2 = QRadioButton("Female")
    self.b2.toggled.connect(lambda:self.getGendr(self.b2))
    layout.addWidget(self.b2)

    self.bf = QPushButton("Open bin file")
    self.bf.setDefault(True)
    self.bf.clicked.connect(self.binFile)
    layout.addWidget(self.bf)

    self.button_close = QPushButton('Add')
    self.button_close.clicked.connect(self.close)
    layout.addWidget(self.button_close)

    self.setLayout(layout)
    self.setWindowTitle("Input Dialog demo")

  def getTime1(self):
    item, ok = QInputDialog.getText(self, "Time", "Input Start Time")
       
    if ok:
      self.le0.setText(str(item))

    addStartTime(item)
   
  def getTime2(self):
    item1, ok = QInputDialog.getText(self, "Time", "Input Finish Time")
          
    if ok:
      self.le1.setText(str(item1))

    addFinishTime(item1)

  def getClinc(self):
    item2, ok = QInputDialog.getText(self, "Clinic Name", 'Input name:')

    if ok:
      self.le2.setText(str(item2))

    addClinicName(item2)
         
  def getCountry(self):
    item3, ok = QInputDialog.getText(self,"Country","Get Country")
      
    if ok:
      self.le3.setText(str(item3))

    addCountry(item3)

  def getSity(self):
    item4, ok = QInputDialog.getText(self,"Sity","Get Sity")

    if ok:
      self.le4.setText(str(item4))

    addSity(item4)

  def getName(self):
    item5, ok = QInputDialog.getText(self,"Name","Input Full name:")

    if ok:
      self.le5.setText(str(item5))
    
    addName(item5)

  def getRace(self):
    race = ("RaceNativeAmerican", "RaceAsian", "RaceBlackOrAfricanAmerican", 
      "RaceHawaiianOrPacificIsland", "RaceWhite", "OtherRace")
    race, ok = QInputDialog.getItem(self, "Race", 
      "list of Race", race, 0, False)
 
    if ok and race:
      self.le6.setText(race)

    addRace(race)

  def updateDate(self):
    date1 = self.birthdayEdit.date()
    self.le7.setText(date1.toString())
    
    addBirthday(date1)
      
  def binFile(self):
    s = QFileDialog.getOpenFileName(self, 'Select file')
    if (s != ''):
      addSignalLead(str(s))

  def getGendr(self,b):
   
    if b.text() == "Male":
      if b.isChecked() == True:
        addGendr('M')  
    if b.text() == "Female":
      if b.isChecked() == True:
        addGendr('F')

    SaveChange()

def main():
  app = QApplication(sys.argv)
  ex = mainMenu()
  ex.show()
  sys.exit(app.exec_())
   
_numberLead_ = {
      'I': 1,
      'II': 2,
      'III': 9,
      'V1': 3,
      'V2': 4,
      'V3': 5,
      'V4': 6,
      'V5': 7,
      'V6': 8,
      'AVR': 10,
      'AVL': 11,
      'AVF': 12
  }
 
   #I, II, V1, V2, V3, V4, V5, V6, III, AVR, AVL, AVF

def formatingTime(_item_):
  _item_ = (_item_[6:10] + _item_[3:5] + _item_[0:2] + _item_[11:13] + _item_[14:16])
  return _item_

def addStartTime(_item_):
  global personalDate
  personalDate[0][4][0][2][0][2][0].attrib = dict([('value', str(formatingTime(str(_item_))))])
  SaveChange()

def addFinishTime(_item_):
  global personalDate
  personalDate[0][4][0][2][0][2][1].attrib = dict([('value', str(formatingTime(str(_item_))))])
  SaveChange()

def addGendr(_item_):
  global personalDate
  personalDate[0][4][0][0][0][2][1].attrib = dict([('value', str(_item_))])
  SaveChange()

def addCountry(_item_):
  global personalDate
  personalDate[0][4][0][2][0][5][0][1][1][0].text = str(_item_)
  SaveChange()

def addSity(_item_):
  global personalDate
  personalDate[0][4][0][2][0][5][0][1][1][2].text = str(_item_)
  personalDate[0][4][0][2][0][5][0][1][1][1].text = ''
  SaveChange()

def addRace(_item_):
  _codeRace_ = {
          'RaceNativeAmerican': "1002-5",
          'RaceAsian': "2028-9",
          'RaceBlackOrAfricanAmerican': "2054-5",
          'RaceHawaiianOrPacificIsland': "2076-8",
          'RaceWhite': "2106-3",
          'OtherRace': "2131-1"
      }
  global personalDate
  personalDate[0][4][0][0][0][2][3].attrib = dict([('displayName', str(_item_)),
                                                     ('code', str(_codeRace_[str(_item_)]))])
  SaveChange()

def addClinicName(_item_):
  global personalDate
  personalDate[0][4][0][2][0][1].text = str(_item_)
  SaveChange()

def addName(_item_):
  global personalDate
  personalDate[0][4][0][0][0][2][0].text = str(_item_)
  SaveChange()

def formatingBirthday(_item_):
  _item_ = _item_[19:]
  _item_ = _item_.replace(")", "")
  _item_ = _item_.replace(",", "")
  flg = False
  counter = 0
  sdd = list(_item_)
  for i in range(len(_item_)):
      if (flg == False and _item_[i] != " "):
          continue
      elif (_item_[i] == ' ' and flg == False):
          flg = True
      elif (_item_[i] != " " and flg):
          print(counter)
          counter += 1
      elif (_item_[i] == " " and flg):
          if (counter == 1):
              sdd[i-2] = '0'
          counter = 0
  if (counter == 1):
      sdd[len(_item_)-2] = '0'
  _item_ = ''.join(sdd)
  _item_ = _item_.replace(" ", "")
  return _item_

def addBirthday(_item_):
  global personalDate
  personalDate[0][4][0][0][0][2][2].attrib = dict([('value', str(formatingBirthday(str(_item_))))])
  SaveChange()

doc = ET.parse("ex.xml") 
a = doc.getroot()
personalDate = a.find('{urn:hl7-org:v3}componentOf')

def addSignalLead(_nameFile_):
  global res
  global a
  s = a.find('{urn:hl7-org:v3}component')

  _nameFile_ = _nameFile_[string.rfind(_nameFile_, '/') + 1:string.find(_nameFile_, '.')]
  record = wfdb.rdrecord(str(_nameFile_)) 
  #wfdb.plot_wfdb(record=record, title='Record a103l from Physionet Challenge 2015')
  leadFromBin = record.p_signal
  nameLeadFrobBin = record.sig_name
  leadFromBin = leadFromBin * 100

  for i in range(12):
    s[0][8][0][i + 1][0][1][2].text = ''
  if (nameLeadFrobBin[0] == 'ECG'):
    for i in range(len(leadFromBin)):
      s[0][8][0][1][0][1][2].text += str(int(leadFromBin[i][0]))
      s[0][8][0][1][0][1][2].text += ' '
      if (i == 1000):
        break
  else:
    for i in range(len(leadFromBin)):
       for j in range(len(leadFromBin[i])):
          s[0][8][0][_numberLead_[nameLeadFrobBin[j]]][0][1][2].text += str(int(leadFromBin[i][0]))
          s[0][8][0][_numberLead_[nameLeadFrobBin[j]]][0][1][2].text += ' '
       if (i == 1000):
          break
  SaveChange()

def SaveChange():
  global doc
  doc.write('output.xml', encoding='utf-8')

def _plot_(_nameFile_):
  _nameFile_ = _nameFile_[string.rfind(_nameFile_, '/') + 1:string.find(_nameFile_, '.')]
  record = wfdb.rdrecord(str(_nameFile_))
  wfdb.plot_wfdb(record=record, title='Record Physionet' + _nameFile_) 

if __name__ == '__main__':
  main()