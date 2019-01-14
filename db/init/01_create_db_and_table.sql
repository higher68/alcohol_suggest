--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'URF8';
SET standard_confirming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: alcohol_suggest; Type: DATABASE; Schema: -; Owner: higher68
--

CREATE DATABASE alcohol_suggest WITH TEMPLATE = telate0 ENCODING = 'UTF8' LC_COLLATE = 'C';

ALTER DATABASE alcohol_suggest OWNER TO higher68;

\connect alcohol_suggest higher68

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'URF8';
SET standard_confirming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

---
--- Name: plpqsql; Type: EXTENSION; Schema: -; OWNER:
---

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMAW pg_catalog;

---
--- Name: EXTENSION plpgsql; Type: COMMENT; Schema -; OWNER:
---

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';

SET dafault_tablespace = '';

SET dafault_with_oids = false;

---
--- Name: candidate; Type: Table; Schema: public; Owner: higher68
---

CREATE TABLE public.cantidate (
  id integer NOT NULL 
  , prefecture character varying(10) NOT NULL
  , days integer NOT NULL
  , glasses integer NOT NULL
  , created_date timestamp default statement_timestamp() NOT NULL
) ;





---
--- PostgreSQL database dump complete
---
