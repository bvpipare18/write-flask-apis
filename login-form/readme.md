1. docker run --name postgres-container -p 5433:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres:9.5

2. docker exec -it postgres-container psql -U postgres

3. CREATE DATABASE login_database;

4. CREATE USER user1 WITH PASSWORD 'password1';

5. GRANT ALL PRIVILEGES ON DATABASE login_database TO user1;

6. \c login_database;

7. CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

8. GRANT ALL PRIVILEGES ON TABLE users TO user1;

9. GRANT USAGE, SELECT ON SEQUENCE users_id_seq TO user1;

10. SELECT * FROM users;






CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);