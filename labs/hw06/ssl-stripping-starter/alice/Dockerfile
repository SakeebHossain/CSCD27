FROM node

RUN apt-get update && apt-get install curl nodejs npm arping -y

RUN mkdir -p /home/nodejs/app
COPY ./index.js /home/nodejs/app/index.js
COPY ./package.json /home/nodejs/app/package.json
WORKDIR /home/nodejs/app
RUN npm install

CMD node index.js