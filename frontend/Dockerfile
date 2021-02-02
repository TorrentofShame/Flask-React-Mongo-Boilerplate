FROM node:latest as build
LABEL maintainer="simon@torrentofshame.com"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package*.json /usr/src/app

RUN npm ci

COPY . /usr/src/app
RUN npm build

FROM nginx:alpine
COPY --from=dist /usr/src/app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
