import os


root_dir='C:\\Users\\Gabriel\\Desktop\\VotingSimulation'
for currentpath, folders, files in os.walk(root_dir):
    for file in files:
        source = os.path.join(currentpath, file)

        destFolder = root_dir='C:\\Users\\Gabriel\\Desktop\\dest'
        destination = os.path.join(destFolder, source[source.find('VotingSimulation'):])

        #print(source)
        if "__pycache__" not in source and ".py" in source:
             with open(source, "r") as f:
                  lines = f.readlines()

             destFolder = os.path.dirname(destination)
             if not os.path.exists(destFolder):
                  os.makedirs(destFolder)

             with open(destination, 'a') as out:
                 for line in lines:
                      out.write(line)
             print(destination)
        #print()