FROM rocketboy/node-phantomjs

RUN sudo apt-get update && sudo sudo apt-get install python python-pip -yq 

RUN pip install selenium selenium-requests

COPY ./alice.py /home/seluser/

CMD /bin/bash

