import csv

source_file = r"C:\Users\user\Documents\7. JUL\01072018.TXT"
output_file = r"C:\Users\user\Documents\7. JUL\output.csv"
s_date = '01072018'
file = open(source_file,'r')
output_dict = {'CASH':0, 'MASTER':0, 'NETS':0, 'VISA':0, 'VOUCHER':0, 'NET B/4 Tax':0, 'Inclusive 7% Tax':0}
s = False
for line in file:
    if 'Z-REPORT(Daily)' in line:
        s = True
    elif 'CANCEL' in line:
        s = False
    if s:
        for key, value in output_dict.items():
            if key in line:
                line = line.replace('\n','')
                if 'CASHCARD' in line:
                    continue
                output_dict[key] = float(line[25:])


    with open(output_file, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Date', 'CASH', 'MASTER', 'NETS', 'VISA', 'VOUCHER', 'GST TAXABLE', '7% GST'])
        output_list = [s_date]
        for k, v in output_dict.items():
            output_list.append(str(v))
        filewriter.writerow(output_list)

file.close()