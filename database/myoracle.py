#conding : utf-8

import cx_Oracle

fp = open('D:\\DeviceInfo_mailai.txt','wb')
conn = cx_Oracle.connect('pfdb/pfdb@162.168.2.79/ora11g')

cur = conn.cursor()

sql = 'select bsid,bs_type,bs_position,longitude,latitude from kbs_station_info '

cur.execute(sql)
conn.commit()
data = cur.fetchall()
cur.close()
conn.close()

for i in range(len(data)):
    fp.write(data[i][0]+'\t'+data[i][1]+'\t'+data[i][2]+'\t'+data[i][3]+'\t'+data[i][4]+'\n')     

fp.close()

