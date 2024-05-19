SELECT 
    vc.name AS vacancy_category,
    AVG(v.salary) AS average_salary
FROM 
    "Sat_Vacancy" v
JOIN 
    "Sat_Vacancy_category" vc 
ON 
    v.candidate_application_id = vc.candidate_application_id
GROUP BY 
    vc.name;
