select SUM(cumulative_data.deaths) / SUM((cumulative_data.cases + 0.0)) as death_rate
from (
     select Max(sars.Cumulative_cases) as cases, Max(sars.deaths) as deaths
     from sars as sars
     group by sars.Country
     ) as cumulative_data;