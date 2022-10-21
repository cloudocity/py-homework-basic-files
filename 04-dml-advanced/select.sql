--количество исполнителей в каждом жанре;
select g.name_genre, count(ag.artist_id)
from genre g
join artist_genre ag on ag.artist_id = g.id
group by g.name_genre


--количество треков, вошедших в альбомы 2019-2020 годов;
select count(t.id)
from album a
join track t on t.album_id = a.id
where year_album >= 2019 and year_album <= 2020


--средняя продолжительность треков по каждому альбому;
select a.name_album , sum(t.duration)/count(t.duration)
from album a
join track t on t.album_id = a.id
group by name_album


--все исполнители, которые не выпустили альбомы в 2020 году;

select a.name_artist
from artist a
join artist_album aa on aa.artist_id = a.id
join album a2 on a2.id = aa.album_id
where a.id  != (select a.id from artist a
				join artist_album aa on aa.artist_id = a.id
				join album a2 on a2.id = aa.album_id
				where a2.year_album  = 2020)


--названия сборников, в которых присутствует конкретный исполнитель (выберите сами);

select m.name_mix
from artist a
join artist_album aa on aa.artist_id = a.id
join album a2 on a2.id = aa.album_id
join track t on t.album_id = a2.id
join mix_track mt on mt.track_id = t.id
join mix m on m.id = mt.mix_id
where a.name_artist = 'Pink Floyd'


--название альбомов, в которых присутствуют исполнители более 1 жанра;

select a2.name_album
from artist a
join artist_album aa on aa.artist_id = a.id
join album a2 on aa.album_id = a2.id
join artist_genre ag on ag.artist_id = a.id
group by a.id , a2.name_album
having count(a.id ) >1


--наименование треков, которые не входят в сборники;

select t2.name_track
from track t2
where not exists (select t.id
				from mix_track mt
				join mix m on mt.mix_id = m.id
				join track t on mt.track_id = t.id
				where t.id = t2.id
				group by t.id
				)


--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);

select a.name_artist
from track t
join artist_album aa on aa.album_id = t.album_id
join artist a on a.id = aa.artist_id
where t.duration = ( select min(duration) from track t )


--название альбомов, содержащих наименьшее количество треков.

select a.name_album
from album a
join track t on t.album_id = a.id
group by a.id
having  count(t.id) = (select min(tdi.count)
			from (select count(t.id)
			from album a
			join track t on t.album_id = a.id
			group by a.id) as tdi
)