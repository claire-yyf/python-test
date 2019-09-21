FROM alpine

WORKDIR /usr/src/app

RUN apk update
RUN apk add --no-cache python3
RUN pip3 install --upgrade pip
RUN apk add --no-cache nodejs
RUN apk add --no-cache npm
RUN npm i -g nodemon

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["nodemon"]
