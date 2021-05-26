select * 
from
	(select substr(covid19_rate.Date, 1, 6) as Date, covid19_rate.region as region, covid19_rate.rate as rate, 
		dow_rate.rate as Dow_Adj_Close_rate
	from
	(
	/* rate of covid19*/
	select hola.bd as Date, hola.region as region, ((hola.bc-max(hola.ac))/max(hola.ac)) as rate
	from	(
	select a.Date as ad, b.Date as bd, a.region as region, a.cases as ac, b.cases as bc
	from	(
		select SUBSTR(covid19.Date_reported, 1, 7) as Date, covid19.WHO_region as region, sum(covid19.New_cases) as cases
		from who_covid_19 as covid19
		group by Date, region
		) as a,
		(
		select SUBSTR(covid19.Date_reported, 1, 7) as Date, covid19.WHO_region as region, sum(covid19.New_cases) as cases
		from who_covid_19 as covid19
		group by Date, region
		) as b
	where a.Date < b.Date 
	and a.region = b.region
	) as hola
	group by hola.bd, hola.region
	order by hola.region, hola.bd

	) as covid19_rate, 
	(
	/*rate of dowjone*/
	select hola.bd as Date, ((hola.avg_close_b-max(hola.avg_close_a))/max(hola.avg_close_a)) as rate
	from (
		select month_data_a.Date as ad, month_data_b.Date as bd, month_data_a.avg_close as avg_close_a, month_data_b.avg_close as avg_close_b
		from (
			select SUBSTR(dow.Date_reported, 1, 7) as Date, AVG(dow.Adj_Close) as avg_close
			from dowjone as dow
			group by Date
			) as month_data_a,
			(
			select SUBSTR(dow.Date_reported, 1, 7) as Date, AVG(dow.Adj_Close) as avg_close
			from dowjone as dow
			group by Date
			) as month_data_b
		where month_data_a.Date < month_data_b.Date
		) as hola
	group by Date
	order by Date

	) as dow_rate
	where covid19_rate.Date = dow_rate.Date
	order by region, Date
	) as summary
where region = 'WPRO'