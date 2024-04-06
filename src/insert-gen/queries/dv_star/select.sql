-- Get average salary among vacancies
-- with candidate applications in the last 3 months
-- in "IT" production branch.

SELECT CAST(ROUND(AVG(v.salary), 2) AS VARCHAR(8)) || '₴' AS "Average salary"
FROM "Hub_Candidate_application" hca
INNER JOIN "Sat_Candidate_application_info" cai
ON cai.candidate_application_id = hca.candidate_application_id
INNER JOIN "Sat_Production_branch" pb
ON pb.Candidate_application_id = hca.candidate_application_id
INNER JOIN "Sat_Vacancy" v
ON v.candidate_application_id = hca.candidate_application_id
WHERE EXTRACT(MONTH FROM AGE(cai.created_at, NOW())) <= 3
AND pb.name LIKE 'IT';