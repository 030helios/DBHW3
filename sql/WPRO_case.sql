select max_data.date as date, DR_data.region as region, DR_data.Country as Country, max_data.cases as cases

from (
     select DR_data.date as date, MAX(DR_data.cases) as cases
     from (
	      select SUBSTR(covid19.Date_reported, 1, 7) as date, Country, covid19.WHO_region as region, SUM(covid19.New_cases) as cases
	      from who_covid_19 as covid19
		  where region = 'WPRO'
	      group by date, Country
          ) as DR_data
     group by date
     ) as max_data,
	(
	select SUBSTR(covid19.Date_reported, 1, 7) as date, Country, covid19.WHO_region as region, SUM(covid19.New_cases) as cases
	from who_covid_19 as covid19
	where region = 'WPRO'
    group by date, Country
	) as DR_data
where DR_data.cases = max_data.cases

