import httplib # for http request
from lib.BeautifulSoup import BeautifulSoup # for html parse
import os # for file operation
import sys
import re # 
import string

prefixurl = "http://android.git.kernel.org/" # "git://android.git.kernel.org/" is so easy to lead to time out
currentdir = os.path.abspath(os.path.dirname(sys.argv[0])) #the dir of the source
listfilename = "projectlist.txt"
repositorydir = ".git"
os.chdir(currentdir) # change the work directory, getcwd()

# get the list of the projects from "android.git.kernel.org"
def updateprojectlist():
    print "updating the projects list"
    conn = httplib.HTTPConnection("android.git.kernel.org")
    conn.request("GET","/")
    res = conn.getresponse()
    
    if res.status == httplib.OK:
        data = res.read();
        #print data
        conn.close()
        
        soup = BeautifulSoup(data)
        table = soup.body.table
        #print soup.body.table
        
        # filter
        tags = table.findAll('a', attrs = {'class' : 'list', 'title': None , 'href' : re.compile('^/\?p')})
        #print tags
        
        projectlist = []
        for tag in tags:
            projectlist.append(tag.string) 
            
        file = open(currentdir+"/"+listfilename,"w")
        #writelines won't add the '\n'
        file.writelines( map( lambda x: x.strip()+"\n", projectlist ) );
        file.close()

    else:
        print "fail to download the page: ",res.status,res.reason
        

# clone the project if not checked out, update the project if checked out, repository All-Projects.git will fail.    
def smart():
    if (os.path.exists(currentdir+"/"+listfilename)):
        print "cloning all projects"
        file = open(currentdir+"/"+listfilename,"r")
        projectlist = file.readlines()
        
        for i in projectlist:
            #print projectlist
            # the source code checkout by repo ignored the platform folder, so we do the same here.
            destDir = string.replace(i,"platform/","")
            
            index = string.rfind(destDir, "/")
            if index != -1:
                projectdir = destDir[0:index]
                dir2create = currentdir + "/" + projectdir
            
                if os.path.exists(dir2create) != True:
                    #print "makedirs : ", dir2create
                    os.makedirs(dir2create)
                
                os.chdir(dir2create)
                
            else:
                os.chdir(currentdir)
                  
            command = "git clone " + prefixurl + i
            
            if os.path.exists(os.getcwd()+ "/" + destDir[index:-4] + "/" + repositorydir):
                os.chdir(os.getcwd() + "/" + destDir[index:-4])
                command = "git pull"
                
            print "In working directory: ", os.getcwd(), "run command:", command
            os.system( command )
    else:
        print listfilename," is not found, make sure you are in correct working directory! or update the projects list first."
       
# clone all the projects, repository All-Projects.git will fail.    
def cloneall():
    if (os.path.exists(currentdir+"/"+listfilename)):
        print "cloning all projects"
        file = open(currentdir+"/"+listfilename,"r")
        projectlist = file.readlines()
        
        for i in projectlist:
            #print projectlist
            # the source code checkout by repo ignored the platform folder, so we do the same here.
            destDir = string.replace(i,"platform/","")
            
            index = string.rfind(destDir, "/")
            if index != -1:
                projectdir = destDir[0:index]
                dir2create = currentdir + "/" + projectdir
            
                if os.path.exists(dir2create) != True:
                    #print "makedirs : ", dir2create
                    os.makedirs(dir2create)
                
                os.chdir(dir2create)
                
            else:
                os.chdir(currentdir)
                
            command = "git clone " + prefixurl + i
            print "In working directory: ", os.getcwd(), "run command:", command
            os.system( command )
    else:
        print listfilename," is not found, make sure you are in correct working directory! or update the projects list first."
        
def updateall():
    if (os.path.exists(currentdir+"/"+listfilename)):
        print "update all projects"
        file = open(currentdir+"/"+listfilename,"r")
        projectlist = file.readlines()
        
        for i in projectlist:
            #print projectlist
            
            # the source code checkout by repo ignored the platform folder, so we do the same here.
            i = string.replace(i,"platform/","")
                
            index = string.rfind(i, ".git")
            if index != -1:
                projectdir = i[0:index]
                dir2update = currentdir + "/" + projectdir
            
                if os.path.exists(dir2update):  
                    os.chdir(dir2update)
            else:
                os.chdir(currentdir)
                
            command = "git pull"
            print "In working directory: ", os.getcwd(), "run command:", command
            os.system( command )
    else:
        print listfilename," is not found, make sure you are in correct working directory! or update the projects list first and clone all projects."
        
    
def main():
    option = raw_input("Slect an option(Any other keys to exit):\n\t1.update the projects list\n\t2.clone all projects\n\t3.update all projects\n\t4.smart\nYour selection is: ")
    if option == '1':
        updateprojectlist()
    elif option == '2':
        cloneall()
    elif option == '3':
        updateall()
    elif option == '4':
        smart()
    else:
        return;
    
    
if __name__=='__main__':
    main()



