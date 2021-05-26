select SUM(cumulative_data.deaths) / SUM((cumulative_data.cases + 0.0)) as death_rate
from (
     select Max(covid19.Cumulative_cases) as cases, Max(covid19.Cumulative_deaths) as deaths
     from who_covid_19 as covid19
     group by covid19.Country
     ) as cumulative_data;