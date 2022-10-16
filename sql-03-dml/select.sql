-- название и год выхода альбомов, вышедших в 2018 году;

select name_album , year_album
from album a
where year_album = 2018

-- название и продолжительность самого длительного трека;

select name_track, max(duration)
from track t
group by name_track
limit 1

-- название треков, продолжительность которых не менее 3,5 минуты;

select name_track
from track t
where  duration > 60*3.5

-- названия сборников, вышедших в период с 2018 по 2020 год включительно;

SELECT name_mix
from mix
where year_mix >= 2018 and year_mix <=2020


--исполнители, чье имя состоит из 1 слова;

select *
from artist a
where (LENGTH(name_artist) - LENGTH(replace(name_artist, ' ', ''))) < 1


--название треков, которые содержат слово "мой"/"my".

select name_track
from track t
where name_track LIKE '%my%' or  name_track LIKE  '%мой%'