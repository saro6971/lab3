import os
import swiftclient.client
import time
import paramiko

config = {'username':os.environ['OS_USERNAME'], 
          'api_key':os.environ['OS_PASSWORD'],
          'project_id':os.environ['OS_TENANT_NAME'],
          'auth_url':os.environ['OS_AUTH_URL'],
           }

from novaclient.client import Client
nc = Client('2',**config)


image = nc.images.find(name = "Ubuntu Server 14.04 LTS (Trusty Tahr)")
flavor = nc.flavors.find(name = "m1.medium")
keypair = nc.keypairs.find(name = "sarokey_very_secure")
network = nc.networks.find(label = "ACC-Course-net")


server = nc.servers.create(name = "SaroMasterAssignment3",
                           image = image.id,
                           flavor = flavor.id,
                           network = network.id,
                           key_name = keypair.name,
                           userdata = open('/home/sam/Desktop/Assignment 2/user_data_file.sh'))

time.sleep(4)
#nc.floating_ip_pools.list()
#floating_ip = nc.floating_ips.create(nc.floating_ip_pools.list()[0].name)

#server.addresses
#server.add_floating_ip(floating_ip)
server.add_floating_ip("130.238.29.31")