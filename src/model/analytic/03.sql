SELECT 
    a.employment_status,
    COUNT(a.candidate_application_id) AS candidate_count
FROM 
    "Sat_Candidate_application_info" a
GROUP BY 
    a.employment_status;
