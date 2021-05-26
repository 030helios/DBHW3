/*
create table who_covid_19(
    Date_reported varchar(15) not null, 
    Country_code varchar(10) not null, 
    Country varchar(30), 
    WHO_region varchar(10), 
    New_cases int not null, 
    Cumulative_cases int not null, 
    New_deaths int not null, 
    Cumulative_deaths int not null,   
    primary key (Date_reported, Country_code)
);

create table sars(
    Date_reported varchar(15) not null,
    Country varchar(30) not null, 
    Cumulative_cases int not null, 
    Deaths int not null, 
    Recovered int not null, 
    primary key (Date_reported, Country)
);

create table dowjone(
    Date_reported varchar(15) not null, 
    Open DOUBLE(30, 6) not null, 
    High DOUBLE(30, 6) not null, 
    Low DOUBLE(30, 6) not null, 
    Close DOUBLE(30, 6) not null, 
    Adj_Close DOUBLE(30, 6) not null, 
    Volume varchar(30) not null, 
    primary key (Date_reported)
);
*/

create table history(
    Date varchar(15) not null,
    Total_cases int not null,
    TW_cases int not null,
    Dow_AdjClose DOUBLE(30, 6) not null,
    TsecIndex_AdjClose DOUBLE(30, 6) not null
);
/*
create table tsec_index(
    Date_reported varchar(15) not null, 
    Open DOUBLE(30, 6), 
    High DOUBLE(30, 6), 
    Low DOUBLE(30, 6), 
    Close DOUBLE(30, 6), 
    Adj_Close DOUBLE(30, 6), 
    Volume varchar(30), 
    primary key (Date_reported)
);
/*
create table tw_covid_19(
    Date_reported varchar(15) not null, 
    Country_code varchar(10) not null, 
    Country varchar(30), 
    WHO_region varchar(10), 
    International_cases int not null,
    National_cases int not null,  
    Cumulative_cases int not null, 
    New_deaths int not null, 
    Cumulative_deaths int not null,   
    primary key (Date_reported, Country_code)
);

load data local infile './WHO_COVID_19_data.csv'
into table who_covid_19
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;

load data local infile './sars_data.csv'
into table sars
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;

load data local infile './DowJones_index.csv'
into table dowjone
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;

load data local infile './TSEC_index.csv'
into table tsec_index
fields terminated by ','
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines;

load data local infile './Taiwan_covid_19.csv'
into table tw_covid_19
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 lines;
*/