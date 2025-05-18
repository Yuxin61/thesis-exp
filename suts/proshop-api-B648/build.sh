python -m pip install --upgrade pip
pip install -r requirements.txt
# psql "sslmode=verify-full sslrootcert=prod-supabase.cer host=db.osflhbeqqhwozmwzbtbs.supabase.co dbname=postgres user=postgres"
# psql postgres://postgres:Ycvy57MvnaDq6rOg@db.osflhbeqqhwozmwzbtbs.supabase.co:6543/postgres
psql postgres://postgres:12345678@localhost:5432/proshop
