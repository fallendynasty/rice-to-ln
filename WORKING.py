from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os 

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file_name = askopenfilename() # show an "Open" dialog box and return the path to the selected file

new_file = os.path.dirname(file_name) + '\\' + os.path.basename(file_name)[:-4] + '[no ln].osu'
# print(file_name, '\n', new_file)
with open(new_file, 'w', encoding="utf-8") as g:
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()
        hit_start = False
        for i in range(len(data)):
            line = data[i]
            if hit_start:
                line = line.split(',') #https://osu.ppy.sh/wiki/en/Client/File_formats/osu_%28file_format%29#hit-objects
                line[3] = '1' #rice object type
                hitSample = line[5].split(':')
                if len(hitSample) == 6: #remove endTime 
                    hitSample = hitSample[1:]
                line[5] = ":".join(hitSample)   
                line = ','.join(line)
            if line[:7] == 'Version': #change the name
                line = line[:-1] + ' no ln\n' 

            if line == '[HitObjects]\n': #hit object section reached
                hit_start = True
            data[i] = line

        g.writelines(data)

