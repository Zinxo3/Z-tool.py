<img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>
img src="https://img.shields.io/badge/Author-KasRoudra-purple?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-cyan?style=flat-square">
  <img src="https://img.shields.io/badge/Made%20in-Bangladesh-green?  







# Z-tool.py
Its a tool thats created by zino
its not be used for iligale stuff



THIS IS THE TOOL

         _____               __________  ____  __ 
        /__  /              /_  __/ __ \/ __ \/ / 
          / /     ______     / / / / / / / / / /  
         / /__   /_____/    / / / /_/ / /_/ / /___
        /____/             /_/  \____/\____/_____/



# picture
![image](https://github.com/Zinxo3/Z-tool.py/assets/151643629/082f8e7d-1f34-4479-a8b0-03fde567af6f)



 

# Main package
FROM python:3

# Author info
LABEL MAINTAINER="soon"

# Working directory
WORKDIR /Z-Tool/
# Add files 
ADD . /Z-Tool

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-pip php openssh-client -y
RUN pip3 install -r files/requirements.txt --break-system-packages
RUN apt-get clean

# Main command
CMD ["python3", "z-tool.py", "--noupdate"]
