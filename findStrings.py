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
      "import swiftclient.client\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 3
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
     "outputs": [],
     "prompt_number": 4
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "conn = swiftclient.client.Connection(auth_version=2, **config)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 5
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "object_id = conn.get_object(\"tweets\",\"tweets_0.txt\")"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stderr",
       "text": [
        "ERROR:swiftclient:Authorization Failure. Authorization Failed: Unable to establish connection to http://smog.uppmax.uu.se:5000/v2.0/tokens\n",
        "Traceback (most recent call last):\n",
        "  File \"/usr/local/lib/python2.7/dist-packages/swiftclient/client.py\", line 1378, in _retry\n",
        "    self.url, self.token = self.get_auth()\n",
        "  File \"/usr/local/lib/python2.7/dist-packages/swiftclient/client.py\", line 1332, in get_auth\n",
        "    timeout=self.timeout)\n",
        "  File \"/usr/local/lib/python2.7/dist-packages/swiftclient/client.py\", line 463, in get_auth\n",
        "    auth_version=auth_version)\n",
        "  File \"/usr/local/lib/python2.7/dist-packages/swiftclient/client.py\", line 391, in get_auth_keystone\n",
        "    raise ClientException('Authorization Failure. %s' % err)\n",
        "ClientException: Authorization Failure. Authorization Failed: Unable to establish connection to http://smog.uppmax.uu.se:5000/v2.0/tokens\n"
       ]
      },
      {
       "ename": "ClientException",
       "evalue": "Authorization Failure. Authorization Failed: Unable to establish connection to http://smog.uppmax.uu.se:5000/v2.0/tokens",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mClientException\u001b[0m                           Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-4-8f54f66a3c39>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mobject_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_object\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"tweets\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"tweets_0.txt\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;32m/usr/local/lib/python2.7/dist-packages/swiftclient/client.pyc\u001b[0m in \u001b[0;36mget_object\u001b[0;34m(self, container, obj, resp_chunk_size, query_string, response_dict, headers)\u001b[0m\n\u001b[1;32m   1486\u001b[0m                            \u001b[0mresp_chunk_size\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mresp_chunk_size\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1487\u001b[0m                            \u001b[0mquery_string\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mquery_string\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1488\u001b[0;31m                            response_dict=response_dict, headers=headers)\n\u001b[0m\u001b[1;32m   1489\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1490\u001b[0m     def put_object(self, container, obj, contents, content_length=None,\n",
        "\u001b[0;32m/usr/local/lib/python2.7/dist-packages/swiftclient/client.pyc\u001b[0m in \u001b[0;36m_retry\u001b[0;34m(self, reset_func, func, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1376\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1377\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murl\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtoken\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1378\u001b[0;31m                     \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtoken\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_auth\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1379\u001b[0m                     \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhttp_conn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1380\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice_auth\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice_token\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
        "\u001b[0;32m/usr/local/lib/python2.7/dist-packages/swiftclient/client.pyc\u001b[0m in \u001b[0;36mget_auth\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1330\u001b[0m                                         \u001b[0mcacert\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcacert\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1331\u001b[0m                                         \u001b[0minsecure\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minsecure\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1332\u001b[0;31m                                         timeout=self.timeout)\n\u001b[0m\u001b[1;32m   1333\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtoken\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1334\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
        "\u001b[0;32m/usr/local/lib/python2.7/dist-packages/swiftclient/client.pyc\u001b[0m in \u001b[0;36mget_auth\u001b[0;34m(auth_url, user, key, **kwargs)\u001b[0m\n\u001b[1;32m    461\u001b[0m                                                \u001b[0minsecure\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0minsecure\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    462\u001b[0m                                                \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 463\u001b[0;31m                                                auth_version=auth_version)\n\u001b[0m\u001b[1;32m    464\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    465\u001b[0m         raise ClientException('Unknown auth_version %s specified.'\n",
        "\u001b[0;32m/usr/local/lib/python2.7/dist-packages/swiftclient/client.pyc\u001b[0m in \u001b[0;36mget_auth_keystone\u001b[0;34m(auth_url, user, key, os_options, **kwargs)\u001b[0m\n\u001b[1;32m    389\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0mClientException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    390\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mexceptions\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mAuthorizationFailure\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 391\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mClientException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Authorization Failure. %s'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    392\u001b[0m     \u001b[0mservice_type\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mos_options\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'service_type'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;34m'object-store'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    393\u001b[0m     \u001b[0mendpoint_type\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mos_options\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'endpoint_type'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;34m'publicURL'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
        "\u001b[0;31mClientException\u001b[0m: Authorization Failure. Authorization Failed: Unable to establish connection to http://smog.uppmax.uu.se:5000/v2.0/tokens"
       ]
      }
     ],
     "prompt_number": 4
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "\n",
      "import sys\n",
      "import json\n",
      "\n",
      "def pronounCount(tweetfile):\n",
      "    triggerWords = {\"han\" : 0, \"hon\" : 0, \"den\" : 0,\n",
      "                    \"denna\" : 0, \"denne\" : 0, \"hen\" : 0}\n",
      "    key = triggerWords.keys()\n",
      "    \n",
      "    with open('tweets_19.txt.part',\"r\") as f:                     #read the file// make this generic for all files\n",
      "        jsonDataLines = f.readlines()                             #read all the lines in file f\n",
      "        for data in jsonDataLines:                                #for every line in all the lines\n",
      "            if data != '\\n':                                      #disregard empty lines\n",
      "                json_data = json.loads(data)                      #load data as json\n",
      "                text = json_data[\"text\"].split()                  #save word for word in text-list\n",
      "                for words in text:                                #\n",
      "                    if words.lower() in key:                      #for every word which corresponds to a key\n",
      "                        triggerWords[words.lower()] += 1          # add 1 to that value\n",
      "                        \n",
      "                \n",
      "    print triggerWords                                            #the result\n",
      "    \n",
      "    \n",
      "\n",
      "\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "{'han': 14306, 'hon': 7187, 'denne': 56, 'den': 28258, 'denna': 524, 'hen': 884}\n"
       ]
      }
     ],
     "prompt_number": 1
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 1
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