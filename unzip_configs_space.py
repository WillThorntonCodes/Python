#Script to unzip configuration files backed up from Juniper Space
#Files are sent over from Juniper Space via SCP job to the Linux box in gzip(gz) format
#Script will read all files in the target directory and unzip to temp directory
#Next update: 
#Copy files from temp folder to main repository on Windows server
#Basic logging

#Begin--
from os import listdir
import datetime
import gzip
import shutil
configs = listdir("configs/")
for config in configs:
    with gzip.open("configs/"+config,"rb") as gzip_ref:
        with open("tempdir/"+(config).replace(".gz",''), "wb") as gzip_out:
            shutil.copyfileobj(gzip_ref, gzip_out)
#End--
