import sys,os,urllib
#example_prefix = 'http://www.itu.edu.tr/tasarim/js/random/kapak/kapak-'
prefix = 'your http://blabla/folderpath/qwerty goes here'
for i in range(1,40):
    if i < 10:
        file_name = '%0*d' % (2, i)
    else:
        file_name = '%d' % i
    file_name = file_name + '.jpg'
    try:
        f = open(file_name,'wb')
        f.write(urllib.urlopen(prefix+file_name).read())
        f.close()        
    except :
        print "Unexpected error:", sys.exc_info()[0]
