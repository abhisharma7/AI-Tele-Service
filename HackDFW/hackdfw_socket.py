#!/usr/bin/python


import socket
import os
import sys
import httplib, urllib, base64
import json
import itertools
import subprocess as sp

def server_(HOST,PORT):
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind((HOST,PORT))
		s.listen(5)
		while True:	
			print "Listening at", s.getsockname()
			sc, sockname = s.accept()

			print "\n\nClient Request Received:"
			print "Accepted Connection from:", sockname
			print "Socket Connects", sc.getsockname(), 'and', sc.getpeername()		
			#(sc,MAX_SIZE)
			#request_receive =  
			receive = sc.recv(MAX_SIZE)
			(url,phone_number) = receive.split(',')
			statement = Azure_api_vision(url)
			#print statement
			#statement2 = Azure_api_Emotion(url)
			#print statement2
			if "person" not in statement:
				statement3 = Azure_api_ocr(url)
				statement = statement + " This is the additional information which we able to fetch " + statement3
			status = cisco_tropo(statement, phone_number)
			print status
			sc.close()
			print "Connection Closed!!!\n"		
			
def Azure_api_vision(url):
	
	subscription_key='776d661a6f474be38d611cca2ad6db32'
       	headers = {
      		'Content-Type': 'application/json',
        	'Ocp-Apim-Subscription-Key': subscription_key,
                }

    	params = urllib.urlencode({
        	# Request parameters
       		'visualFeatures': 'Categories',
     	})
       	body = '{\'URL\' :' + '\'' + url + '\'}'

    	try:

     		conn = httplib.HTTPSConnection('api.projectoxford.ai')
          	conn.request("POST", "/vision/v1/analyses?%s" % params, body, headers)
        	response = conn.getresponse()
        	data = response.read()
           	d = json.loads(data)
           	list_ = d['categories'][0]
           	description = list_['name']
		description_final = description.replace("_"," ")
             	statement = "Hi, we are calling from cisco... This call is regarding the picture you just clicked... its about " + description_final
          	conn.close()
		return statement
   	except Exception as e:
        	print e

def Azure_api_ocr(url):

	subscription_key='776d661a6f474be38d611cca2ad6db32'	
	headers = {
        	#subscription_key='776d661a6f474be38d611cca2ad6db32'
           	# Request headers
        	'Content-Type': 'application/json',
             	'Ocp-Apim-Subscription-Key': subscription_key,
      	}

	params = urllib.urlencode({
        	# Request parameters
               	#'visualFeatures': 'All',
       		'language' : 'en',
                })
   	#body = '{\'URL\': \'https://jurnsearch.files.wordpress.com/2009/07/ocr-test.jpg\'}'
    	body = '{\'URL\' :' + '\'' + url + '\'}'
     	#body = { "Url" : url }

      	try:
		os.system("rm -f ~/ocr_sample")
		os.system("rm -f ~/ocr_result")
		conn = httplib.HTTPSConnection('api.projectoxford.ai')
            	#conn.request("POST", "/vision/v1/analyses?%s", %params, body, headers)
           	conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
           	response = conn.getresponse()
            	#print response
           	data = response.read()
              	#d = json.loads(data)
		#print d
		file_reader = open('ocr_sample','wb')
		file_reader.write(data)
		file_reader.close()
		os.system("bash ~/ocr_execute")
		
               	execute = sp.Popen(["cat ~/ocr_result1"],stdout=sp.PIPE, shell=True)
                (output, err) = execute.communicate()
		conn.close()
		return output


   	except Exception as e:
         	print e
       		#print("[Errno {0}] {1}".format(e.errno, e.strerror))


def Azure_api_Emotion(url):
	
        subscription_key='f500e6bbce1c4067aa9642d65fd90677'
        headers = {
                'Content-Type': 'application/json',
                'Ocp-Apim-Subscription-Key': subscription_key,
                }

        params = urllib.urlencode({
                # Request parameters
        })
        body = '{\'URL\' :' + '\'' + url + '\'}'

        try:

                conn = httplib.HTTPSConnection('api.projectoxford.ai')
                conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
                response = conn.getresponse()
                data = response.read()
                d = json.loads(data)
		print d
		#[{u'faceRectangle': {u'width': 699, u'top': 1239, u'left': 589, u'height': 699}, u'scores': {u'sadness': 1.40004314e-13, u'neutral': 3.87832023e-11, u'contempt': 1.26417887e-11, u'disgust': 3.1012198e-12, u'anger': 4.81995e-11, u'surprise': 3.347419e-10, u'fear': 3.63359733e-13, u'happiness': 1.0}}]
		
		#score_list = d[1]
		#pr
                conn.close()
                return "Done2"
        except Exception as e:
                print e
	

def cisco_tropo(statement, number):

	urllib.urlopen("https://api.tropo.com/1.0/sessions?action=create&token=4371527245684855627a78696d7a504970655059655143624453454367417078494f46556c70775456694943&number_to_dial=" + number + "&text_msg=" + statement)
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '0.0.0.0'
PORT = 7000
MAX_SIZE = 65535
server_(HOST,PORT)
