FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances système pour psycopg2 et pg_isready
RUN apt-get update && \
    apt-get install -y gcc libpq-dev postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Donner les droits d’exécution à l’entrypoint
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
