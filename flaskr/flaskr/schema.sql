drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	address text not null,
	zipcode text not null,
    home_description text not null
);
