-- PostgreSQL database dump for The world of Star Wars assignment
-- DB name: wosw

ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS pk_users_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.planet_votes DROP CONSTRAINT IF EXISTS pk_planet_votes_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.planet_votes DROP CONSTRAINT IF EXISTS fk_users_id CASCADE;

DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.users_id_seq;
CREATE TABLE users (
    id serial NOT NULL,
    username varchar,
    password varchar
);

DROP TABLE IF EXISTS public.planet_votes;
DROP SEQUENCE IF EXISTS public.planet_votes_id_seq;
CREATE TABLE planet_votes (
    id serial NOT NULL,
    planet_id integer,
    planet_name varchar,
    users_id integer,
    submission_time char(16) default to_char(LOCALTIMESTAMP, 'YYYY-MM-DD HH24:MI')
);

ALTER TABLE ONLY users
    ADD CONSTRAINT pk_users_id PRIMARY KEY (id);

ALTER TABLE ONLY planet_votes
    ADD CONSTRAINT pk_planet_votes_id PRIMARY KEY (id);

ALTER TABLE ONLY planet_votes
    ADD CONSTRAINT fk_users_id FOREIGN KEY (users_id) REFERENCES users(id)
    ON DELETE CASCADE;
