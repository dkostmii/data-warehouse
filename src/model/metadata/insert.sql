INSERT INTO "Meta_DataElements" ("element_id", "table_name", "column_name", "data_type", "is_nullable", "default_value", "description", "load_date")
VALUES
    (gen_random_uuid(), 'Hub_Candidate', 'candidate_id', 'UUID', FALSE, 'gen_random_uuid()', 'Унікальний ідентифікатор кандидата', NOW()),
    (gen_random_uuid(), 'Sat_Candidate_contacts', 'phone_number', 'VARCHAR(22)', FALSE, NULL, 'Номер телефону кандидата', NOW());

INSERT INTO "Meta_Tables" ("table_id", "table_name", "description", "load_date")
VALUES
    (gen_random_uuid(), 'Hub_Candidate', 'Таблиця хабу для кандидатів', NOW()),
    (gen_random_uuid(), 'Sat_Company_info', 'Таблиця сателітів для інформації про компанії', NOW());

INSERT INTO "Meta_Relationships" ("relationship_id", "table_name", "column_name", "related_table_name", "related_column_name", "relationship_type", "load_date")
VALUES
    (gen_random_uuid(), 'Sat_Candidate_info', 'candidate_id', 'Hub_Candidate', 'candidate_id', '1:1', NOW()),
    (gen_random_uuid(), 'Link_Vacancy', 'company_id', 'Hub_Company', 'company_id', 'N:1', NOW());

INSERT INTO "Meta_Sources" ("source_id", "source_name", "description", "load_date")
VALUES
    (gen_random_uuid(), 'HR System', 'Внутрішня система управління персоналом', NOW()),
    (gen_random_uuid(), 'External Job Portal', 'Зовнішній портал для пошуку роботи', NOW());

INSERT INTO "Meta_ETL_Processes" ("etl_id", "process_name", "source_table", "target_table", "description", "load_date")
VALUES
    (gen_random_uuid(), 'Load Candidates', 'External Job Portal', 'Hub_Candidate', 'Завантаження даних про кандидатів із зовнішнього порталу', NOW()),
    (gen_random_uuid(), 'Update Company Info', 'HR System', 'Sat_Company_info', 'Оновлення інформації про компанії з внутрішньої системи', NOW());

INSERT INTO "Meta_Business_Rules" ("rule_id", "rule_name", "description", "table_name", "column_name", "rule_expression", "load_date")
VALUES
    (gen_random_uuid(), 'Valid Email Format', 'Перевірка формату електронної пошти', 'Sat_Candidate_contacts', 'email', 'REGEXP_LIKE(email, ''^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'')', NOW()),
    (gen_random_uuid(), 'Non-Negative Salary', 'Зарплата не може бути негативною', 'Sat_Vacancy_info', 'salary', 'salary >= 0', NOW());

INSERT INTO "Meta_Audit" ("audit_id", "table_name", "column_name", "old_value", "new_value", "change_date", "changed_by")
VALUES
    (gen_random_uuid(), 'Sat_Candidate_contacts', 'phone_number', '1234567890', '0987654321', NOW(), 'admin'),
    (gen_random_uuid(), 'Sat_Company_info', 'location', 'Old Location', 'New Location', NOW(), 'system');

INSERT INTO "Meta_Users" ("user_id", "user_name", "role", "email", "load_date")
VALUES
    (gen_random_uuid(), 'john_doe', 'Data Analyst', 'john.doe@example.com', NOW()),
    (gen_random_uuid(), 'jane_smith', 'Database Admin', 'jane.smith@example.com', NOW());
