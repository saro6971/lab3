import os
import swiftclient.client
import time


config = {'username':os.environ['OS_USERNAME'], 
          'api_key':os.environ['OS_PASSWORD'],
          'project_id':os.environ['OS_TENANT_NAME'],
          'auth_url':os.environ['OS_AUTH_URL'],
           }

from novaclient.client import Client
nc = Client('2',**config)


image = nc.images.find(name = "SaroAssignment3Snap")
flavor = nc.flavors.find(name = "m1.medium")
keypair = nc.keypairs.find(name = "sarokey_very_secure")



server = nc.servers.create(name = "SaroMasterAssignment3",
                           image = image.id,
                           flavor = flavor.id,
                           key_name = keypair.name,)

time.sleep(4)
#nc.floating_ip_pools.list()
#floating_ip = nc.floating_ips.create(nc.floating_ip_pools.list()[0].name)

#server.addresses
#server.add_floating_ip(floating_ip)
server.add_floating_ip("130.238.29.98")
