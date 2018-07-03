CREATE EXTENSION IF NOT EXISTS multicorn; 

DROP SERVER IF EXISTS multicorn_test;
CREATE SERVER multicorn_test FOREIGN DATA WRAPPER multicorn OPTIONS(
  wrapper 'postgres-wikipedia.postgres-wikipedia.ConstantForeignDataWrapper'
);

DROP FOREIGN TABLE IF EXISTS test;
CREATE FOREIGN TABLE test (
  test character varying,
  test2 character varying
) server multicorn_srv;