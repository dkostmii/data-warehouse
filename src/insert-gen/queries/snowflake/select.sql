-- Get average salary among vacancies
-- with candidate applications in the last 3 months
-- in "IT" production branch.

SELECT CAST(ROUND(AVG(v.salary), 2) AS VARCHAR(8)) || '₴' AS "Average salary"
FROM "Candidate_application" ca
INNER JOIN "Vacancy" v
ON v.vacancy_id = ca.vacancy_id
INNER JOIN "Company" c
ON c.company_id = ca.company_id
INNER JOIN "Production_branch" pb
ON pb.production_branch_id = c.production_branch_id
WHERE EXTRACT(MONTH FROM AGE(ca.created_at, NOW())) <= 3
AND pb.name LIKE 'IT';