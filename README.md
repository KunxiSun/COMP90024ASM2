# COMP90024ASM2

## Contributor
| Surname| Given name | Student ID | Contact                          |
|--------|------------|------------|--------------------------------—-|
| Guan   |  Xueting   | 1076010    | guaxg@student.unimelb.edu.au     |
| Zhou   | Eryi       | 1257309    | eryiz@student.unimelb.edu.au     |
| Li     |  Yi        | 1103422    | yi10@student.unimelb.edu.au      |
| Zhao   |  Jian      | 1131605    | jianzhao2@student.unimelb.edu.au |
| Sun    |  Kunxi     | 1225759    | kunxis@student.unimelb.edu.au    |


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


    TO deploy couchdb cluster on instance
        
        ansible-playbook web.yaml --ask-become-pass -i inventory/hosts.ini
    
    TO deploy web app and web server on instance
        
        ansible-playbook web.yaml --ask-become-pass -i inventory/hosts.ini
## Presentation slides
https://docs.google.com/presentation/d/13BIvwDQTOCIpdS13aw6p4WH74d4aI65FDofiA2VryDg/edit?usp=sharing

## System Architecture

![image](https://github.com/KunxiSun/COMP90024ASM2/blob/main/img/Architecture.png)
* The CouchDB cluster is deployed at the first three instances. Web server and web app are deployed on the second instances. The fourth instance is used to constantly run the harvester to retrieve data from Twitter API.
* The architecture of system is shown in the figure above, Harvest derives the data from Twitter through API and store the data into CouchDB dataset. The analyzer such as MapReduce and machine learning process the data and store into files. Web app can get the data through sever which connected to databased. The visualization is present on the Web app
## Front End (http://172.26.134.30:8080)
* The front end is built in JavaScript, Css and HTML using the web framework Vue. This component-based development technology was chosen as it provided easy access to libraries that facilitated the use of google maps which are used to demonstrate map. In addition, Vue can provide convenient visualization tools which can help with drawing graphs.
## Back End
* Data server
* Machine learning Server
* Harvest
## Database
* Three couchdb database in instance 1~3 are combined as a cluster

  
## Demo video
### Harvester
* Part1: https://youtu.be/7amPRdHpvN4
### Create the instance (Ansible)
* Part2: https://youtu.be/YdCYpG4NP7s
### Web app (Ansible)
* Part3: https://youtu.be/VWbJ1dKj5ek
### Couchdb and MapReduce
* Part4: https://youtu.be/BgTXzn-5bsc


## Dependencies:
### Ansible
* Ansible
* Docker

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
* Couchdb
### Docker files
* CouchDB
* https://hub.docker.com/_/couchdb
* Web app image
* https://hub.docker.com/r/emostudio/group57-webapp
* Data server
* https://hub.docker.com/r/emostudio/group57-dataserver
## Instance
* Instance 1: 172.26.130.11
* Instance 2: 172.26.134.30
* Instnace 3: 172.26.130.62
* Instance 4: 172.26.129.117
