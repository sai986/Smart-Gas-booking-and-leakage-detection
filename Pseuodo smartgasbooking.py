from random import randint
def read_configfile():
    fin = open("config.txt","r")
    lines= tuple(fin)
    config = {}
    for line in lines:
       config[line.split(":")[0]]=line.split(":")[1]   
    fin.close()
    return config
    
def weight_read():
    return randint(0,9)

def call_number(phnum):
    print "calling number",phnum,"\n"

def estimate_gas_lastage():
    print "Estimated running of gas cylinder : 3 days\n"

config_arr=read_configfile()
while(1):
    weight=weight_read()
    print "weight",weight
    if( weight < float(config_arr["min_weight"])):
        estimate_gas_lastage()
        call_number(config_arr["phonenum"])

    
