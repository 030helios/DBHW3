select t.Date_reported as Date, t.open as TsecIndex_open, t.Adj_Close as TsecIndex_AdjClose, t.volume as TsecIndex_volume, 
	   d.open as Dow_open, d.Adj_Close as Dow_AdjClose, d.volume as Dow_volume
from tsec_index as t, dowjone as d
where t.Date_reported = d.Date_reported
and t.Date_reported = '2002/1/9'
