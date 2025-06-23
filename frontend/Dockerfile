FROM node:20

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

# Angular needs the CLI to serve
RUN npm install -g @angular/cli

CMD ["ng", "serve", "--host", "0.0.0.0"]
