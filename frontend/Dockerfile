# Step 1: Build Angular app
FROM node:20 AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build --prod

# Step 2: Serve built app with a lightweight server
FROM node:20-slim

WORKDIR /app

RUN npm install -g serve

# Copy only the dist folder (adapt folder name based on your project)
COPY --from=build /app/dist/frontend /app

# Serve on port 8080 (Render uses 8080 by default)
ENV PORT 8080
EXPOSE 8080

CMD ["serve", "-s", ".", "-l", "8080"]
