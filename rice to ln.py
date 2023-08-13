import os 

filedir = os.getcwd()
for file in os.listdir(filedir):
    if file[-4:] == '.osu':
        file_name = os.path.join(filedir, file)
        new_file = os.path.basename(file_name)[:-4] + '[no ln].osu'
        with open(new_file, 'w') as g:
            with open(file_name) as f:
                data = f.readlines()
                hit_start = False
                for i in range(len(data)):
                    line = data[i]
                    if hit_start:
                        line = line.split(',')
                        line[3] = '1'
                        hitSample = line[5].split(':')
                        if len(hitSample) == 6:
                            hitSample = hitSample[1:]
                        line[5] = ":".join(hitSample)   
                        line = ','.join(line)
                    if line[:7] == 'Version':
                        line = line[:-1] + ' no ln\n' 

                    if line == '[HitObjects]\n':
                        hit_start = True
                    data[i] = line
                    
                g.writelines(data)
