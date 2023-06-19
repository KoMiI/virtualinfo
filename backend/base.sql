create user virtualinfo login password 'vi9966834';

CREATE SCHEMA IF NOT EXISTS AUTHORIZATION virtualinfo;

ALTER DATABASE SET search_path = virtualinfo;

CREATE TABLE keys (
    id serial PRIMARY KEY,
    name text NOT NULL,
    key text,
    pub_key text
);

CREATE TABLE scripts (
    id serial PRIMARY KEY,
    name text not null,
    script text,
    created timestamp default now(),
    user_login text
);

CREATE TABLE servers (
    id serial PRIMARY KEY,
    name text NOT NULL,
    host text NOT NULL,
    port integer NOT NULL,
    user_login text,
    key_id integer NOT NULL REFERENCES keys (id),
    script_id integer NOT NULL REFERENCES scripts (id)
);

CREATE TABLE vm_reserve (
    id serial PRIMARY KEY,
    server_id integer NOT NULL REFERENCES servers (id) ON DELETE CASCADE,
    vm_name text not null,
    user_login text,
    until_date timestamp
);

CREATE INDEX ON vm_reserve (server_id, vm_name);
