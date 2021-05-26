select t.Date_reported as Date, covid19.cases as Total_cases, (tw.International_cases+tw.National_cases) as TW_cases, d.Adj_Close as Dow_AdjClose, t.Adj_Close as TsecIndex_AdjClose
from tsec_index as t, dowjone as d, 
	(select covid19.Date_reported as Date, sum(covid19.New_cases)as cases 
	from who_covid_19 as covid19 
	group by covid19.Date_reported) as covid19, tw_covid_19 as tw
where t.Date_reported = d.Date_reported
and covid19.Date = d.Date_reported
and tw.Date_reported = d.Date_reported

