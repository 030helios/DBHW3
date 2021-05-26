select substr(t.Date, 1, 6) as Date, covid.cases as Total_Cases, tw.TW_cases as TW_cases, t.TSEC_AdjClose as TSEC_AdjClose
from (
	select SUBSTR(t.Date_reported, 1, 7) as Date, avg(t.Adj_Close) as TSEC_AdjClose
	from tsec_index as t
	group by Date
	) as t,
	(
	select SUBSTR(covid19.Date_reported, 1, 7) as Date, Sum(covid19.New_cases) as cases
	from who_covid_19 as covid19
	group by Date) as covid,
	(
	select SUBSTR(tw.Date_reported, 1, 7) as Date, Sum(tw.International_cases+tw.National_cases) as TW_cases
	from tw_covid_19 as tw
	group by Date
	) as tw
where t.Date = covid.Date
and tw.Date = covid.Date
