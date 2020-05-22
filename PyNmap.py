
#!/usr/bin/python
# -*- coding: utf-8 -*-

# LIBRARIES

from datetime import date
import os
import pickle
import json
import subprocess
import difflib
# SET VARIABLES

my_dir = '/root/Desktop/123456'
my_pickle = '/root/Desktop/tmp/data.pickle'
my_json = '/root/Desktop/tmp/data.json'
port_list = ['127.0.0.1:80', '127.0.0.1:23', '127.0.0.0:22']
nmap_path = '/bin/nmap'
n_diff = '/bin/ndiff'
nmap_network = '127.0.0.1'


def create_directory():
    if os.path.isdir(my_dir) == False:
        try:
            os.mkdir(my_dir)
            print ('INFO: The directory was created:', my_dir)
        except OSError:
            print ('ERROR: Failed to create directory:', my_dir)
    else:
        print ('INFO: The directory already exists:', my_dir)


def create_date_string():
    my_pickle= date.today().strftime('%m%d%y.pickle')
    my_json = date.today().strftime('%m%d%y.json')
   # print ('Date String:', date_str)
    return my_pickle, my_json

def write_files(my_pickle,my_json, nmap_data):

    # write the pickle file

    with open(my_pickle, 'wb') as fp:
        pickle.dump(nmap_data, fp)
    fp.close()

#    json_nmap = json.dumps(nmap_data)
    # write the json file

#    with open(my_json, 'w') as fp:
 #      json.dump(nmap_data, fp)
  #  fp.close()


def read_files(my_pickle, my_json):
    

    # read the pickle file

    with open(my_pickle, 'rb') as fp:
        infile = pickle.load(fp)
    fp.close()

    print ('pickle:', infile)
    

    # read the json file

#    with open(my_json, 'r') as fp:
#        port_list = json.load(fp)
#    fp.close()

 #   print ('json:', port_list)


def run_nmap():
    nmap_out = subprocess.run([nmap_path, '-T4', nmap_network],
                              capture_output=True)
    nmap_data = nmap_out.stdout.splitlines()
    return nmap_data


nmap_data = run_nmap()
my_pickle, my_json = create_date_string()
write_files(my_pickle,my_json, nmap_data)
read_files(my_pickle, my_json)

subprocess.call([n_diff, "preListoner.pickle", "052120.pickle"])


