select substr(d.Date, 1, 6) as Date, covid_US.cases as US_Cases, covid.cases as Total_Cases, d.Dow_AdjClose as Dow_AdjClose
from (
	select SUBSTR(d.Date_reported, 1, 7) as Date, avg(d.Adj_Close) as Dow_AdjClose
	from dowjone as d
	group by Date
	) as d, 
	(
	select SUBSTR(covid19.Date_reported, 1, 7) as Date, Sum(covid19.New_cases) as cases, covid19.Country_code as Country
	from who_covid_19 as covid19
	where covid19.Country_code = 'US'
	group by Date) as covid_US,
	(
	select SUBSTR(covid19.Date_reported, 1, 7) as Date, Sum(covid19.New_cases) as cases
	from who_covid_19 as covid19
	group by Date) as covid
where d.Date = covid.Date
and d.Date = covid_US.Date
