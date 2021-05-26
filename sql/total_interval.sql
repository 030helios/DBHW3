select WLD.Date as Date, WLD.Cum_case as Daily_umulative_case, dowjone.Adj_close as DJI
from (
    select Date_reported as Date, SUM(New_cases) as Cum_case from who_covid_19
    group by Date_reported
    ) as WLD, dowjone
where WLD.Date = dowjone.Date_reported