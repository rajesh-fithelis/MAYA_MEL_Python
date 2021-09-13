import os
import io
import sys
import json
import time
import ctypes

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
    # from PySide import QtGui, QtCore
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    import PySide2.QtWidgets as QtGui
    from PySide2.QtWidgets import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import PyQt5
#sys.path.insert(0, r"E:\rajeshf_intern\jsonQT")
from botje import Ui_botShotForm

class MainDialog(Ui_botShotForm, QtGui.QDialog):
    
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.startup_configFile_check()
        self.startup_baseJSON_File_check()
        self.loadShots()
        self.previewButton.clicked.connect(self.previewButtonClicked)
        #Text
        self.previewTreeWidget.itemSelectionChanged.connect(self.previewTreeItemSelected)
        self.editEditPushButton.clicked.connect(self.editButtonClicked)
        self.editSavePushButton.clicked.connect(self.editSaveButtonClicked)
        #self.getProgressPushButton.clicked.connect(self.loadAllMessages)
        #self.folderDialog()
        #Add Button click @ Create Tab
        self.createPushButton.clicked.connect(self.addButtonClicked)
        self.tabWidget.currentChanged.connect(self.tabFocus)
        self.editDirectoryPushButton.clicked.connect(self.editDirectoryPushButtonClicked)
        self.deleteDeletePushButton.clicked.connect(self.deleteDeletePushButtonClicked)
        self.settingsCreatePushButton.clicked.connect(self.settingsCreatePushButtonClicked)
        self.settingsDirectoryPushButton.clicked.connect(self.settingsDirectoryPushButtonClicked)

    def startup_configFile_check(self):
        if os.path.isfile("config.json") and os.access("config.json", os.R_OK):
            # checks if file exists
            print ("Config file is readable and ready to access-\nStatus: success")
        else:
            print ("Either file is missing or is not readable, creating file...")
            cwd = os.getcwd()
            configFile = "config.json"
            config= dict()
            config["base_directory"]=cwd
            config["base_JSON_file_name"]="data.json"
            with io.open(os.path.join(cwd, configFile), 'w') as db_file:
                db_file.write(json.dumps(config))
                print("Config file creation done - \nStatus: success")
                #startup_baseJSON_File_check()

    def startup_baseJSON_File_check(self):
        #read the config JSON and read the base-file-name first
        cwd = os.getcwd()
        configFile = os.path.join(cwd, "config.json")
        print("Config File: ",configFile)
        with open(configFile, "r") as jsonFile:
            jsonData = json.load(jsonFile)    
        print(jsonData)
       #read the base file name    
        DATA_FILENAME = jsonData["base_JSON_file_name"]
        BASE_DIRECTORY = jsonData["base_directory"]
        
        print("Data File: ",DATA_FILENAME)
        print("Base Directory: ",BASE_DIRECTORY)

        cwd = os.getcwd()
        dataFile = os.path.join(BASE_DIRECTORY, DATA_FILENAME)
        print(dataFile)

        data= dict()
        data["data"] =   list(dict())
        print(data)
        feeds = list()
        #check the file exist or not
        if os.path.isfile(dataFile) and os.access(dataFile, os.R_OK):
            # checks if file exists
            print ("base JSON file is readable and ready to access-\nStatus: success")
        else:
            print ("Either the base JSON file is missing or is not readable, creating file...")
            with io.open(os.path.join(BASE_DIRECTORY, DATA_FILENAME), 'w') as db_file:
                db_file.write(json.dumps(data))
                print("base JSON file creation done - \nStatus: success")    

    def configCreateEdit(self,fileName,path):
        #read the config JSON and read the base-file-name first
        cwd = os.getcwd()
        configFile = os.path.join(cwd, "config.json")
        print(configFile)
        with open(configFile, "r") as jsonFile:
            jsonData = json.load(jsonFile)    

        #read the base file name    
        newJSONDATA ={}
        newJSONDATA["base_JSON_file_name"]=fileName
        newJSONDATA["base_directory"]=path
        with io.open(os.path.join(cwd, configFile), 'w') as db_file:
            if db_file.write(json.dumps(newJSONDATA)):
                print("New JSON file creation done! - \nStatus: success") 
                return 200
            else:
                print("Config file write failed!")
                return 401
        #After the alteration call the startup_baseJSON_File_check() function  
        print(newJSONDATA)    

    def settingsCreatePushButtonClicked(self):
        newJSONFileName = self.settingsNewFileNameLineEdit.text()
        newBaseDirectory = self.settingsBaseDirectoryLineEdit.text()
        configStatus = self.configCreateEdit(newJSONFileName,newBaseDirectory)
        if configStatus==200:
            self.startup_baseJSON_File_check()
            ret = QMessageBox.warning(self, self.tr("Information"), self.tr("New JSON file creation done!" + "\n" +"Config file altered successfully!"), QMessageBox.Ok)
        elif configStatus==401:
            ret = QMessageBox.warning(self, self.tr("Critical"), self.tr("Somthing went wrong with File disk write, permission ..."+"\n"+"Contact your BOTVFX development team!"), QMessageBox.Ok)

    def loadShots(self):
        baseJSONPath = self.getBaseJSONFilePath()
        with open(baseJSONPath) as f:
            shotsData=json.load(f)
            #previewTreeWidget
            #print(shotsData['data'][0]['type'])
        varData=shotsData['data']
        for info in varData:
            #print(info)
            previewTreeShot = QTreeWidgetItem([
                                    info['type'],
                                    info['department'],
                                    info['render'],
                                    info['version'],
                                    info['output_path']
                                   ]) #previewTreeWidget
            self.previewTreeWidget.addTopLevelItem(previewTreeShot)
            deleteTreeShot = QTreeWidgetItem([
                                    info['type'],
                                    info['department'],
                                    info['render'],
                                    info['version'],
                                    info['output_path']
                                   ]) #deleteTreeWidget
            self.deleteTreeWidget.addTopLevelItem(deleteTreeShot)
            #self.deleteTreeWidget.addTopLevelItem(deleteTreeShot)
            #print(shotsData)

    def previewButtonClicked(self):
        print("previewButtonClicked")
        #check the type and version text entered
        versionlineEditValue = self.previewVersionLineEdit.text()
        typeLineEditValue = self.previewTypeLineEdit.text()
        if len(versionlineEditValue.strip()) ==0 or len(typeLineEditValue.strip()) ==0:
            print("Enter a type/shot name to process the output!")
            self.finalPreviewOutputLabel.setText("Enter a type/shot name to process the output!")
            #msgBox = QMessageBox()
            #msgBox.setText("Shot/Version is Empty!.")
            #msgBox.setInformativeText("Select a shot from the list OR enter the version and shot to generate the output.")
            ret = QMessageBox.warning(self, self.tr("ERROR"),
                               self.tr("Shot/Version is Empty.\n" + \
                                  "Select a shot from the list OR enter the version and shot to generate the output."),
                               QMessageBox.Ok
                               )
            #msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            #msgBox.setStandardButtons(QMessageBox.Ok)
            #msgBox.setDefaultButton(QMessageBox.Ok)
            #ret = msgBox.exec_()          
            #ctypes.windll.user32.MessageBoxW(0, "Enter a type/shot name to process the output!", "ERROR: Empty!", 0)
        else:
            self.previewVersionLineEdit.setText(versionlineEditValue)
            #print (self.previewVersionLineEdit.text())
            self.previewTypeLineEdit.setText(typeLineEditValue)
            #print (self.previewTypeLineEdit.text())

        selectedPreviewTreeValues = self.previewTreeWidget.selectedItems()
        finalStringValue = ""
        if selectedPreviewTreeValues:
            baseNode    = selectedPreviewTreeValues[0]

            shot_typeValue   = baseNode.text(0)
            shot_departmentValue = baseNode.text(1)
            shot_renderValue = baseNode.text(2)
            shot_versionValue     = baseNode.text(3)
            shot_base_pathValue   = baseNode.text(4)
            print(shot_typeValue)
            print(shot_renderValue)
            print(shot_departmentValue)
            print(shot_versionValue)
            print(shot_base_pathValue)
            finalStringValue += shot_base_pathValue
            finalStringValue += '/'
            finalStringValue += shot_versionValue
            finalStringValue += '/'
            finalStringValue += shot_typeValue
            finalStringValue += '_'
            finalStringValue += shot_departmentValue
            finalStringValue += '/'

            extractShotName = self.extractShotName(str(typeLineEditValue))
            splitList = extractShotName.split(":")
            
            if len(splitList)>1:
                start = splitList[0]
                end = splitList[1]
                if len(start)==0:
                    start=0
                else:
                    start=int(start)
                if len(end)==0:
                    end=0
                else:
                    end=int(end)
                if start==0 and end==0:
                    start=0
                    end=len(shot_typeValue)
                if start>0 and end==0:
                    end=len(shot_typeValue)
            elif len(splitList)==0 and extractShotName.isdigit():
                #without colon entered only a number
                start = 0
                end = int(extractShotName)
            else:
                #without colon some raw string entered means 
                #display the whole string
                start=0
                end=len(shot_typeValue)

            extractShotName = shot_typeValue[start:end]
            finalStringValue += extractShotName #shot_typeValue
            finalStringValue += '_'
            finalStringValue += shot_departmentValue
            finalStringValue += '.mov'
            self.finalPreviewOutputLabel.setText(finalStringValue)

    def previewTreeItemSelected(self):
        print("previewTreeItemSelected")
        selectedPreviewTreeValues = self.previewTreeWidget.selectedItems()
        if selectedPreviewTreeValues:
            baseNode    = selectedPreviewTreeValues[0]

            shot_versionValue     = baseNode.text(3)
            shot_base_pathValue   = baseNode.text(4)
            shot_typeValue   = baseNode.text(0)
            shot_departmentValue = baseNode.text(2)
            shot_renderValue = baseNode.text(1)

            print (shot_typeValue, ', ', shot_versionValue)
            self.previewVersionLineEdit.setText(shot_versionValue)
            self.previewTypeLineEdit.setText(shot_typeValue)


        #self.ui.lineEdit.setText("safa")
        #print self.ui.lineEdit.text()

    def settingsDirectoryPushButtonClicked(self):
        baseFolderPathValue = self.folderDialog()
        self.settingsBaseDirectoryLineEdit.setText(baseFolderPathValue)

    def editDirectoryPushButtonClicked(self):
        baseFolderPathValue = self.folderDialog()
        self.editDirectoryLineEdit.setText(baseFolderPathValue)

    def folderDialog(self):
         selected_directory = QtGui.QFileDialog.getExistingDirectory()
         print ('selected_directory:', selected_directory)
         return selected_directory

    def extractShotName(self,s):
        start = s.find('[')
        if start == -1:
            # No opening bracket found. Should this be an error?
            return ''
        start += 1  # skip the bracket, move to the next character
        end = s.find(']', start)
        if end == -1:
            # No closing bracket found after the opening bracket.
            # Should this be an error instead?
            return s[start:]
        else:
            return s[start:end]

    def addButtonClicked(self):
        shotName = self.createTypeLineEdit.text()
        departmentValue = self.createDepartmentComboBox.currentText()
        renderValue = self.createRenderLineEdit.text()
        versionValue = self.createVersionLineEdit.text()
        baseJSONPath = self.getBaseJSONFilePath()
        insertStatus = self.addShotsJSON(shotName.lower(),renderValue,departmentValue,versionValue,baseJSONPath)
        if insertStatus==200:
            self.createRenderLineEdit.setText("")
            self.createVersionLineEdit.setText("")
            self.createTypeLineEdit.setText("")
            ret = QMessageBox.warning(self, self.tr("Information"), self.tr("Shot inserted successfully!"), QMessageBox.Ok)
        elif insertStatus==400:
            #Sorry shot already exist!
            ret = QMessageBox.warning(self, self.tr("Warning"), self.tr("Shot already exist!"), QMessageBox.Ok)
        elif insertStatus==401:
            ret = QMessageBox.warning(self, self.tr("Critical"), self.tr("Somthing went wrong with File disk write, permission ..."+"\n"+"Contact your administrator!"), QMessageBox.Ok)

    def tabFocus(self):
        self.previewTreeWidget.clear()
        self.deleteTreeWidget.clear()
        """
        for i in reversed(range(previewTreeWidget.childCount())):
            parent.removeChild(previewTreeWidget.child(i))
        """
        self.loadShots()
        print ("Preview Tab Clicked!")

    def editButtonClicked(self):
        fetchRecord = self.editTypeLineEdit.text()
        self.getRecord(fetchRecord)

    def deleteDeletePushButtonClicked(self):
        deleteRecord = self.deleteTypeLineEdit.text()
        delete_status = self.deleteShotJSON(deleteRecord)
        if delete_status==200:
            self.tabFocus()
            ret = QMessageBox.warning(self, self.tr("Information"), self.tr("Shot deleted successfully!"), QMessageBox.Ok)
        elif delete_status==401:
            ret = QMessageBox.warning(self, self.tr("Critical"), self.tr("Shot not get deleted and File not saved! Contact your BOTVFX development team!"), QMessageBox.Ok)
        elif delete_status==400:
            ret = QMessageBox.warning(self, self.tr("Critical"), self.tr("No match found!"), QMessageBox.Ok)         

    def getRecord(self,typ):
        cwd = os.getcwd()
        configFile = os.path.join(cwd, "config.json")
        print(configFile)
        with open(configFile, "r") as jsonFile:
            jsonData = json.load(jsonFile)    

       #read the base file name    
        DATA_FILENAME = jsonData["base_JSON_file_name"]
        print(DATA_FILENAME)

        cwd = os.getcwd()
        dataFile = os.path.join(cwd, DATA_FILENAME)
        print(dataFile)

        #new_entry = {"type": tpe, "render": render,"department": department,"version": version,"output_path": output_path }
        #read all data from the dataFile
        dataExist = 0
        matchType =""
        matchVersion = ""
        matchDepartment = ""
        matchRender = ""
        matchOutputPath = ""
        with open(dataFile) as f:
            shotsData=json.load(f)
        chkData = shotsData["data"]
        flag=0
        match_flag =0
        for inrow in chkData:
            chkType = inrow["type"].lower()
            tmpEditType = typ.lower()
            if chkType == tmpEditType:
                matchType = inrow["type"]
                matchVersion = inrow["version"]
                matchDepartment = inrow["department"]
                matchRender = inrow["render"]
                matchOutputPath = inrow["output_path"]

                dataExist = 1
                match_flag = flag
            flag +=1

        if dataExist==1:
            print("Match found!")
            self.editRenderLineEdit.setText(matchRender)
            self.editDirectoryLineEdit.setText(matchOutputPath)
            self.editVersionLineEdit.setText(matchVersion)
            dataExist =0
            match_flag=0
            flag =0
        else:
            print ("No matching record found")
            ret = QMessageBox.warning(self, self.tr("Information"), self.tr("No matching record found!"), QMessageBox.Ok)

