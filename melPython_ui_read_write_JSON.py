# Autodesk MAYA MEL/Python
# Get User Data in UI and Save in JSON and Disply the Saved Data Back in Other TAB
# ------------------UI to create ticket which will have two tabs------------------
# 1)First tab will have a form to feed following details and save it as a picked or JSON file
#   a)Name
#   b)E-mail ID
#   c)Ticket type e.g.: Hardware, Software
#   d)Message.
# 2)Second tab will display the data in saved picked or JSON file.
# Rajesh Fithelis
# Email: rajeshf@live.com
import maya.cmds as cmds
import io
import json
import os

def cellChangedCB(pRow, pClm, pValue):
    return 1
    
def saveJSON(*args):
    name = cmds.textField("nameOfTexFld", query=True, text=True)
    email_id = cmds.textField("EmailId", query=True, text=True)
    ticket_type = cmds.optionMenu("ticketType", query = True, value = True)
    message = cmds.textField("messageld", query=True, text=True)
    #write to JSON
    #check the file exist or not
    data = {}
    data['ticket'] = []
    data['ticket'].append({
    'name': name,
    'email_id': email_id,
    'ticket_type': ticket_type,
    'message': message
    })
    PATH = os.getcwd()
    print(os.path.join(PATH, 'data.json'))
    if os.path.isfile(os.path.join(PATH, 'data.json')) and os.access(os.path.join(PATH, 'data.json'), os.R_OK):
        # checks if file exists
        with open(os.path.join(PATH, 'data.json'), 'r') as f:
            data = json.load(f)
            data['ticket'].append({
            'name': name,
            'email_id': email_id,
            'ticket_type': ticket_type,
            'message': message
            })
            with io.open(os.path.join(PATH, 'data.json'),'w',encoding="utf-8") as outfile:
                outfile.write(unicode(json.dumps(data, ensure_ascii=False)))          
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")
        with io.open(os.path.join(PATH, 'data.json'),'w',encoding="utf-8") as outfile:
            outfile.write(unicode(json.dumps(data, ensure_ascii=False))) 
    loadData()

def loadData():
    PATH = os.getcwd()
    if os.path.isfile(os.path.join(PATH, 'data.json')) and os.access(os.path.join(PATH, 'data.json'), os.R_OK):
        # checks if file exists
        with open(os.path.join(PATH, 'data.json'), 'r') as f:
            json_obj = json.load(f)
            u=0
            for i in json_obj['ticket']:
                print i['name']
                cmds.scriptTable(spr, e=True, ci=[1+u, 1], cv=i['name'])
                cmds.scriptTable(spr, e=True, ci=[1+u, 2], cv=i['email_id'])
                cmds.scriptTable(spr, e=True, ci=[1+u, 3], cv=i['ticket_type'])
                cmds.scriptTable(spr, e=True, ci=[1+u, 4], cv=i['message'])
                u += 1
                            
cmds.window(title="Test 2", iconName='Short Name', widthHeight=(750, 250) )
form = cmds.formLayout()
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

tab1 =  cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 600)] )
cmds.text( label='Name:  ' )
name = cmds.textField("nameOfTexFld", tx="")
cmds.text( label='E-mail ID:  ' )
email_id = cmds.textField("EmailId", tx="")

cmds.text( label='Ticket type:  ' )
ticket_type = cmds.optionMenu("ticketType")
cmds.menuItem( label='Hardware' )
cmds.menuItem( label='Software' )
cmds.menuItem( label='Service' )

cmds.text( label='Message:  ' )
message = cmds.textField("messageld", tx="")
cmds.text( label='' )
cmds.text( label='' )
cmds.text( label='' )
cmds.button( label='Submit', command=saveJSON )
cmds.setParent( '..' )

tab2 = cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=750 )
frm = cmds.formLayout(nd=100)
spr = cmds.scriptTable(c=4, r=500, cw=[[1, 100], [2, 100], [3, 100], [4, 700]], l=[[1, "Name"], [2, "E-mail ID"], [3, "Ticket type"], [4, "Message"]], ccc=cellChangedCB)
cmds.formLayout(frm, e=True, af=[[spr, 'right', 0], [spr, 'left', 0], [spr, 'top', 0], [spr, 'bottom', 0]])

for i in xrange(500):
   cmds.scriptTable(spr, e=True, ir=1)

loadData()

cmds.setParent( '..' )

cmds.tabLayout( tabs, edit=True, tabLabel=((tab1, 'Feed'), (tab2, 'Read')) )

cmds.showWindow()