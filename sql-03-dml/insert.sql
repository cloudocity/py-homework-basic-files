INSERT INTO artist (name_artist) values
('Pink Floyd'),
('AC/DC'),
('Backstreet Boys'),
('The Beatles'),
('Maddona'),
('Led Zeppelin'),
('Metallica'),
('Nirvana'),
('Bon Jovi'),
('Magnum')
;

INSERT INTO Genre (name_genre) values
('Pop'),
('Hip hop'),
('Heavy metal'),
('Indie pop'),
('Rock')
;

INSERT INTO Album (name_album, year_album) values
('The Dark Side of the Moon', 2018),
('Back in Black', 2019),
('Backstreet Boys', 2020),
('Music Box', 2019),
('ABBA Gold: Greatest Hits', 2018),
('Slippery When Wet', 2018),
('True Blue', 2017),
('Black & Blue', 2021),
('Hybrid Theory', 2022)
;

INSERT INTO Track (name_track, duration, album_id) values
('Intro', 150 , 1),
('my Travel', 250 , 1),
('Money', 140 , 1),
('Hells Bells', 350 , 2),
('Back in Black', 420 , 2),
('Everybody ', 150 , 3),
('All I Have to Give my', 450 , 3),
('Music my', 250 , 4),
('Amazing', 280 , 4),
('Dancing Queen', 350 , 5),
('Mamma Mia', 450 ,5),
('Money, Money, Money', 550 , 5),
('Does Your Mother Know', 150 , 5),
('The Name of the Game', 150 , 5),
('Thank You for the Music', 650 , 5)
;

INSERT INTO mix (name_mix, year_mix) values
('Top 100', 2018),
('Hot Track', 2019),
('Top 10', 2020),
('Summer 2019', 2019),
('Gold Stars', 2018),
('Platimun', 2018),
('Rock', 2017),
('Pop Top', 2021)
;

INSERT INTO artist_album (artist_id,album_id) VALUES
	 (1,1),
	 (2,2),
	 (3,3),
	 (5,4),
	 (8,7),
	 (9,9);

INSERT INTO artist_genre (artist_id,genre_id) VALUES
	 (1,3),
	 (2,5),
	 (3,1),
	 (4,1),
	 (5,1),
	 (8,5),
	 (9,5);

INSERT INTO mix_track (mix_id,track_id) VALUES
	 (1,1),
	 (1,2),
	 (1,8),
	 (2,3),
	 (2,1),
	 (5,5),
	 (3,11),
	 (3,7),
	 (3,12),
	 (4,15),
	 (8,12),
	 (6,6),
	 (4,4),
	 (5,8),
	 (7,11),
	 (8,5),
	 (8,8);