CREATE TABLE Genre (
	id SERIAL PRIMARY key,
	name_genre varchar NOT NULL
);

CREATE TABLE Artist (
	id SERIAL PRIMARY key,
	name_artist varchar NOT null
);

CREATE TABLE Artist_Genre (
	artist_id int references Artist (id),
	genre_id int references Genre (id),
	constraint pk primary key (artist_id, genre_id)
);

CREATE TABLE Album (
	id SERIAL PRIMARY key,
	name_album varchar NOT null,
	year_album int
);

CREATE TABLE Artist_Album (
	artist_id int references Artist (id),
	album_id int references Album (id),
	constraint pki primary key (artist_id, album_id)
);

CREATE TABLE Track (
	id SERIAL PRIMARY key,
	name_track varchar NOT null,
	duration int,
	album_id int references Album (id)
);

CREATE TABLE Mix (
	id SERIAL PRIMARY key,
	name_mix varchar NOT null,
	year_mix int
);

CREATE TABLE Mix_Track(
	mix_id int references Mix (id),
	track_id int references Track (id),
	constraint pku primary key (mix_id, track_id)
);