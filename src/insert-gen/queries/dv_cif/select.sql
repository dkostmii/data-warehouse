-- Get average salary among vacancies
-- with candidate applications in the last 3 months
-- in "IT" production branch.

SELECT CAST(ROUND(AVG(vi.salary), 2) AS VARCHAR(8)) || '₴' AS "Average salary"
FROM "Hub_Candidate" hca
INNER JOIN "Link_Vacancy" lv
ON lv.candidate_id = hca.candidate_id
INNER JOIN "Sat_Vacancy_info" vi
ON vi.vacancy_id = lv.vacancy_id
INNER JOIN "Hub_Company" hco
ON hco.company_id = lv.company_id
INNER JOIN "Sat_Production_branch" pb
ON pb.company_id = hco.company_id
WHERE EXTRACT(MONTH FROM AGE(hca.load_date, NOW())) <= 3
AND pb.name LIKE 'IT';