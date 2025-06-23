#!/bin/bash

echo "🔧 Waiting for MySQL to be ready..."

# Tentatives de connexion à MySQL (change user/password/db/host selon besoin)
export MYSQL_PWD="$DB_PASSWORD"
until mysqladmin ping -h"$DB_HOST" -u"$DB_USER" --silent; do
    sleep 2
done

echo "✅ MySQL is ready."

# Lancer l'app Flask
exec python app.py
