FROM node

RUN apt-get update && apt-get install nodejs npm -y

RUN mkdir -p /home/nodejs/app
COPY ./start.sh /home/nodejs/app/start.sh
COPY ./index.js /home/nodejs/app/index.js
COPY ./package.json /home/nodejs/app/package.json
WORKDIR /home/nodejs/app
RUN npm install

CMD ./start.sh