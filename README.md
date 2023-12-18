<img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>





# Z-tool.py
Its a tool thats created by zino
its not be used for iligale stuff






# picture
![image](https://github.com/Zinxo3/Z-tool.py/assets/151643629/082f8e7d-1f34-4479-a8b0-03fde567af6f)



 


/FROM python:3


/LABEL MAINTAINER="soon"


/WORKDIR /Z-Tool/

/ADD . /Z-Tool


/RUN apt-get update
/RUN apt-get upgrade -y
/RUN apt-get install python3-pip php openssh-client -y
/RUN pip3 install -r files/requirements.txt --break-system-packages
/RUN apt-get clean

/CMD ["python3", "z-tool.py", "--noupdate"]
