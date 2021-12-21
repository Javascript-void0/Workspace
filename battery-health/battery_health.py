import os
import datetime

os.system("powercfg /batteryreport")
d = datetime.datetime.now()
try:
    os.rename('battery-report.html', f'battery-health/reports/battery-report-{d.month}-{d.day}-{d.year}.html')
    os.startfile(f'battery-health\\reports\\battery-report-{d.month}-{d.day}-{d.year}.html')
except WindowsError:
    print(' > Data already collected today')

files = os.listdir('battery-health/reports')
for i in range(len(files)):
    f = open(f'battery-health/reports/{files[i]}', 'r')
    lines = f.readlines()
    for line in lines:
        if 'FULL CHARGE CAPACITY' in line and 'mWh' in line:
            l = line.split('<td>')
            l = l[2].replace('\n', '')
    name = files[i].split('-')
    files[i] = f'{name[2]}/{name[3]}/{name[4][:4]}: {l}'

log = open(f'battery-health/log.txt', 'w')
log.writelines(files)
log.close()

print(' > Done')