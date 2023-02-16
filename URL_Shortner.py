# import the package 
import pyshorteners as sh


# add link
link = input('Paste the link here: ')

s = sh.Shortener()

# tinyurl is one of the url shortner Application Programming Interface (API).
# others are:-
# Adf.ly, Bit.ly, Chilp.it, Clck.ru, Cutt.ly, Da.gd, Git.io, Is.gd, 
# NullPointer, Os.db, Ow.ly, Po.st, Qps.ru, Short.cm, Tiny.cc, TinyURL.com, Git.io, Tiny.cc

# print(s.tinyurl.short(link))

# git.io only supports Github URLs
print(s.gitio.short(link))

# expand will show the orignal link of the short URLs
# print(s.gitio.expand(link))