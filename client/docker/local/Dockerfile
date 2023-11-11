ARG NODE_VERSION=18-alpine

FROM node:${NODE_VERSION} as node

FROM node as client-local-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./package*.json .
RUN npm ci
COPY . .
RUN npm run build



# COPY . ${APP_HOME}
# FROM node:${NODE_VERSION} as runner
# COPY --from=node /app/package*.json ./
# COPY --from=node /app/.next ./.next
# COPY --from=node /app/public ./public
# COPY --from=node /app/node_modules ./node_modules
EXPOSE 3000
CMD ["npm", "run", "dev"]