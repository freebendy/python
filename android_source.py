import httplib # for http request
from lib.BeautifulSoup import BeautifulSoup # for html parse
import os # for file operation
import sys
import re # 
import string

prefixurl = "https://android.git.kernel.org/" # "git://android.git.kernel.org/" is so easy to lead to time out
currentdir = os.path.abspath(os.path.dirname(sys.argv[0])) #the dir of the source
repositorydir = ".git"
os.chdir(currentdir) # change the work directory, getcwd()

conn = httplib.HTTPConnection("android.git.kernel.org")
conn.request("GET","/")
res = conn.getresponse()

if res.status == httplib.OK:
    data = res.read();
    #print data
    conn.close()
    
    soup = BeautifulSoup(data)
    #print soup.prettify()
    table = soup.body.table
    #print soup.body.table
    # filter
    tags = table.findAll('a', attrs = {'class' : 'list', 'title': None , 'href' : re.compile('^/\?p')})
    #print tags
    projectlist = []
    for tag in tags:
        projectlist.append(tag.string) 
        
    file = open(currentdir+"/list.txt","w")
    #writelines won't add the '\n'
    file.writelines( map( lambda x: x.strip()+"\n", projectlist ) );
    file.close()
        
    for i in projectlist:
        #list = string.split(i, "/")
        #print list
        index = string.rfind(i, "/")
        if index != -1:
            projectdir = i[0:index]
            dir2create = currentdir + "/" + projectdir
            
            if os.path.exists(dir2create) != True:
                #print "makedirs : ", dir2create
                os.makedirs(dir2create)
                
            os.chdir(dir2create)
            command = "git clone " + prefixurl + i
            
            if os.path.exists(os.getcwd()+ "/" + i[index:-4] + "/" + repositorydir):
                os.chdir(os.getcwd() + "/" + i[index:-4])
                command = "git pull"
            
            print "In working directory: ", os.getcwd(), "run command:", command
            os.system( command)
        
else:
    print res.status,res.reason