#---------------------------------------------------------------------------------------------------
# Add a new SHOT START------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

    def addShotsJSON(self,tpe,render,department,version,output_path):
        #read the config JSON and read the base-file-name first
        cwd = os.getcwd()
        configFile = os.path.join(cwd, "config.json")
        print(configFile)
        with open(configFile, "r") as jsonFile:
            jsonData = json.load(jsonFile)    

       #read the base file name    
        DATA_FILENAME = jsonData["base_JSON_file_name"]
        print(DATA_FILENAME)

        cwd = os.getcwd()
        dataFile = os.path.join(cwd, DATA_FILENAME)
        print(dataFile)

        data= dict()
        data["data"] =   list(dict())
        print(data)
        feeds = list()
        #check the file exist or not
        if os.path.isfile(dataFile) and os.access(dataFile, os.R_OK):
            # checks if file exists
            print ("base JSON file is readable and ready to access-\nStatus: success")
        else:
            print ("Either the base JSON file is missing or is not readable, creating file...")
            with io.open(os.path.join(cwd, DATA_FILENAME), 'w') as db_file:
                db_file.write(json.dumps(data))
                print("base JSON file creation done - \nStatus: success")

        new_entry = {"type": tpe, "render": render,"department": department,"version": version,"output_path": output_path }
        
        #read all data from the dataFile
        dataExist = 0
        with open(dataFile) as f:
            shotsData=json.load(f)
        chkData = shotsData["data"]
        for inrow in chkData:
            chkType = inrow["type"].lower()
            newType = new_entry["type"].lower()
            if chkType == newType:
                dataExist = 1

        if dataExist==1:
            print("Sorry shot already exist!")
            dataExist=0
            return 400
        else:
            shotsData['data'].append(new_entry)
            with io.open(os.path.join(cwd, DATA_FILENAME), 'w') as db_file:
                if db_file.write(json.dumps(shotsData)):
                    print("New data added!  - \nStatus: success")
                    return 200
                else:
                    return 401


