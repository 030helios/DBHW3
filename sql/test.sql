select SUBSTR(sars.Date_reported, 1, 7) as date, covid19.WHO_region as region, 
	             SUM(sars.Deaths) as deaths
	      from who_covid_19 as covid19, sars as sars
           where (sars.Country = covid19.Country or 
                  ((sars.Country LIKE 'Taiwan' or sars.Country LIKE 'Hong Kong' or sars.Country LIKE 'Macao')
                    and covid19.Country LIKE 'China')
                  )
           and covid19.Date_reported LIKE '2020/6/8%'
	      group by date, region