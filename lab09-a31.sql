DROP TABLE fn_backup;
CREATE TABLE fn_backup AS SELECT * FROM fn;
SELECT * FROM fn_backup ORDER BY x LIMIT 10;
