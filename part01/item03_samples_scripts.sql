-- ######################  Operations for a basic CRUD  ############################

-- SELECT ALL DATA
SELECT * FROM todo;

-- INSERT THE FIRST DATA
INSERT INTO todo
    (title, description, is_completed)    
    values( 'First todo', 'Do a lot of very important things', 0 );


INSERT INTO todo
    (title, description, is_completed)
    values('Second', 'llevar a chanchito feliz al doctor, duele panza', 0);


-- Generate data FROM
-- https://www.generatedata.com/

-- INSERT 100 RECORDS
INSERT INTO todo (title,description,is_completed) VALUES ("Nibh Aliquam Ornare Company","purus mauris a",0),("Dis Parturient Montes Limited","posuere cubilia",1),("Metus Urna Convallis Inc.","diam luctus lobortis. Class aptent taciti sociosqu",1),("Volutpat Nulla Dignissim Industries","est, vitae sodales nisi magna sed dui. Fusce aliquam, enim",1),("Integer Eu Lacus Inc.","parturient montes, nascetur ridiculus mus. Donec dignissim magna",0),("Augue Industries","nonummy ipsum non arcu. Vivamus sit amet risus. Donec egestas.",0),("In At Foundation","consectetuer rhoncus. Nullam velit dui, semper et,",1),("Ad Ltd","a felis ullamcorper viverra. Maecenas iaculis aliquet",0),("Consectetuer Adipiscing Elit Institute","rhoncus id, mollis nec, cursus a, enim. Suspendisse aliquet, sem",1),("Praesent Eu Dui Institute","suscipit",1),("Aenean Egestas Hendrerit Ltd","aliquet, metus urna convallis erat, eget",1),("Augue Limited","consectetuer adipiscing",1),("Imperdiet Ornare Corporation","sociis natoque penatibus et magnis dis parturient",1),("Egestas Rhoncus Proin Corp.","dolor. Donec fringilla. Donec",0),("Pretium Neque LLP","feugiat tellus lorem eu metus. In lorem. Donec elementum, lorem",0),("Dui Augue Eu Associates","eleifend. Cras sed leo. Cras vehicula aliquet",0),("In Hendrerit Consectetuer LLC","venenatis lacus. Etiam bibendum fermentum metus. Aenean sed pede",0),("Tortor At Risus Limited","ornare, libero at auctor ullamcorper, nisl arcu",0),("Nec Leo Morbi Consulting","lacus pede sagittis augue, eu tempor erat neque non",0),("Id Sapien Cras Industries","nascetur ridiculus mus. Aenean eget",0),("Diam LLP","cubilia Curae;",0),("Nunc Ut Corporation","sagittis augue, eu tempor erat neque non quam. Pellentesque",1),("Augue Inc.","posuere cubilia Curae;",1),("Pellentesque Tincidunt Tempus Foundation","Aliquam vulputate ullamcorper magna. Sed eu eros. Nam consequat",0),("Lacus Pede Sagittis Corporation","ipsum. Donec sollicitudin adipiscing ligula. Aenean gravida",0),("Sagittis Consulting","magna. Ut tincidunt orci",0),("Ullamcorper Incorporated","eros. Nam consequat",1),("Aenean Gravida Nunc Incorporated","ut aliquam iaculis, lacus pede sagittis augue, eu",0),("Nec Eleifend Non Corporation","Vivamus sit amet",1),("Risus Donec Associates","fames ac turpis egestas. Fusce aliquet magna a neque.",1),("Donec Sollicitudin Inc.","ipsum dolor sit amet, consectetuer",1),("A Company","pretium neque. Morbi quis urna. Nunc quis arcu",1),("Pellentesque Industries","In scelerisque scelerisque",0),("Ornare Elit Elit Foundation","libero. Morbi accumsan laoreet",0),("Tincidunt Institute","Integer sem elit,",1),("Tristique Neque Venenatis LLC","sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus",0),("Lorem Ac Consulting","eu metus. In lorem. Donec elementum, lorem ut aliquam",0),("Cras Dolor Inc.","sit amet nulla. Donec non justo. Proin non",1),("Rutrum Eu Ultrices Limited","nec urna et arcu imperdiet ullamcorper. Duis",1),("Pellentesque Incorporated","pharetra ut, pharetra sed, hendrerit a,",0),("Arcu Incorporated","luctus sit amet, faucibus ut, nulla. Cras eu",1),("Vitae Limited","nisl arcu iaculis enim, sit amet ornare lectus justo",0),("Felis Donec Tempor LLC","at,",0),("Risus At Fringilla LLC","posuere, enim nisl elementum",0),("Duis Mi Enim PC","sed leo. Cras vehicula aliquet",1),("Dui LLC","posuere at, velit. Cras lorem lorem, luctus ut,",1),("Ut Quam Vel Consulting","eget laoreet posuere, enim nisl elementum purus, accumsan interdum libero",0),("Libero Proin Inc.","Phasellus nulla. Integer",1),("Sed Et Corp.","convallis",1),("Magna Et Ipsum Corp.","risus varius",1),("Amet Industries","aliquet libero. Integer in magna. Phasellus dolor elit,",1),("Etiam Vestibulum Industries","risus quis diam luctus",0),("Ut Cursus Institute","nunc, ullamcorper eu, euismod ac, fermentum",1),("Tincidunt Corporation","Etiam laoreet, libero et",1),("Torquent LLC","metus urna convallis erat, eget tincidunt",0),("Euismod Est Arcu Institute","lacus. Mauris non dui nec urna suscipit nonummy. Fusce",0),("Vehicula Corp.","dictum ultricies",0),("Pharetra PC","nec, diam. Duis mi enim, condimentum eget, volutpat",0),("Lacus Etiam Ltd","erat. Etiam vestibulum massa",0),("Ipsum Sodales Institute","Sed diam",0),("Est Mauris Eu LLC","nulla. Integer vulputate,",1),("Ante Blandit Viverra LLC","dignissim tempor arcu. Vestibulum ut eros",1),("Lacus Quisque LLC","pretium",1),("Fusce Incorporated","egestas a, dui. Cras pellentesque.",1),("Sagittis Augue Eu Foundation","nisi nibh",1),("Ornare Facilisis Eget PC","pellentesque a, facilisis non,",1),("Curabitur Ut Inc.","aliquet odio. Etiam ligula tortor, dictum",1),("Augue Associates","hendrerit. Donec porttitor tellus non magna. Nam ligula elit,",0),("Et Industries","elit. Etiam laoreet, libero et tristique pellentesque, tellus sem mollis",1),("Nibh Quisque Industries","lacus, varius et, euismod et, commodo at, libero. Morbi accumsan",0),("Lectus Sit Institute","metus. In nec orci. Donec nibh. Quisque nonummy ipsum",1),("Ipsum Sodales Purus Associates","mollis non, cursus non, egestas a, dui. Cras",0),("Mauris Magna Duis Incorporated","lacus. Aliquam rutrum lorem ac risus.",1),("Eget Varius Limited","augue malesuada malesuada. Integer",0),("Quisque Ltd","Proin dolor. Nulla",0),("Aliquam LLC","augue",0),("Diam Ltd","elit, dictum eu, eleifend",1),("Massa Limited","Vivamus nisi. Mauris nulla. Integer urna. Vivamus molestie dapibus ligula.",0),("Per Conubia PC","Mauris vel turpis. Aliquam adipiscing lobortis risus. In mi pede,",1),("Iaculis Lacus LLP","pharetra, felis eget varius ultrices,",0),("Etiam Ligula Tortor Industries","in, cursus et, eros. Proin ultrices. Duis volutpat",0),("Cras Eget Nisi Foundation","in, cursus et, eros. Proin ultrices. Duis",0),("Cursus Diam At Limited","ultrices, mauris ipsum porta elit,",1),("Sem Semper Industries","dis",0),("Orci Lobortis Augue LLC","bibendum ullamcorper. Duis cursus, diam at pretium aliquet,",0),("Eros Nam Consequat LLP","adipiscing elit. Curabitur sed tortor. Integer",1),("Pellentesque Tincidunt Company","lorem ut",0),("Donec Feugiat Associates","eros turpis non enim. Mauris",1),("Dui Nec LLP","eu turpis. Nulla aliquet.",1),("Curabitur Institute","mus. Aenean eget magna. Suspendisse tristique neque",1),("Et Netus Et Institute","cursus luctus, ipsum leo elementum",1),("Tincidunt Congue Institute","pede sagittis augue, eu tempor erat neque non quam.",1),("Enim Gravida Sit Corporation","lectus convallis",1),("Congue A Aliquet Corp.","sagittis augue, eu tempor erat neque non quam.",1),("Vulputate Ullamcorper Company","porttitor",0),("Neque LLP","consectetuer euismod est arcu ac orci. Ut semper pretium",0),("Ornare Institute","nulla. In tincidunt congue turpis. In condimentum. Donec",1),("Duis At Corporation","luctus et ultrices",1),("Cras LLP","velit eget",1),("Diam Associates","feugiat metus sit amet ante. Vivamus non lorem vitae odio",0);


