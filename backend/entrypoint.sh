#!/bin/bash

echo "🔧 Waiting for PostgreSQL to be ready..."

# Boucle jusqu’à ce que la base réponde (utilise pg_isready)
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
    >&2 echo "PostgreSQL is unavailable - sleeping"
    sleep 2
done

echo "✅ PostgreSQL is ready."

# Lancer l'app Flask
exec python app.py
