题目1：现在运营想要找到每个学校gpa最低的同学来做调研，请你取出每个学校的最低gpa的学生。
Id university gpa
1 山东大学 3.8
2 复旦大学 3.6
3 复旦大学 4
4 山东大学 3.4

--with tmp_table as (
--select university, sort_array(collect_list(gpa))
--from test1
--group by university)

select id, university, gpa
from T1
inner join

(
    select university, min(gpa) as gpa
    from test1
    group by university)) T2

on T1.university = T2.university AND T1.gpa = T2.gpa
order by university



