import configparser
import os
#config = configparser.ConfigParser(delimiters=(' '))
#config.read('inventory.ini')
#config.set('all', 'node1', 'ansible_host=95.54.0.12   ip=10.3.0.1 etcd_member_name=etcd1')

#with open('test_update.ini', 'w') as configfile:
#    config.write(configfile)





import json 

project_dir = os.getcwd()+'/kubespray/inventory/eks-automated-cluster/'
f = open(project_dir+'ips.json',) 
  
data = json.load(f) 

total_master = 1
total_worker = 2
node_ip = data['k8s_node_ips']['value']  
master_ip =  data['k8s_master_ips']['value']
total_nodes_ip = node_ip + master_ip
print (total_nodes_ip)  
f.close()

config = configparser.ConfigParser(delimiters=(' '),allow_no_value=True)
config.read(project_dir+'/inventory.ini')
for idx, ip in enumerate(total_nodes_ip):
    config.set('all', 'node'+str(idx), 'ansible_host='+ip+'  ' + ' ip='+ip+ ' etcd_member_name='+'etcd'+str(idx))
    config.set('etcd', 'etcd'+str(idx))

i=0
while i < total_master:
    config.set('kube-master', 'node'+str(i))
    i += 1

while i < total_worker+total_master:
    config.set('kube-node', 'node'+str(i))
    i += 1


#config.set('k8s-cluster:children', 'node'+str(idx))
with open(project_dir+'/inventory.ini', 'w') as configfile:
    config.write(configfile)

