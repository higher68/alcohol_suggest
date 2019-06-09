--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: alcohol_suggest; Type: DATABASE; Schema: -; Owner: higher68
--

CREATE DATABASE alcohol_suggest WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C' LC_CTYPE = 'C';

ALTER DATABASE alcohol_suggest OWNER TO higher68;

\connect alcohol_suggest higher68

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

---
--- Name: plpqsql; Type: EXTENSION; Schema: -; OWNER:
---

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;

---
--- Name: EXTENSION plpgsql; Type: COMMENT; Schema -; OWNER:
---

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';

SET default_tablespace = '';

SET default_with_oids = false;

---
--- Name: candidates; Type: Table; Schema: public; Owner: higher68
---

CREATE TABLE public.cantidates (
  id integer NOT NULL
  , prefecture character varying(10) NOT NULL
  , days integer NOT NULL
  , glasses integer NOT NULL
  , data_source_ver integer NOT NULL
  , created_date timestamp default statement_timestamp() NOT NULL
);


ALTER TABLE public.cantidates OWNER TO higher68;

---
--- Name: archives; Type: Table; Schema: public; Owner: higher68
---

CREATE TABLE public.archives (
  id integer NOT NULL
  , prefecture character varying(10) NOT NULL
  , sales integer NOT NULL
  , consumption integer NOT NULL
  , data_source_ver integer NOT NULL
  , created_date timestamp default statement_timestamp() NOT NULL
) ;

ALTER TABLE public.archives OWNER TO higher68;

---
--- Name: settings; Type: Table; Schema: public; Owner: higher68
---

CREATE TABLE public.settings (
  past_length integer NOT NULL
  , candidate_num integer NOT NULL
  , alcohol_consumption_lower_limit integer NOT NULL
  , drink_days_upper_limit integer NOT NULL
  , ml_of_1glass integer NOT NULL
  , number_of_output_upper_limit integer NOT NULL
  , created_date timestamp default statement_timestamp() NOT NULL
) ;

ALTER TABLE public.settings OWNER TO higher68;

---
--- PostgreSQL database dump complete
---
