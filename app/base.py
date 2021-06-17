import sqlite3
db = sqlite3.connect('databasev2.db')

db.execute('create table posts (postid integer not null primary key autoincrement, image text, text text, userid integer not null, foreign key(userid) references users(userid));')
db.commit()
db.close()
