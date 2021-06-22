# import win32print, win32api
# import sys
# #from pathlib import Path

# print(win32print.GetDefaultPrinter())
# printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
# printercount = 0
# for x in printers:
#     print(printercount, "-", x[2])
#     printercount += 1

# chosenprinter = int(input("Printer number? "))

# #print(chosenprinter)
# #print(printers[chosenprinter][2])
# print(win32print.GetDefaultPrinter())
# win32print.SetDefaultPrinter(printers[chosenprinter][2])
# print(win32print.GetDefaultPrinter())
# #print(win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL))

# #chosenfile = Path()
# #while not chosenfile.is_file():
# #    filename = "C:/Users/danil/Downloads/TE-50615042100310109010000100001040000000057131657581.pdf"
# #    chosenfile = Path(filename)

# #myprinter = win32print.OpenPrinter(printers[chosenprinter][2])

# #printjob = win32print.StartDocPrinter(
# #    myprinter, 1, ("Python test RAW print", None, "raw"))

# #with open(chosenfile, mode='rb') as file:
# #    buf = file.read()

# #win32api.ShellExecute(0, "printto", '"%s"' % filename, '"%s"' % myprinter, ".", 0)
# #bytesprinted = win32print.WritePrinter(myprinter, buf)



# #win32print.EndDocPrinter(myprinter)
# #win32print.ClosePrinter(myprinter)

#terrible = [["Company","Contact","Country"],["Alfreds Futterkiste","Maria Anders","Germany"],["Centro comercial Moctezuma","Francisco Chang","Mexico"],["Ernst Handel","Roland Mendel","Austria"],["Island Trading","Helen Bennett","UK"],["Laughing Bacchus Winecellars","Yoshi Tannamuri","Canada"],["Magazzini Alimentari Riuniti","Giovanni Rovelli","Italy"]]

#for each in terrible:
#    for cada in each:
#        cada.replace("\"", "'")
# terrible.replace("\"", "'")

#print(terrible)

# import win32gui
# print(win32gui.__file__)

# handleInfo = []

# def winEnumHandler(hwnd, ctx):
#             global handleInfo
#             if win32gui.IsWindowVisible(hwnd):
#                 handleInfo.append((hwnd, win32gui.GetWindowText(hwnd)))

# print(win32gui.EnumWindows(winEnumHandler, None))

# for h in handleInfo:
#     print(h[1])

import win32api
import win32print

printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
Printers = []
printercount = 0
for printer in printers:
    print(printercount, "-", printer[2])
    Printers.append(printer[2])
    printercount += 1

print(printers[1][0])
print(win32print.GetDefaultPrinter())
print(printers[3][2])
win32print.SetDefaultPrinter(printers[3][2])