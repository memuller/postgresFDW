CREATE EXTENSION IF NOT EXISTS multicorn; 

DROP SERVER IF EXISTS multicorn_test CASCADE;
CREATE SERVER multicorn_test FOREIGN DATA WRAPPER multicorn OPTIONS(
  wrapper 'memPostgres.Wikipedia'
);

DROP FOREIGN TABLE IF EXISTS test;
CREATE FOREIGN TABLE wikipedia_en (
  title character varying,
  url character varying,
  description character varying
) server multicorn_test;
CREATE FOREIGN TABLE wikipedia_pt (
  title character varying,
  url character varying,
  description character varying
) server multicorn_test options (
  language 'pt'
);