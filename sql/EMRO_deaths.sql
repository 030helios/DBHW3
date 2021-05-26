select substr(max_data.date,1,6) as date, DR_data.region as region, DR_data.Country as Country, max_data.deaths as deaths
from (
     select DR_data.date as date, MAX(DR_data.deaths) as deaths
     from (
	      select SUBSTR(covid19.Date_reported, 1, 7) as date, Country, covid19.WHO_region as region, SUM(covid19.New_deaths) as deaths
	      from who_covid_19 as covid19
		  where region = 'EMRO'
	      group by date, Country
          ) as DR_data
     group by date
     ) as max_data,
	(
	select SUBSTR(covid19.Date_reported, 1, 7) as date, Country, covid19.WHO_region as region, SUM(covid19.New_deaths) as deaths
	from who_covid_19 as covid19
	where region = 'EMRO'
    group by date, Country
	) as DR_data
where DR_data.deaths = max_data.deaths

