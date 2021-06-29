# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""
import sys
import os
from pathlib import Path

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Printer" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

try:

    from win32 import win32api

    from win32 import win32print
except Exception as e:
    PrintException()
    raise e

module = GetParams("module")

try:

    if module == "get_printers":

        printerLocal = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
        printerConnected = win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS)
        printers = printerLocal + printerConnected
        # Uncomment the 3 lines to see in console the list of printers
        # printercount = 0
        Printers = []
        for printer in printers:
            # print(printercount, "-", printer[2])
            Printers.append(printer[2])
            # printercount += 1
        
        SetVar("Printer_fake_var", {
            "printers" : Printers,
        })
    
    if module == "default_printer":

        printerWanted = GetParams("iframe")
        printer = eval(printerWanted)["printer"]

        win32print.SetDefaultPrinter(printer)

    if module == "print_file":

        fileType = GetParams("fileType")
        defaultPrinter = win32print.GetDefaultPrinter()
        
        if (fileType == "doc"):

            myprinter = win32print.OpenPrinter(defaultPrinter)

            fileToPrint = GetParams("fileToPrint")

            win32api.ShellExecute(0, "print", '"%s"' % fileToPrint, '"%s"' % myprinter, ".", 0)

        elif (fileType == "txt"):
            fileToPrint = GetParams("fileToPrint")
            win32api.ShellExecute(0, "print", fileToPrint, None, ".", 0)
        

    if module == "folder_to_print":

        from glob import glob

        fileType = GetParams("fileType")

        defaultPrinter = win32print.GetDefaultPrinter()
        folderToPrint = GetParams("folderToPrint") + "/**/*"
        for fileToPrint in glob(folderToPrint, recursive=True):

            if (fileType == "doc"):

                myprinter = win32print.OpenPrinter(defaultPrinter)

                win32api.ShellExecute(0, "print", '"%s"' % fileToPrint, '"%s"' % myprinter, ".", 0)

            elif (fileType == "txt"):

                win32api.ShellExecute(0, "print", fileToPrint, defaultPrinter, ".", 0)

except Exception as e:
    print("\x1B[" + "31;40mError\x1B[" + "0m")
    PrintException()
    raise e