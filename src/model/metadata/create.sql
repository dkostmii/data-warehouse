CREATE TABLE "Meta_DataElements" (
    "element_id" UUID DEFAULT gen_random_uuid(),
    "table_name" VARCHAR(100) NOT NULL,
    "column_name" VARCHAR(100) NOT NULL,
    "data_type" VARCHAR(50) NOT NULL,
    "is_nullable" BOOLEAN DEFAULT TRUE,
    "default_value" VARCHAR(100),
    "description" TEXT,
    "load_date" TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY ("element_id")
);

CREATE TABLE "Meta_Tables" (
    "table_id" UUID DEFAULT gen_random_uuid(),
    "table_name" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "load_date" TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY ("table_id")
);

CREATE TABLE "Meta_Relationships" (
    "relationship_id" UUID DEFAULT gen_random_uuid(),
    "table_name" VARCHAR(100) NOT NULL,
    "column_name" VARCHAR(100) NOT NULL,
    "related_table_name" VARCHAR(100) NOT NULL,
    "related_column_name" VARCHAR(100) NOT NULL,
    "relationship_type" VARCHAR(50) NOT NULL, -- Тип зв'язку, наприклад, 1:1, 1:N, M:N
    "load_date" TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY ("relationship_id")
);

CREATE TABLE "Meta_Sources" (
    "source_id" UUID DEFAULT gen_random_uuid(),
    "source_name" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "load_date" TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY ("source_id")
);

CREATE TABLE "Meta_ETL_Processes" (
    "etl_id" UUID DEFAULT gen_random_uuid(),
    "process_name" VARCHAR(100) NOT NULL,
    "source_table" VARCHAR(100) NOT NULL,
    "target_table" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "load_date" TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY ("etl_id")
);

CREATE TABLE "Meta_Business_Rules" (
    "rule_id" UUID DEFAULT gen_random_uuid(),
    "rule_name" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "table_name" VARCHAR(100) NOT NULL,
    "column_name" VARCHAR(100),
    "rule_expression" TEXT,
    "load_date" TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY ("rule_id")
);

CREATE TABLE "Meta_Audit" (
    "audit_id" UUID DEFAULT gen_random_uuid(),
    "table_name" VARCHAR(100) NOT NULL,
    "column_name" VARCHAR(100) NOT NULL,
    "old_value" VARCHAR(255),
    "new_value" VARCHAR(255),
    "change_date" TIMESTAMP DEFAULT NOW(),
    "changed_by" VARCHAR(100),
    PRIMARY KEY ("audit_id")
);

CREATE TABLE "Meta_Users" (
    "user_id" UUID DEFAULT gen_random_uuid(),
    "user_name" VARCHAR(100) NOT NULL,
    "role" VARCHAR(100) NOT NULL,
    "email" VARCHAR(100) NOT NULL,
    "load_date" TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY ("user_id")
);
