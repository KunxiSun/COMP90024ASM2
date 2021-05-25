# COMP90024ASM2

## Contributor
| Surname | Given name | Student ID | Contact                          |
|---------|------------|------------|----------------------------------|
| Guan    | Xueting    | 1076010    | guaxg@student.unimelb.edu.au     |
| Zhou    | Eryi       | 1257309    |                                  |
| Li      | Yi         | 1103422    |                                  |
| Zhao    | Jian       | 1131605    | jianzhao2@student.unimelb.edu.au |
| Sun     | Kunxi      | 1225759    | kunxis@student.unimelb.edu.au    |


## How to auto deploy the system
* Before you deploy the system, make sure you have the ansible downloaded
  The prefered version of Ansible is 2.10.8

* First, create ssh key pair:  

        ssh-keygen -t rsa -f id-asm2 

    Note: You can name the key as any name you want, but if you create it in a different name, you need to change the variable of key name in the path *./ansible/mrc-common.yaml* which is *instance_key_name* 
* Download your own openstackRC file from MRC, and put it in the ansible folder 
* Go to ansible folder

        cd ansible   

* Run the command 
  
         . ./<your open rc file>; ansible-playbook mrc.yaml --ask-become-pass
    Note that you are required to input the mrc password, and BECOME password. mrc password can be generated in mrc setting. BECOME password is your sudo password.

## Demo video


## Dependencies:
### Ansible
* Ansible

### Harvester:
* TwitterAPI
* couchdb

### Webapp:
* Node.js
* npm

### Data analysis
* numpy
* matplotlib
* textblob
* couchdb