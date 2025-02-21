
# read version of file 
def read_version():
    try:
     return open("myfile").readline().rstrip()
    except:
       return "1.0.0"
    
def update_minor_version(version_str):
   splitted = version_str.split('.')
   major = splitted[0]
   minor = splitted[0]
   patch = splitted[0]