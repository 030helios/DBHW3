select distinct substr(max_data.Date, 1, 6) as Date, DR_data.region as region, DR_data.Country as Country, max_data.Deaths as Deaths
from (	
	select DR_data.date as Date, MAX(DR_data.Deaths) as Deaths
	from(
	      	select SUBSTR(sars.Date_reported, 1, 7) as Date, sars.Country as Country, max(sars.Deaths) as Deaths
		from sars,  
			( 
			select covid19.country as country, covid19.WHO_region as region
			from who_covid_19 as covid19
			group by country, region
			) as reg
		where sars.Country = reg.country
		and reg.region = 'WPRO'
		group by Date, sars.Country
	     ) as DR_data
     	group by Date
     ) as max_data, 
     (
      	select SUBSTR(sars.Date_reported, 1, 7) as Date, reg.region as region, sars.Country as Country, max(sars.Deaths) as Deaths
	from sars,  
		( 
		select covid19.country as country, covid19.WHO_region as region
		from who_covid_19 as covid19
		group by country, region
		) as reg
	where sars.Country = reg.country
	and reg.region = 'WPRO'
	group by Date, sars.Country
     ) as DR_data
where DR_data.Deaths = max_data.Deaths


