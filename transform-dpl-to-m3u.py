file_name='/home/cs/1223.DPL'
file_name2='/home/cs/d.m3u'
d=open(file_name2,'a')
d.write('#EXTM3U\n')
with open(file_name) as f:
    lines=f.readlines()
    print(len(lines))
for i in range(0,len(lines)-1,2):
    biaoti=lines[i+1].split('*')
    wangzhi=lines[i].split('*')
    biaoti_final='#EXTINF:-1,group-title="频道",'+biaoti[2]
    wangzhi_final=wangzhi[2]
    d.write(biaoti_final)
    d.write(wangzhi_final)
d.close()
