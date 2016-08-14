CREATE TABLE workouts (
    id bigserial primary key,
    title varchar(20) NOT NULL,
    date date default NULL,
    workout json NOT NULL
);
