import csv
import os
from tkinter import filedialog
from tkinter import *

path = filedialog.askdirectory()
file_list = []
if os.path.isdir(path):
    for filename in os.listdir(path):
        if filename.endswith('.TXT'):
            file_list.append(filename)

    output_file = os.path.join(path,'output.csv')
    with open(output_file, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Date', 'CASH', 'MASTER', 'NETS', 'VISA', 'VOUCHER', 'GST TAXABLE', '7% GST'])

        output_dict = {'CASH ': 0, 'MASTER ': 0, 'NETS ': 0, 'VISA ': 0, 'VOUCHER ': 0, 'NET B/4 Tax:': 0, 'Inclusive 7% Tax:': 0}
        for source_file in file_list:
            s_date = source_file[:-4]
            file = open(os.path.join(path,source_file), 'r')
            s = False
            for line in file:
                if 'Z-REPORT(Daily)' in line:
                    s = True
                elif 'CANCEL' in line:
                    s = False
                if s:
                    for k, v in output_dict.items():
                        if k in line:
                            line = line.replace('\n','')
                            if 'CASHCARD' in line:
                                continue
                            output_value = line[25:]
                            if ',' in output_value:
                                output_value = output_value.replace(',', '')
                            output_dict[k] = float(output_value)
            output_list = [s_date]
            for k,v in output_dict.items():
                output_list.append(str(v))
            filewriter.writerow(output_list)

file.close()