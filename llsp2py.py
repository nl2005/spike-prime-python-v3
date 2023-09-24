'''
 this python file converts spike prime/mind strom python project files into actual python file
 for the purpose of code diff. It does not convert word block project to python. 
 Just put the file in the root folder of all spike prime python project and run python. 
 
 https://github.com/nl2005/spike-prime-python-v3/
 
'''


import os, sys, zipfile

rootdir = '.' if len(sys.argv) < 2 else sys.argv[1]

for root, dirs, files in os.walk(rootdir, topdown=False):
    for name in files:
        if (name.endswith('.llsp3') or  name.endswith('.llsp') or name.endswith('.lms')):
            filename = os.path.join(root, name)
            print(filename)
            with zipfile.ZipFile(filename, 'r') as sp:
                if sp.namelist().__contains__("projectbody.json"):
                    data = str(sp.read("projectbody.json"))
                    # 11: b'{"main"  -3: "}'
                    data = data[11:-3].replace("\\\\n","\n").replace('\\\\"','"').replace("\\'","'")
                    outname = filename.replace('.llsp3','.py').replace('.llsp','.v2.py').replace('.lms','.ms.py')
                    with open(outname, 'w') as py:
                        py.write(data)
                
      
   