select distinct(who_covid_19.country) as Country
from who_covid_19, sars
where who_covid_19.Country = sars.Country

