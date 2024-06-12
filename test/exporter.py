#import library
from prometheus_client import start_http_server, Gauge
import time
import subprocess
import re

#Metrik
Cluster_UT =Gauge('Cluster_UT', 'Metrik yang menghitung jumlah koneksi node ipfs-cluster UT')
Cluster_ITS=Gauge('Cluster_ITS', 'Metrik yang menghitung jumlah koneksi node ipfs-cluster ITS')
Cluster_ITTP=Gauge('Cluster_ITTP', 'Metrik yang menghitung jumlah koneksi node ipfs-cluster ITTP')
Cluster_UNISA=Gauge('Cluster_UNISA', 'Metrik yang menghitung jumlah koneksi node ipfs-cluster UNISA')

#Function jalankan bash script
def run_bash_script():
    result = subprocess.run(['./test/bash_script.sh'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    return output

#Function mengelola hasil dari bash script untuk mendapatkan metrik koneksi node ipfs-cluster
def cluster_peers():
    output = run_bash_script()
    matches = re.findall(r'cluster-(\w+) \| Sees (\d+) other peers', output)
    PT = [match[0] for match in matches]
    peers = [int(match[1]) for match in matches]
    Cluster_UT.set(float(0))
    Cluster_ITS.set(float(0))
    Cluster_ITTP.set(float(0))
    Cluster_UNISA.set(float(0))
    for i in PT:
        if i=="UT":
            posisi = PT.index(i)
            Cluster_UT.set(float(peers[posisi]))
        elif i=="ITS":
            posisi = PT.index(i)
            Cluster_ITS.set(float(peers[posisi]))
        elif i=="ITTP":
            posisi = PT.index(i)
            Cluster_ITTP.set(float(peers[posisi]))
        elif i=="UNISA":
            posisi = PT.index(i)
            Cluster_UNISA.set(float(peers[posisi]))

#jalankan app prometheus_client sebagai exporter
if __name__ == '__main__':
    start_http_server(2512)
    while True:
        cluster_peers()
        time.sleep(10)
