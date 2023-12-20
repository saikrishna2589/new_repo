# shutil stands for Shell Utilities
#With Shutil , we can copy files, create zip files,extract files from zip files

import shutil

# the below function 'make_archive' here is creating folder 'output' in zip format(so output.zip) and
# loading the files in the folder 'glob function demo required files' into a zip file .notice 'output.zip' created

shutil.make_archive("ouput","zip",'glob function demo required files')