# https://support.vector.com/kb?id=kb_article_view&sysparm_article=KB0012474&sys_kb_id=3735c2681b2614148e9a535c2e4bcba0&spa=1
import time, os, msvcrt,sys
from win32com.client import *
from win32com.client.connect import *
mApp = DispatchEx('CANoe.Application')
mMeasurement    =   mApp.Measurement
mSystem         =   mApp.System
mNamespaces     =   mSystem.Namespaces
mNamespace      =   mNamespaces.Item("python")
mVariables      =   mNamespace.Variables
m_voltage       =   mVariables.Item("voltage")
m_current       =   mVariables.Item("current")
m_py_exit       =   mVariables.Item("py_exit")


# while True:
while not msvcrt.kbhit():
# if msvcrt.kbhit():
    time.sleep(1)
    print("******************")
    print('voltage = ', m_voltage.Value)
    m_current.Value = m_current.Value +0.1
    # print(m_py_exit.Value)
    # print(int(1))
    print("******************")
    if (m_py_exit.Value):
        # quit(1)
        # quit()
        exit()
        # sys.exit(1)
