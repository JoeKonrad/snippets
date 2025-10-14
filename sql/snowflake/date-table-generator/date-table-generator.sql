select *
  from (select dateadd('day',row_number() over (order by seq4()) - 1,'2024-01-01'::DATE) AS calendar_date
          from table(generator(rowcount => 1000)))
where calendar_date < current_date()
