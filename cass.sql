CONCAT(CONVERT(varchar, [Exception ID]), 
       CONVERT(varchar, [AGE]), 
       CONVERT(varchar, CONVERT(date, [Last Load Date])))
NOT IN (SELECT CONCAT(CONVERT(varchar, i_exception_id), 
                        CONVERT(varchar, t_age), 
                        CONVERT(varchar, CONVERT(date, s_last_load_date)))
        FROM [daedbo].[dae_custbi_cass])
