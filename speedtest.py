#!/usr/bin/python
import os
import sys
from twython import Twython

#Twitter Authentication
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def test():

        #run speedtest-cli
        print 'running speedtest'
        a = os.popen("speedtest-cli --simple --no-pre-allocate").read()
        print 'finished'
		
        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print a
		
        #If there is no connection -> values = 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
				
        #Extract the values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]

        #Tweet: Slow Internet
        if "Cannot" in a:
                try:
                        message="Hey @provider! Why is my Internet down?"
                        twitter.update_status(status=message)
                except:
                        pass

        #Tweet: Internetspeed To Slow
        elif eval(d)<28:
                print "sending tweet..."
                try:
                        message="Hey @provider why is my internetspeed " + str(int(eval(d))) + " MBit/s down & " + str(int(eval(u))) + " MBit/s up? I'm paying for 50 down & 10 up!"
                        twitter.update_status(status=message)
                except Exception,e:
                        print str(e)
                        pass
        return
		
        
if __name__ == '__main__':
        test()
        print 'completed'
