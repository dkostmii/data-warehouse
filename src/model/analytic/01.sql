SELECT 
    a.first_name,
    a.last_name,
    a.employment_status,
    v.name AS vacancy_name
FROM 
    "Sat_Candidate_application_info" a
JOIN 
    "Sat_Vacancy" v 
ON 
    a.candidate_application_id = v.candidate_application_id
WHERE 
    a.employment_status = 'employed';
