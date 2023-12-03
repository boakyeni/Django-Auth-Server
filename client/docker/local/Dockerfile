ARG NODE_VERSION=18-alpine

FROM node:${NODE_VERSION} as node

FROM node as client-local-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./package*.json .
RUN npm ci
COPY . .
RUN npm run build


EXPOSE 3000
CMD ["npm", "run", "dev"]