SELECT 
    a.first_name,
    a.last_name,
    a.phone_number,
    a.email,
    p.name AS production_branch
FROM 
    "Sat_Candidate_application_info" a
JOIN 
    "Sat_Production_branch" p 
ON 
    a.candidate_application_id = p.candidate_application_id
WHERE 
    p.name = 'IT';
