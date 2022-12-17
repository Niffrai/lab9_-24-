CREATE RULE prevent_updates AS ON UPDATE TO fn_backup DO INSTEAD NOTHING;
SELECT * FROM pg_rules;
