SELECT 
    c.company_location,
    COUNT(v.candidate_application_id) AS total_vacancies,
    AVG(v.salary) AS average_salary
FROM 
    "Sat_Vacancy" v
JOIN 
    "Sat_Company" c 
ON 
    v.candidate_application_id = c.candidate_application_id
GROUP BY 
    c.company_location;
