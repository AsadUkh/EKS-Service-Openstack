import re
import os

content ={
    "cluster" : {
        "cluster_name" : "hell-auto-cluster",
        "network_name": "hell_testing_net_kube",
        "number_of_worker" : "hell_2",
        "number_of_master": "hell_l1",
        "subnet_cidr": "hell_192.168.2.0/24",  
		"floatingip_pool" : "hell_external"
    
    }
}
def str_replace(fname, pat, s_after):
  with open(fname) as f:
        out_fname = fname + ".tmp"
        out = open(out_fname, "w")
        for line in f:
            out.write(re.sub(pat, s_after, line))
        out.close()
        os.rename(out_fname, fname)

filename = '/home/asad/KUBE_AUTO/projects/api/kubespray/inventory/kube-auto-cluster/cluster.tfvars_bkp'
pattern = '\s*=\s*([\S\s]+)'
str_replace(filename, 'cluster_name' +pattern , 'cluster_name = '+ '"'+ content['cluster']['cluster_name']+'"'+'\n')
str_replace(filename, 'number_of_k8s_nodes' +pattern , 'number_of_k8s_nodes = '+ content['cluster']['number_of_worker']+'\n')
str_replace(filename, 'number_of_k8s_masters' +pattern , 'number_of_k8s_masters = '+ content['cluster']['number_of_master']+'\n')
str_replace(filename, 'network_name' +pattern , 'network_name = '+'"'+content['cluster']['network_name']+'"'+'\n')
str_replace(filename, 'floatingip_pool' +pattern , 'floatingip_pool = '+'"'+content['cluster']['floatingip_pool']+'"'+'\n')
str_replace(filename, 'subnet_cidr' +pattern , 'subnet_cidr = '+'"'+ content['cluster']['subnet_cidr']+'"'+'\n')