-- Add two new recods
INSERT INTO todo
    (title, description, is_completed)
    values('mmm', 'llevar a chanchito feliz al football', 0);

INSERT INTO todo
    (title, description, is_completed)
    values('no se', 'realizar sesion de fotografica de chanchito feliz', 0);


-- SELECT BY ID
SELECT * 
FROM todo
WHERE id = 5;

-- COUNT ALL
SELECT COUNT(*)
FROM todo;

-- WHERE LIKE
SELECT *
FROM todo
WHERE description LIKE '%chanchito%';


-- ORDER BY id descendant
SELECT *
FROM todo
WHERE description LIKE '%chanchito%'
ORDER BY id DESC;


-- DELETE
SELECT * 
FROM todo
WHERE id = 9;


-- BE CAREFULL..
-- ALWAYS ALWAYS USE A WHERE CLAUSELE
DELETE
FROM todo

-- this item should not appear
DELETE
FROM todo
WHERE id = 9;

--  PASTE AGAIN THE PREVIOUS RECORDS


INSERT INTO todo
    (title, description, is_completed)
    values('Second', 'llevar a chanchito feliz al doctor, duele panza', 0);


-- INSERT 100 RECORDS
INSERT INTO todo (title,description,is_completed) VALUES ("Nibh Aliquam Ornare Company","purus mauris a",0),("Dis Parturient Montes Limited","posuere cubilia",1),("Metus Urna Convallis Inc.","diam luctus lobortis. Class aptent taciti sociosqu",1),("Volutpat Nulla Dignissim Industries","est, vitae sodales nisi magna sed dui. Fusce aliquam, enim",1),("Integer Eu Lacus Inc.","parturient montes, nascetur ridiculus mus. Donec dignissim magna",0),("Augue Industries","nonummy ipsum non arcu. Vivamus sit amet risus. Donec egestas.",0),("In At Foundation","consectetuer rhoncus. Nullam velit dui, semper et,",1),("Ad Ltd","a felis ullamcorper viverra. Maecenas iaculis aliquet",0),("Consectetuer Adipiscing Elit Institute","rhoncus id, mollis nec, cursus a, enim. Suspendisse aliquet, sem",1),("Praesent Eu Dui Institute","suscipit",1),("Aenean Egestas Hendrerit Ltd","aliquet, metus urna convallis erat, eget",1),("Augue Limited","consectetuer adipiscing",1),("Imperdiet Ornare Corporation","sociis natoque penatibus et magnis dis parturient",1),("Egestas Rhoncus Proin Corp.","dolor. Donec fringilla. Donec",0),("Pretium Neque LLP","feugiat tellus lorem eu metus. In lorem. Donec elementum, lorem",0),("Dui Augue Eu Associates","eleifend. Cras sed leo. Cras vehicula aliquet",0),("In Hendrerit Consectetuer LLC","venenatis lacus. Etiam bibendum fermentum metus. Aenean sed pede",0),("Tortor At Risus Limited","ornare, libero at auctor ullamcorper, nisl arcu",0),("Nec Leo Morbi Consulting","lacus pede sagittis augue, eu tempor erat neque non",0),("Id Sapien Cras Industries","nascetur ridiculus mus. Aenean eget",0),("Diam LLP","cubilia Curae;",0),("Nunc Ut Corporation","sagittis augue, eu tempor erat neque non quam. Pellentesque",1),("Augue Inc.","posuere cubilia Curae;",1),("Pellentesque Tincidunt Tempus Foundation","Aliquam vulputate ullamcorper magna. Sed eu eros. Nam consequat",0),("Lacus Pede Sagittis Corporation","ipsum. Donec sollicitudin adipiscing ligula. Aenean gravida",0),("Sagittis Consulting","magna. Ut tincidunt orci",0),("Ullamcorper Incorporated","eros. Nam consequat",1),("Aenean Gravida Nunc Incorporated","ut aliquam iaculis, lacus pede sagittis augue, eu",0),("Nec Eleifend Non Corporation","Vivamus sit amet",1),("Risus Donec Associates","fames ac turpis egestas. Fusce aliquet magna a neque.",1),("Donec Sollicitudin Inc.","ipsum dolor sit amet, consectetuer",1),("A Company","pretium neque. Morbi quis urna. Nunc quis arcu",1),("Pellentesque Industries","In scelerisque scelerisque",0),("Ornare Elit Elit Foundation","libero. Morbi accumsan laoreet",0),("Tincidunt Institute","Integer sem elit,",1),("Tristique Neque Venenatis LLC","sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus",0),("Lorem Ac Consulting","eu metus. In lorem. Donec elementum, lorem ut aliquam",0),("Cras Dolor Inc.","sit amet nulla. Donec non justo. Proin non",1),("Rutrum Eu Ultrices Limited","nec urna et arcu imperdiet ullamcorper. Duis",1),("Pellentesque Incorporated","pharetra ut, pharetra sed, hendrerit a,",0),("Arcu Incorporated","luctus sit amet, faucibus ut, nulla. Cras eu",1),("Vitae Limited","nisl arcu iaculis enim, sit amet ornare lectus justo",0),("Felis Donec Tempor LLC","at,",0),("Risus At Fringilla LLC","posuere, enim nisl elementum",0),("Duis Mi Enim PC","sed leo. Cras vehicula aliquet",1),("Dui LLC","posuere at, velit. Cras lorem lorem, luctus ut,",1),("Ut Quam Vel Consulting","eget laoreet posuere, enim nisl elementum purus, accumsan interdum libero",0),("Libero Proin Inc.","Phasellus nulla. Integer",1),("Sed Et Corp.","convallis",1),("Magna Et Ipsum Corp.","risus varius",1),("Amet Industries","aliquet libero. Integer in magna. Phasellus dolor elit,",1),("Etiam Vestibulum Industries","risus quis diam luctus",0),("Ut Cursus Institute","nunc, ullamcorper eu, euismod ac, fermentum",1),("Tincidunt Corporation","Etiam laoreet, libero et",1),("Torquent LLC","metus urna convallis erat, eget tincidunt",0),("Euismod Est Arcu Institute","lacus. Mauris non dui nec urna suscipit nonummy. Fusce",0),("Vehicula Corp.","dictum ultricies",0),("Pharetra PC","nec, diam. Duis mi enim, condimentum eget, volutpat",0),("Lacus Etiam Ltd","erat. Etiam vestibulum massa",0),("Ipsum Sodales Institute","Sed diam",0),("Est Mauris Eu LLC","nulla. Integer vulputate,",1),("Ante Blandit Viverra LLC","dignissim tempor arcu. Vestibulum ut eros",1),("Lacus Quisque LLC","pretium",1),("Fusce Incorporated","egestas a, dui. Cras pellentesque.",1),("Sagittis Augue Eu Foundation","nisi nibh",1),("Ornare Facilisis Eget PC","pellentesque a, facilisis non,",1),("Curabitur Ut Inc.","aliquet odio. Etiam ligula tortor, dictum",1),("Augue Associates","hendrerit. Donec porttitor tellus non magna. Nam ligula elit,",0),("Et Industries","elit. Etiam laoreet, libero et tristique pellentesque, tellus sem mollis",1),("Nibh Quisque Industries","lacus, varius et, euismod et, commodo at, libero. Morbi accumsan",0),("Lectus Sit Institute","metus. In nec orci. Donec nibh. Quisque nonummy ipsum",1),("Ipsum Sodales Purus Associates","mollis non, cursus non, egestas a, dui. Cras",0),("Mauris Magna Duis Incorporated","lacus. Aliquam rutrum lorem ac risus.",1),("Eget Varius Limited","augue malesuada malesuada. Integer",0),("Quisque Ltd","Proin dolor. Nulla",0),("Aliquam LLC","augue",0),("Diam Ltd","elit, dictum eu, eleifend",1),("Massa Limited","Vivamus nisi. Mauris nulla. Integer urna. Vivamus molestie dapibus ligula.",0),("Per Conubia PC","Mauris vel turpis. Aliquam adipiscing lobortis risus. In mi pede,",1),("Iaculis Lacus LLP","pharetra, felis eget varius ultrices,",0),("Etiam Ligula Tortor Industries","in, cursus et, eros. Proin ultrices. Duis volutpat",0),("Cras Eget Nisi Foundation","in, cursus et, eros. Proin ultrices. Duis",0),("Cursus Diam At Limited","ultrices, mauris ipsum porta elit,",1),("Sem Semper Industries","dis",0),("Orci Lobortis Augue LLC","bibendum ullamcorper. Duis cursus, diam at pretium aliquet,",0),("Eros Nam Consequat LLP","adipiscing elit. Curabitur sed tortor. Integer",1),("Pellentesque Tincidunt Company","lorem ut",0),("Donec Feugiat Associates","eros turpis non enim. Mauris",1),("Dui Nec LLP","eu turpis. Nulla aliquet.",1),("Curabitur Institute","mus. Aenean eget magna. Suspendisse tristique neque",1),("Et Netus Et Institute","cursus luctus, ipsum leo elementum",1),("Tincidunt Congue Institute","pede sagittis augue, eu tempor erat neque non quam.",1),("Enim Gravida Sit Corporation","lectus convallis",1),("Congue A Aliquet Corp.","sagittis augue, eu tempor erat neque non quam.",1),("Vulputate Ullamcorper Company","porttitor",0),("Neque LLP","consectetuer euismod est arcu ac orci. Ut semper pretium",0),("Ornare Institute","nulla. In tincidunt congue turpis. In condimentum. Donec",1),("Duis At Corporation","luctus et ultrices",1),("Cras LLP","velit eget",1),("Diam Associates","feugiat metus sit amet ante. Vivamus non lorem vitae odio",0);

-- Add two new recods
INSERT INTO todo
    (title, description, is_completed)
    values('mmm', 'llevar a chanchito feliz al football', 0);

INSERT INTO todo
    (title, description, is_completed)
    values('no se', 'realizar sesion de fotografica de chanchito feliz', 0);


INSERT INTO todo
    (title, description, is_completed)
    values( 'First todo', 'Do a lot of very important things', 0 );




-- update title and description
SELECT *
FROM todo
WHERE description LIKE '%chanchito%';

UPDATE  todo
SET 
    title = 'ir a football',
    description = 'LLEVAR A chanchito feliz al Balon Pie'
WHERE id = 207;    
