# COMP90024ASM2

## Contributor
| Surname | Given name | Student ID | Contact                          |
|---------|------------|------------|----------------------------------|
| Guan    | Xueting    | 1076010    | guaxg@student.unimelb.edu.au     |
| Zhou    | Eryi       | 1257309    | eryiz@student.unimelb.edu.au     |
| Li      | Yi         | 1103422    | yi10@student.unimelb.edu.au      |
| Zhao    | Jian       | 1131605    | jianzhao2@student.unimelb.edu.au |
| Sun     | Kunxi      | 1225759    | kunxis@student.unimelb.edu.au    |


## How to auto deploy the system
Before you deploy the system:
* Make sure you have the ansible downloaded. The prefered version of Ansible is **2.10.8**
* Connect to Anyconnect VPN with url: remote.unimelb.edu.au/student.
* Change the python interpreter path in *ansible/host_vars/mrc-common.yaml* 

* First, create ssh key pair, and upload the public key to MRC

        ssh-keygen -t rsa -f id-asm2 

    Note: You can name the key as any name you want, but if you create it in a different name, you need to change the variable of key name in the path *./ansible/mrc-common.yaml* which is *instance_key_name* 
  
* Download your own openstackRC file from MRC, and put it in the ansible folder 
* Go to ansible folder

        cd ansible   

* Run the command 
    To deploy instance on MRC
  
         . ./<your open rc file>; ansible-playbook mrc.yaml --ask-become-pass

    Note that you are required to input the mrc password, and BECOME password. mrc password can be generated in mrc setting. BECOME password is your sudo password.

    T

    TO deploy couchdb cluster on instance
        
        ansible-playbook web.yaml --ask-become-pass -i inventory/hosts.ini
    
    TO deploy web app and web server on instance
        
        ansible-playbook web.yaml --ask-become-pass -i inventory/hosts.ini
## System Architecture




  
## Demo video
* Harvester
*Part1: https://youtu.be/7amPRdHpvN4
* Create the instance
*Part2: https://youtu.be/YdCYpG4NP7s
*Web app
*Part3: https://youtu.be/VWbJ1dKj5ek
* Couchdb and MapReduce
*Part4: https://youtu.be/BgTXzn-5bsc


## Dependencies:
### Ansible
* Ansible

### Harvester:
* TwitterAPI
* couchdb

### Webapp:
* React
* Nginx Proxy

### Data analysis
* numpy
* matplotlib
* textblob
* couchdb