# Add a new SHOT END--------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Edit a new SHOT START-----------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
    def editSaveButtonClicked(self):
        editTypeText = self.editTypeLineEdit.text()
        editRenderText = self.editRenderLineEdit.text()
        editVersionText = self.editVersionLineEdit.text()
        editOutput_pathText = self.editDirectoryLineEdit.text()
        editStatus = self.editSaveShotsJSON(editTypeText,editRenderText,editVersionText,editOutput_pathText)
        if editStatus==200:
            ret = QMessageBox.warning(self, self.tr("Information"), self.tr("Shot edited successfully!"), QMessageBox.Ok)
            self.editRenderLineEdit.setText("")
            self.editDirectoryLineEdit.setText("")
            self.editVersionLineEdit.setText("")
        elif editStatus==401:
            ret = QMessageBox.warning(self, self.tr("Critical"), self.tr("File not saved! Contact your BOTVFX development team!"), QMessageBox.Ok)
        elif editStatus==400:
            ret = QMessageBox.warning(self, self.tr("Critical"), self.tr("No match found!"), QMessageBox.Ok)            

    def editSaveShotsJSON(self,editType,render,version,output_path):
        cwd = os.getcwd()
        configFile = os.path.join(cwd, "config.json")
        print(configFile)
        with open(configFile, "r") as jsonFile:
            jsonData = json.load(jsonFile)    

       #read the base file name    
        DATA_FILENAME = jsonData["base_JSON_file_name"]
        print(DATA_FILENAME)

        cwd = os.getcwd()
        dataFile = os.path.join(cwd, DATA_FILENAME)
        print(dataFile)

        #new_entry = {"type": tpe, "render": render,"department": department,"version": version,"output_path": output_path }
        #read all data from the dataFile
        dataExist = 0
        with open(dataFile) as f:
            shotsData=json.load(f)
        chkData = shotsData["data"]
        print (chkData)
        flag=0
        match_flag =0
        for inrow in chkData:
            chkType = inrow["type"].lower()
            print(chkType)
            tmpEditType = editType.lower()
            print(tmpEditType)
            if chkType == tmpEditType:
                dataExist = 1
                match_flag = flag
                print("Match found - Break flag!")
                break
            flag +=1

        if dataExist==1:
            print("Match found!")
            shotsData["data"][match_flag]["render"] = render
            shotsData["data"][match_flag]["version"] = version
            shotsData["data"][match_flag]["output_path"] = output_path
            dataExist =0
            match_flag=0
            flag =0
            with io.open(os.path.join(cwd, DATA_FILENAME), 'w') as db_file:
                if db_file.write(json.dumps(shotsData)):
                    print("base JSON file edit done - \nStatus: success")
                    return 200
                else:
                    return 401
        else:
            print("No match found!")
            return 400
                
