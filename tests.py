import os
import glob
import subprocess
import sys

blenderExecutable = 'blender'

# Accept Blender Executable as command line argument
if len(sys.argv) > 1:
    blenderExecutable = sys.argv[1]

# iterate over each *.test.blend file in the "tests" directory
# and open up blender with the .test.blend file and the corresponding .test.py python script
for f in glob.glob('./tests/**/*.test.blend'):
    test_file = f.replace('.blend', '.py')
    print(f)
    print(test_file)
    subprocess.call([blenderExecutable, '--factory-startup', '-noaudio', '-b', f, '--python', test_file])
