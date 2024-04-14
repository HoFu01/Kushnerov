Task 1
INSERT INTO "actors" (name,surname,age,movie_name,budget,manager,release_year,sex)
VALUES
("Arnold","Schwarzenegger",75,"Terminator",10000000,"James Cameron",1984,"male"),
("Arnold","Schwarzenegger",75,"The 6th Day",14000000,"Roger Spottiswoode",2000,"male"),
("Arnold","Schwarzenegger",75,"End of Days",16000000,"Peter Hyams",1999,"male"),
("Bruce","Willis",67,"Blind Date",9000000,"Blake Edwards",1987,"male"),
("Bruce","Willis",67,"Die Hard 2",15000000,"Renny Harlin",1990,"male"),
("Bruce","Willis",67,"Striking Distance",11000000,"Rowdy Herrington",1993,"male"),
("Brad","Pitt",53,"Happy Together",12000000,"Mel Damski",1989,"male"),
("Brad","Pitt",53,"Ad Astra",17000000,"James Gray",2019,"male"),
("Brad","Pitt",53,"Bullet Train",19000000,"David Leitch",2022,"male"),
("Will","Smith",54,"Bad Boys",24000000,"Adil El Arbi",2024,"male"),
("Will","Smith",54,"Emancipation",26000000,"Antoine Fuqua",2022,"male"),
("Will","Smith",54,"King Richard",28000000,"Reynaldo Marcus Green",2021,"male"),
("Leonardo","DiCaprio",48,"Killers of the Flower Moon",17000000,"Martin Charles Scorsese",2023,"male"),
("Leonardo","DiCaprio",48,"Don’t Look Up",19000000,"Adam McKay",2021,"male"),
("Leonardo","DiCaprio",48,"The Revenant",14000000,"Alejandro González Iñárritu",2015,"male"),
("Tom","Hanks",66,"The Simpsons Movie",21000000,"David Silverman",2007,"male"),
("Tom","Hanks",66,"Mamma Mia!",22000000,"Phyllida Lloyd",2008,"male"),
("Tom","Hanks",66,"City of Ember",26000000,"Gil Keenan",2008,"male"),
("Johnny","Depp",59,"Pirates of the Caribbean: On Stranger Tides",34000000,"Robert Doyle Marshall Jr",2011,"male"),
("Johnny","Depp",59,"Jack & Jilly",31000000,"Dennis Dugan",2011,"male"),
("Johnny","Depp",59,"City of Lies",33000000,"Brad Furman",2018,"male"),
("Harrison","Ford",80,"	Indiana Jones and the Dial of Destiny",27000000,"James Allen Mangold",2023,"male"),
("Harrison","Ford",80,"The Call of the Wild",26000000,"Christopher Michael Sanders ",2020,"male"),
("Harrison","Ford",80,"Star Wars: The Rise of Skywalker",30000000,"JJeffrey Jacob Abrams",2019,"male"),
("Sandra","Bullock",58,"The Blind Side",16000000,"John Lee Hancock, Jr",2009,"female"),
("Sandra","Bullock",58,"Extremely Loud & Incredibly Close",11000000,"Stephen David Daldry",2011,"female"),
("Sandra","Bullock",58,"The Heat",12000000,"Paul Samuel Feig",2013,"female"),
("Halle","Berry",56,"Moonfall",17000000,"Roland Emmerich",2022,"female"),
("Halle","Berry",56,"Bruised",16000000,"Halle Maria Berry",2020,"female"),
("Halle","Berry",56,"John Wick: Chapter 3 — Parabellum",14000000,"Chad Stahelski",2019,"female"),
("Julia","Roberts",55,"Eat, Pray, Love",13000000,"Ryan Patrick Murphy",2010,"female"),
("Julia","Roberts",55,"Wonder",11400000,"Stephen Chbosky",2017,"female"),
("Julia","Roberts",55,"Leave The World Behind",12000000,"Sam Esmail",2013,"female"),
("Kate","Winslet",47,"Wonder Wheel",14000000,"Heywood Woody Allen",2016,"female"),
("Kate","Winslet",47,"The Mountain Between US",18000000,"Hani Abu Assad",2017,"female"),
("Kate","Winslet",47,"Collateral Beauty",25000000,"David Frankel",2017,"female"),
("Angelina","Jolie",47,"Kung Fu Panda 2",26000000,"Jennifer Yu Nels",2011,"female"),
("Angelina","Jolie",47,"The Tourist",23000000,"Florian Maria Georg",2010,"female"),
("Angelina","Jolie",47,"The Good Shepherd",29000000,"Robert Anthony De Niro",2006,"female"),
("Jim","Carrey",59,"Kidding",24000000,"Michel Gondry",2020,"male"),
("Jim","Carrey",59,"The Cable Guy",22000000,"Benjamin Edward Meara",1996,"male"),
("Jim","Carrey",59,"Dumb & Dumber",28000000,"Peter John Farrelly",1994,"male")
;
-- Result: запрос успешно выполнен. Заняло 375мс, 42 строк изменено

Task 2
ALTER TABLE "actors" ADD COLUMN "fee" REAL

Task 3
ALTER TABLE "actors"
RENAME COLUMN "fee" TO "fee actors"
ALTER TABLE "actors" ADD COLUMN "city" TEXT

Task 4
SELECT DISTINCT(name),surname FROM actors
WHERE release_year BETWEEN 1990 AND 2000;

Task 5
SELECT name,count(surname) AS "количество"
FROM actors
GROUP BY surname
HAVING count(surname) >=2
ORDER BY surname DESC;

Task 6
SELECT count(DISTINCT(name)) AS "Количество актеров мужчин старше 55" FROM actors
WHERE age>55 AND sex="male";

Task 7
SELECT name,count(surname) AS "количество"
FROM actors
WHERE fee_actors >= 10000000
GROUP BY surname
HAVING count(surname) >=2;

Task 8
SELECT sum(fee_actors)
FROM actors
WHERE release_year>=1995 and release_year<=2005;

Task 10
SELECT movie_name AS "фильм"
FROM actors
WHERE movie_name like '%%';