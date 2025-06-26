FROM node:alpine

RUN apk add curl

WORKDIR /apps/frontend

COPY ./apps/frontend .

RUN npm install

CMD [ "npm", "run", "deploy" ]