# Edit a new SHOT END-------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# DELETE a SHOT START-------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

    def deleteShotJSON(self,editType):
        cwd = os.getcwd()
        configFile = os.path.join(cwd, "config.json")
        print(configFile)
        with open(configFile, "r") as jsonFile:
            jsonData = json.load(jsonFile)    

       #read the base file name    
        DATA_FILENAME = jsonData["base_JSON_file_name"]
        print(DATA_FILENAME)

        cwd = os.getcwd()
        dataFile = os.path.join(cwd, DATA_FILENAME)
        print(dataFile)

        #new_entry = {"type": tpe, "render": render,"department": department,"version": version,"output_path": output_path }
        #read all data from the dataFile
        dataExist = 0
        with open(dataFile) as f:
            shotsData=json.load(f)
        chkData = shotsData["data"]
        flag=0
        match_flag =0
        for inrow in chkData:
            chkType = inrow["type"].lower()
            tmpEditType = editType.lower()
            if chkType == tmpEditType:
                dataExist = 1
                del shotsData["data"][flag]
                match_flag = flag
            flag +=1

        if dataExist==1:
            print("Match found!")
            with io.open(os.path.join(cwd, DATA_FILENAME), 'w') as db_file:
                if db_file.write(json.dumps(shotsData)):
                    print("Match found and deleted - \nDelete Status: success")
                    return 200
                else:
                    return 400
        else:
            print("No match found!")            
            return 401

# DELETE a SHOT END---------------------------------------------------------------------------------

    def getBaseJSONFilePath(self):
        cwd = os.getcwd()
        configFile = os.path.join(cwd, "config.json")
        with open(configFile, "r") as jsonFile:
            jsonData = json.load(jsonFile)
        #read the base file name
        DATA_FILENAME = jsonData["base_JSON_file_name"]
        DATA_FILE_PATH = jsonData["base_directory"]
        print(DATA_FILE_PATH)
        print(DATA_FILENAME)
        cwd = os.getcwd()
        dataFile = os.path.join(DATA_FILE_PATH, DATA_FILENAME)
        return dataFile

    def getBaseJSONFileName(self):
        cwd = os.getcwd()
        configFile = os.path.join(cwd, "config.json")
        with open(configFile, "r") as jsonFile:
            jsonData = json.load(jsonFile)
        #read the base file name
        DATA_FILENAME = jsonData["base_JSON_file_name"]
        cwd = os.getcwd()
        dataFile = os.path.join(cwd, DATA_FILENAME)
        return dataFile

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainDialog()
    ex.show()
    sys.exit(app.exec_())