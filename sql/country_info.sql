select cumulative_data.Country as Country, cumulative_data.covid19_cases as covid19_cumulative_cases, 
	   cumulative_data.covid19_deaths / (cumulative_data.covid19_cases+0.0) as covid19_death_rate, 
	   cumulative_data.sars_cases as sars_cumulative_cases, 
	   cumulative_data.sars_deaths / (cumulative_data.sars_cases+0.0) as sars_death_rate
from (
	  select covid19.Country as Country, MAX(covid19.Cumulative_cases) as covid19_cases, 
	         MAX(covid19.Cumulative_deaths) as covid19_deaths, 
	         Max(sars.Cumulative_cases) as sars_cases, Max(sars.deaths) as sars_deaths
	  from who_covid_19 as covid19, sars as sars
	  where covid19.Country = sars.Country
	  group by covid19.Country
	 ) as cumulative_data
where Country LIKE 'Romania';

