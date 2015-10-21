{
 "metadata": {
  "name": ""
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "import os\n",
      "import swiftclient.client"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 1
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "config = {'user':os.environ['OS_USERNAME'], \n",
      "          'key':os.environ['OS_PASSWORD'],\n",
      "          'tenant_name':os.environ['OS_TENANT_NAME'],\n",
      "          'authurl':os.environ['OS_AUTH_URL']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "config = {'username':os.environ['OS_USERNAME'], \n",
      "          'api_key':os.environ['OS_PASSWORD'],\n",
      "          'project_id':os.environ['OS_TENANT_NAME'],\n",
      "          'auth_url':os.environ['OS_AUTH_URL'],\n",
      "           }\n",
      "from novaclient.client import Client\n",
      "nc = Client('2',**config)\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 2
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "import time\n",
      "import paramiko\n",
      "image = nc.images.find(name = \"Ubuntu Server 14.04 LTS (Trusty Tahr)\")\n",
      "flavor = nc.flavors.find(name = \"m1.medium\")\n",
      "keypair = nc.keypairs.find(name = \"sarokey_very_secure\")\n",
      "network = nc.networks.find(label = \"ACC-Course-net\")\n",
      "\n",
      "\n",
      "server = nc.servers.create(name = \"SaroMasterAssignment3\",\n",
      "                           image = image.id,\n",
      "                           flavor = flavor.id,\n",
      "                           network = network.id,\n",
      "                           key_name = keypair.name,\n",
      "                           userdata = open('/home/sam/Desktop/Assignment 2/user_data_file.sh'))\n",
      "\n",
      "time.sleep(4)\n",
      "#nc.floating_ip_pools.list()\n",
      "#floating_ip = nc.floating_ips.create(nc.floating_ip_pools.list()[0].name)\n",
      "\n",
      "#server.addresses\n",
      "#server.add_floating_ip(floating_ip)\n",
      "server.add_floating_ip(\"130.238.29.31\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 4
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}