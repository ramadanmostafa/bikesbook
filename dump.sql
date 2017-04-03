--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO postgres;

--
-- Name: custom_user_customuser; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE custom_user_customuser (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(254),
    first_name character varying(254) NOT NULL,
    last_name character varying(254) NOT NULL,
    email character varying(254) NOT NULL,
    address character varying(254) NOT NULL,
    area_code character varying(20) NOT NULL,
    country_code character varying(10),
    date_joined timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    full_name character varying(254) NOT NULL,
    fb_id character varying(60),
    twitter_id character varying(60),
    avatar character varying(100),
    is_social boolean NOT NULL
);


ALTER TABLE public.custom_user_customuser OWNER TO postgres;

--
-- Name: custom_user_customuser_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE custom_user_customuser_groups (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.custom_user_customuser_groups OWNER TO postgres;

--
-- Name: custom_user_customuser_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE custom_user_customuser_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.custom_user_customuser_groups_id_seq OWNER TO postgres;

--
-- Name: custom_user_customuser_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE custom_user_customuser_groups_id_seq OWNED BY custom_user_customuser_groups.id;


--
-- Name: custom_user_customuser_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE custom_user_customuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.custom_user_customuser_id_seq OWNER TO postgres;

--
-- Name: custom_user_customuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE custom_user_customuser_id_seq OWNED BY custom_user_customuser.id;


--
-- Name: custom_user_customuser_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE custom_user_customuser_user_permissions (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.custom_user_customuser_user_permissions OWNER TO postgres;

--
-- Name: custom_user_customuser_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE custom_user_customuser_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.custom_user_customuser_user_permissions_id_seq OWNER TO postgres;

--
-- Name: custom_user_customuser_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE custom_user_customuser_user_permissions_id_seq OWNED BY custom_user_customuser_user_permissions.id;


--
-- Name: custom_user_emailconfirmed; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE custom_user_emailconfirmed (
    id integer NOT NULL,
    activation_key character varying(200) NOT NULL,
    confirmed boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.custom_user_emailconfirmed OWNER TO postgres;

--
-- Name: custom_user_emailconfirmed_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE custom_user_emailconfirmed_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.custom_user_emailconfirmed_id_seq OWNER TO postgres;

--
-- Name: custom_user_emailconfirmed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE custom_user_emailconfirmed_id_seq OWNED BY custom_user_emailconfirmed.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: garage_bicycestyle; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_bicycestyle (
    id integer NOT NULL,
    style character varying(120) NOT NULL
);


ALTER TABLE public.garage_bicycestyle OWNER TO postgres;

--
-- Name: garage_bicycestyle_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_bicycestyle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_bicycestyle_id_seq OWNER TO postgres;

--
-- Name: garage_bicycestyle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_bicycestyle_id_seq OWNED BY garage_bicycestyle.id;


--
-- Name: garage_bicycle; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_bicycle (
    id integer NOT NULL,
    make_id integer NOT NULL,
    style_id integer NOT NULL
);


ALTER TABLE public.garage_bicycle OWNER TO postgres;

--
-- Name: garage_bicycle_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_bicycle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_bicycle_id_seq OWNER TO postgres;

--
-- Name: garage_bicycle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_bicycle_id_seq OWNED BY garage_bicycle.id;


--
-- Name: garage_bicyclemake; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_bicyclemake (
    id integer NOT NULL,
    brand character varying(120) NOT NULL
);


ALTER TABLE public.garage_bicyclemake OWNER TO postgres;

--
-- Name: garage_bicyclemake_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_bicyclemake_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_bicyclemake_id_seq OWNER TO postgres;

--
-- Name: garage_bicyclemake_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_bicyclemake_id_seq OWNED BY garage_bicyclemake.id;


--
-- Name: garage_garage; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_garage (
    id integer NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    active boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.garage_garage OWNER TO postgres;

--
-- Name: garage_garage_bicycles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_garage_bicycles (
    id integer NOT NULL,
    garage_id integer NOT NULL,
    bicycle_id integer NOT NULL
);


ALTER TABLE public.garage_garage_bicycles OWNER TO postgres;

--
-- Name: garage_garage_bicycles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_garage_bicycles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_garage_bicycles_id_seq OWNER TO postgres;

--
-- Name: garage_garage_bicycles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_garage_bicycles_id_seq OWNED BY garage_garage_bicycles.id;


--
-- Name: garage_garage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_garage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_garage_id_seq OWNER TO postgres;

--
-- Name: garage_garage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_garage_id_seq OWNED BY garage_garage.id;


--
-- Name: garage_garage_motorcycles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_garage_motorcycles (
    id integer NOT NULL,
    garage_id integer NOT NULL,
    motorcycle_id integer NOT NULL
);


ALTER TABLE public.garage_garage_motorcycles OWNER TO postgres;

--
-- Name: garage_garage_motorcycles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_garage_motorcycles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_garage_motorcycles_id_seq OWNER TO postgres;

--
-- Name: garage_garage_motorcycles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_garage_motorcycles_id_seq OWNED BY garage_garage_motorcycles.id;


--
-- Name: garage_motorcycle; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_motorcycle (
    id integer NOT NULL,
    make_id integer NOT NULL,
    model_id integer NOT NULL,
    color character varying(120) NOT NULL,
    engine_size_id integer NOT NULL,
    production_year character varying(10) NOT NULL,
    style_id integer NOT NULL
);


ALTER TABLE public.garage_motorcycle OWNER TO postgres;

--
-- Name: garage_motorcycle_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_motorcycle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_motorcycle_id_seq OWNER TO postgres;

--
-- Name: garage_motorcycle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_motorcycle_id_seq OWNED BY garage_motorcycle.id;


--
-- Name: garage_motorengine; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_motorengine (
    id integer NOT NULL,
    cc character varying(120) NOT NULL
);


ALTER TABLE public.garage_motorengine OWNER TO postgres;

--
-- Name: garage_motorengine_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_motorengine_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_motorengine_id_seq OWNER TO postgres;

--
-- Name: garage_motorengine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_motorengine_id_seq OWNED BY garage_motorengine.id;


--
-- Name: garage_motormake; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_motormake (
    id integer NOT NULL,
    brand character varying(120) NOT NULL
);


ALTER TABLE public.garage_motormake OWNER TO postgres;

--
-- Name: garage_motormake_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_motormake_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_motormake_id_seq OWNER TO postgres;

--
-- Name: garage_motormake_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_motormake_id_seq OWNED BY garage_motormake.id;


--
-- Name: garage_motormodel; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_motormodel (
    id integer NOT NULL,
    model character varying(120) NOT NULL,
    make_id integer NOT NULL
);


ALTER TABLE public.garage_motormodel OWNER TO postgres;

--
-- Name: garage_motormodel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_motormodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_motormodel_id_seq OWNER TO postgres;

--
-- Name: garage_motormodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_motormodel_id_seq OWNED BY garage_motormodel.id;


--
-- Name: garage_motorstyle; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE garage_motorstyle (
    id integer NOT NULL,
    style character varying(120) NOT NULL
);


ALTER TABLE public.garage_motorstyle OWNER TO postgres;

--
-- Name: garage_motorstyle_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE garage_motorstyle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.garage_motorstyle_id_seq OWNER TO postgres;

--
-- Name: garage_motorstyle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE garage_motorstyle_id_seq OWNED BY garage_motorstyle.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_customuser ALTER COLUMN id SET DEFAULT nextval('custom_user_customuser_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_customuser_groups ALTER COLUMN id SET DEFAULT nextval('custom_user_customuser_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('custom_user_customuser_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_emailconfirmed ALTER COLUMN id SET DEFAULT nextval('custom_user_emailconfirmed_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_bicycestyle ALTER COLUMN id SET DEFAULT nextval('garage_bicycestyle_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_bicycle ALTER COLUMN id SET DEFAULT nextval('garage_bicycle_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_bicyclemake ALTER COLUMN id SET DEFAULT nextval('garage_bicyclemake_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_garage ALTER COLUMN id SET DEFAULT nextval('garage_garage_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_garage_bicycles ALTER COLUMN id SET DEFAULT nextval('garage_garage_bicycles_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_garage_motorcycles ALTER COLUMN id SET DEFAULT nextval('garage_garage_motorcycles_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motorcycle ALTER COLUMN id SET DEFAULT nextval('garage_motorcycle_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motorengine ALTER COLUMN id SET DEFAULT nextval('garage_motorengine_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motormake ALTER COLUMN id SET DEFAULT nextval('garage_motormake_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motormodel ALTER COLUMN id SET DEFAULT nextval('garage_motormodel_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motorstyle ALTER COLUMN id SET DEFAULT nextval('garage_motorstyle_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add Token	6	add_token
17	Can change Token	6	change_token
18	Can delete Token	6	delete_token
19	Can add user	7	add_customuser
20	Can change user	7	change_customuser
21	Can delete user	7	delete_customuser
22	Can add email confirmed	8	add_emailconfirmed
23	Can change email confirmed	8	change_emailconfirmed
24	Can delete email confirmed	8	delete_emailconfirmed
25	Can add motorcycle	9	add_motorcycle
26	Can change motorcycle	9	change_motorcycle
27	Can delete motorcycle	9	delete_motorcycle
28	Can add bicycle make	10	add_bicyclemake
29	Can change bicycle make	10	change_bicyclemake
30	Can delete bicycle make	10	delete_bicyclemake
31	Can add bicyce style	11	add_bicycestyle
32	Can change bicyce style	11	change_bicycestyle
33	Can delete bicyce style	11	delete_bicycestyle
34	Can add bicycle	12	add_bicycle
35	Can change bicycle	12	change_bicycle
36	Can delete bicycle	12	delete_bicycle
37	Can add garage	13	add_garage
38	Can change garage	13	change_garage
39	Can delete garage	13	delete_garage
40	Can add motor make	14	add_motormake
41	Can change motor make	14	change_motormake
42	Can delete motor make	14	delete_motormake
43	Can add motor model	15	add_motormodel
44	Can change motor model	15	change_motormodel
45	Can delete motor model	15	delete_motormodel
46	Can add motor style	16	add_motorstyle
47	Can change motor style	16	change_motorstyle
48	Can delete motor style	16	delete_motorstyle
49	Can add motor engine	17	add_motorengine
50	Can change motor engine	17	change_motorengine
51	Can delete motor engine	17	delete_motorengine
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 51, true);


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY authtoken_token (key, created, user_id) FROM stdin;
9a52c19d253a508eac56371da7fbdea237e11078	2016-08-23 18:02:55.056658+02	1
bfad5e927adeeb5571ce4686fcf9cf3a4cf55328	2016-08-23 18:04:46.826099+02	2
\.


--
-- Data for Name: custom_user_customuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY custom_user_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, address, area_code, country_code, date_joined, updated, is_active, is_staff, full_name, fb_id, twitter_id, avatar, is_social) FROM stdin;
1	pbkdf2_sha256$24000$wrfs4O08orfQ$CoGWGVHsFBc6EEWgLc2q9i24pTJqssMM/ZHXMxwCw8M=	2016-08-27 22:48:00.558989+02	t	\N			alsum@gmail.com			\N	2016-08-23 18:02:54.925196+02	2016-08-23 18:02:55.034152+02	t	t		\N	\N		f
2	pbkdf2_sha256$24000$CMMoFhQ6X3HI$eXtu1FtVrL7pdk7LlXaui2fRzTB7KACQUYO0aozzMIs=	2016-08-27 22:48:13.572026+02	f	sum	hassan		engsum@gmail.com			KW	2016-08-23 18:04:46.803657+02	2016-08-26 23:32:20.67347+02	t	f	sum	\N	\N	/static/img/placeholder.png	f
\.


--
-- Data for Name: custom_user_customuser_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY custom_user_customuser_groups (id, customuser_id, group_id) FROM stdin;
\.


--
-- Name: custom_user_customuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('custom_user_customuser_groups_id_seq', 1, false);


--
-- Name: custom_user_customuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('custom_user_customuser_id_seq', 2, true);


--
-- Data for Name: custom_user_customuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY custom_user_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
\.


--
-- Name: custom_user_customuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('custom_user_customuser_user_permissions_id_seq', 1, false);


--
-- Data for Name: custom_user_emailconfirmed; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY custom_user_emailconfirmed (id, activation_key, confirmed, user_id) FROM stdin;
1	89a917797e6c16581a91605326b33fdf1925e760	f	1
2	055a7e78d54aa68ecc88932cbc8a83b9c2f1886a	t	2
\.


--
-- Name: custom_user_emailconfirmed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('custom_user_emailconfirmed_id_seq', 2, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	authtoken	token
7	custom_user	customuser
8	custom_user	emailconfirmed
9	garage	motorcycle
10	garage	bicyclemake
11	garage	bicycestyle
12	garage	bicycle
13	garage	garage
14	garage	motormake
15	garage	motormodel
16	garage	motorstyle
17	garage	motorengine
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 17, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2016-08-23 17:54:49.348186+02
2	contenttypes	0002_remove_content_type_name	2016-08-23 17:54:49.414674+02
3	auth	0001_initial	2016-08-23 17:54:50.117321+02
4	auth	0002_alter_permission_name_max_length	2016-08-23 17:54:50.151736+02
5	auth	0003_alter_user_email_max_length	2016-08-23 17:54:50.179235+02
6	auth	0004_alter_user_username_opts	2016-08-23 17:54:50.198312+02
7	auth	0005_alter_user_last_login_null	2016-08-23 17:54:50.22392+02
8	auth	0006_require_contenttypes_0002	2016-08-23 17:54:50.229783+02
9	auth	0007_alter_validators_add_error_messages	2016-08-23 17:54:50.255131+02
10	custom_user	0001_initial	2016-08-23 17:54:51.085393+02
11	admin	0001_initial	2016-08-23 17:54:51.397322+02
12	admin	0002_logentry_remove_auto_add	2016-08-23 17:54:51.443134+02
13	authtoken	0001_initial	2016-08-23 17:54:51.643392+02
14	authtoken	0002_auto_20160226_1747	2016-08-23 17:54:51.765512+02
15	custom_user	0002_auto_20160725_2141	2016-08-23 17:54:51.843185+02
16	custom_user	0003_customuser_full_name	2016-08-23 17:54:52.22072+02
17	custom_user	0004_auto_20160729_2329	2016-08-23 17:54:52.267072+02
18	custom_user	0005_customuser_is_social	2016-08-23 17:54:52.676633+02
19	custom_user	0006_auto_20160803_1859	2016-08-23 17:54:52.734127+02
20	custom_user	0007_auto_20160803_1905	2016-08-23 17:54:52.778369+02
21	custom_user	0008_auto_20160803_1945	2016-08-23 17:54:53.143867+02
22	custom_user	0009_remove_customuser_is_social	2016-08-23 17:54:53.190189+02
23	custom_user	0010_auto_20160807_1934	2016-08-23 17:54:53.412097+02
24	custom_user	0011_customuser_avatar	2016-08-23 17:54:53.444993+02
25	custom_user	0012_auto_20160819_2315	2016-08-23 17:54:54.122933+02
26	garage	0001_initial	2016-08-23 17:54:54.891651+02
27	garage	0002_remove_garage_name	2016-08-23 17:54:54.948285+02
28	garage	0003_auto_20160823_1546	2016-08-23 17:54:55.494955+02
29	sessions	0001_initial	2016-08-23 17:54:55.749739+02
30	garage	0004_auto_20160826_1733	2016-08-26 19:33:50.620443+02
31	garage	0005_auto_20160827_2012	2016-08-27 22:12:32.382699+02
32	garage	0006_auto_20160827_2103	2016-08-27 23:03:47.009162+02
33	garage	0007_auto_20160827_2119	2016-08-27 23:19:43.527468+02
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 33, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
qkvg5g8loosqy5ssefav9etodhkoz77t	MjRjYmYzMjM2NWE5Nzg2ZTY2NTc2MjE4Njk2YzFjNjEzYjM0NGU4OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjYzZmJhMTUxNmY5YzQ2MjE1M2Y5ZmJmMWE5ZTJkN2NkYTNmMTU4OWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJjdXN0b21fdXNlci5iYWNrZW5kcy5DdXN0b21Vc2VyQXV0aCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=	2016-09-10 22:48:13.584986+02
\.


--
-- Data for Name: garage_bicycestyle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_bicycestyle (id, style) FROM stdin;
1	Road
2	Cyclocross
3	Touring
4	Triathlon/Time Trial
5	Flat-Bar Road
6	Track/Fixed-Gear
7	Mountain
8	Hybrid
9	Cruiser
10	Flat-Foot Comfort
11	City
12	BMX
13	Folding
14	Recumbent
15	Tandem
16	Adult
\.


--
-- Name: garage_bicycestyle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_bicycestyle_id_seq', 1, false);


--
-- Data for Name: garage_bicycle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_bicycle (id, make_id, style_id) FROM stdin;
9	3	3
\.


--
-- Name: garage_bicycle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_bicycle_id_seq', 9, true);


--
-- Data for Name: garage_bicyclemake; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_bicyclemake (id, brand) FROM stdin;
1	Giant
2	Trek
3	Specialized
4	Cannondale
5	Santa Cruz
6	GT
7	Scott
8	Yeti
9	Merida
10	Kona
11	Marin
12	Acros
13	Airborne
14	Answer
15	Avid
16	Azonic
17	Banshee
18	Bell
19	Bergamont
20	Bird Cycleworks
21	Black Burn
22	Blackspire
23	BLISS Protection
24	BlkMrkt Bikes
25	BMC
26	Bold Cycles
27	BOS MTB
28	Breezer
29	BTR Fabrications
30	Canfield Brothers
31	Cannondale
32	Canyon
33	Chromag Bikes
34	Chumba Racing
35	COLE
36	Commencal
37	Continental
38	Cove
39	CrankBrothers
40	Dakine
41	Dartmoor Bikes
42	Deity
43	Devinci
44	Diamondback
45	DMR Bikes
46	DT Swiss
47	DVO Suspension\nDurango
48	Durango
49	e13
50	Easton
51	Elka
52	Ellsworth
53	Ergon
54	EVOC Sports
55	Felt
56	Fly Racing
57	Fox Racing
58	Other
\.


--
-- Name: garage_bicyclemake_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_bicyclemake_id_seq', 1, false);


--
-- Data for Name: garage_garage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_garage (id, "timestamp", updated, active, user_id) FROM stdin;
1	2016-08-23 18:02:55.067939+02	2016-08-23 18:02:55.068009+02	t	1
2	2016-08-23 18:04:46.837201+02	2016-08-23 18:04:46.83727+02	t	2
\.


--
-- Data for Name: garage_garage_bicycles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_garage_bicycles (id, garage_id, bicycle_id) FROM stdin;
2	2	9
\.


--
-- Name: garage_garage_bicycles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_garage_bicycles_id_seq', 2, true);


--
-- Name: garage_garage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_garage_id_seq', 2, true);


--
-- Data for Name: garage_garage_motorcycles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_garage_motorcycles (id, garage_id, motorcycle_id) FROM stdin;
1	2	2
\.


--
-- Name: garage_garage_motorcycles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_garage_motorcycles_id_seq', 1, true);


--
-- Data for Name: garage_motorcycle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_motorcycle (id, make_id, model_id, color, engine_size_id, production_year, style_id) FROM stdin;
1	2	2	RED	1	2015	1
2	1	17	1157	1	2016	1
\.


--
-- Name: garage_motorcycle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_motorcycle_id_seq', 2, true);


--
-- Data for Name: garage_motorengine; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_motorengine (id, cc) FROM stdin;
1	100
2	125
3	150
4	200
5	225
6	250
7	275
8	300
9	350
10	400
11	450
12	500
13	550
14	600
15	650
16	700
17	750
18	800
19	803
20	883
21	850
22	900
23	916
24	950
25	954
26	1000
27	1100
28	1150
29	1200
30	1250
31	1300
32	1400
33	1450
34	1500
35	1550
36	1600
37	1650
38	1700
39	1750
40	1800
41	1850
42	1900
43	1950
44	2000
\.


--
-- Name: garage_motorengine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_motorengine_id_seq', 1, false);


--
-- Data for Name: garage_motormake; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_motormake (id, brand) FROM stdin;
1	APRILIA
2	BMW
3	CAN-AM
4	DUCATI
5	HARLEY-DAVIDSON
6	HONDA
7	INDIAN
8	KTM
9	KAWASAKI
10	KYMCO
11	STAR MOTORCYCLES
12	SUZUKI
13	TRIUMPH
14	VICTORY
15	YAMAHA
16	Other
\.


--
-- Name: garage_motormake_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_motormake_id_seq', 1, false);


--
-- Data for Name: garage_motormodel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_motormodel (id, model, make_id) FROM stdin;
1	ATLANTIC	1
2	CAPONORD 	1
3	DORSODURO 	1
4	FALCO 	1
5	MANA 	1
6	MOJITO 	1
7	RS 	1
8	RST 	1
9	RSV 	1
10	RSV4	1
11	RXV	1
12	SCARABEO	1
13	SHIVER	1
14	SPORTCITY	1
15	SR	1
16	SXV	1
17	TUONO	1
18	C 600 	2
19	C 650 	2
20	C EVOLUTION	2
21	F 650 	2
22	F 700 	2
23	F 800 	2
24	G 450 	2
25	G 650 	2
26	HP2 	2
27	HP4 	2
28	K 1	2
29	K 100 	2
30	K 1100	2
31	K 1200	2
32	K 1300	2
33	K 1600 	2
34	K 75	2
35	R 100	2
36	R 1000	2
37	R 1100	2
38	R 1150	2
39	R 1200	2
40	R 60	2
41	R 65	2
42	R 75	2
43	R 80	2
44	R 850R	2
45	R 90	2
46	R NINE T	2
47	S 1000	2
48	XMOTO 	2
49	ASE 	3
50	COMMANDER 	3
51	DEFENDER	3
52	DS	3
53	FREEDOM TRAILER	3
54	MAVERICK	3
55	MX	3
56	OTHER	3
57	OUTLANDER	3
58	OUTLANDER 6X6 XT	3
59	OUTLANDER MAX	3
60	SONIC	3
61	SPYDER	3
62	748 MONO 	4
63	98	4
64	ALA ROSSA	4
65	DARK	4
66	DESMOSEDICI RR	4
67	DIAVEL	4
68	E 900	4
69	ELITE	4
70	F1	4
71	F3	4
72	FE 900	4
73	GT	4
74	HYPERMOTARD	4
75	HYPERSTRADA	4
76	JACKEL 150Z	4
77	MACH I 250	4
78	MH900	4
79	MIKE HAILWOOD REPLICA	4
80	MONSTER 	4
81	MULTISTRADA	4
82	PASO	4
83	PAUL SMART 1000	4
84	SCRAMBLER	4
85	SEBRING	4
86	SPORT	4
87	ST	4
88	STREET SCRAMBLER	4
89	STREETFIGHTER	4
90	SUPER SPORT	4
91	SUPERBIKE	4
92	TESTATRETTA	4
93	XDIAVEL	4
94	BAD BOY	5
95	BLACKLINE	5
96	BREAKOUT 	5
97	CUSTOM	5
98	CVO LIMITED	5
99	DUO GLIDE	5
100	DYNA	5
101	DYNA SPORT GLIDE	5
102	DYNA STREET BOB	5
103	DYNA WIDE GLIDE	5
104	ELECTRA GLIDE	5
105	FAT BOB	5
106	FAT BOY	5
107	FLATHEAD	5
108	FORTY-EIGHT 	5
109	FREEWHEELER	5
110	FXR	5
111	HERITAGE SOFTAIL	5
112	HERITAGE SPRINGER	5
113	HUMMER	5
114	HYDRA GLIDE	5
115	JD	5
116	KNUCKLEHEAD	5
117	LOW GLIDE	5
118	LOW RIDER	5
119	M45	5
120	M50	5
121	MT500 	5
122	NIGHT ROD	5
123	NIGHT TRAIN	5
124	NIGHTSTER	5
125	PANHEAD 	5
126	ROAD GLIDE	5
127	ROAD KING	5
128	ROADSTER	5
129	SERVI CAR	5
130	SEVENTY-TWO	5
131	SHOVELHEAD 	5
132	SIDE CAR	5
133	SOFTAIL	5
134	SPORTSTER	5
135	SPORTSTER 1000 	5
136	SPORTSTER 1100 	5
137	SPORTSTER 1200 	5
138	SPORTSTER 883	5
139	SPORTSTER RT 1200 	5
140	SPORTSTER XR1000	5
141	SPORTSTER XR1200	5
142	SPRINGER	5
143	SPRINT	5
144	STREET	5
145	STREET GLIDE	5
146	STREET ROD	5
147	STURGIS	5
148	SUPER GLIDE	5
149	SWITCH BLADE	5
150	SWITCHBACK	5
151	TOUR GLIDE	5
152	TRI GLIDE	5
153	V-ROD	5
154	XR750	5
155	919 BASE 	6
156	AFRICA TWIN 	6
157	ASCOT	6
158	ATC	6
159	ATVS	6
160	BIG RED	6
161	BIG RUCKUS	6
162	CB	6
163	CBR	6
164	CBX	6
165	CFR	6
166	CL	6
167	CM SERIES	6
168	CMX	6
169	CR SERIES	6
170	CRF	6
171	CRX250	6
172	CT 	6
173	CTX	6
174	CUSTOM	6
175	CX	6
176	DN-01 	6
177	DREAM 	6
178	ELITE 	6
179	ELSINORE 	6
180	FORZA 	6
181	FOURTRAX FOREMAN	6
182	FOURTRAX RANCHER	6
183	FOURTRAX RECON 	6
184	FOURTRAX RINCON	6
185	FURY 	6
186	GB 	6
187	GOLD WING	6
188	GROM	6
189	HAWK	6
190	HELIX	6
191	HONDAMATIC	6
192	INTERCEPTOR	6
193	INTERSTATE	6
194	MAGNA	6
195	METROPOLITAN	6
196	MONTESA	6
197	NC700	6
198	NM4	6
199	NSF	6
200	NSR 	6
201	NT700 VARADERO 	6
202	NX250 	6
203	NX650 DOMINATOR 	6
204	PACIFIC COAST 	6
205	PASSPORT	6
206	PCX 	6
207	PIONEER 	6
208	QA50 	6
209	RC 	6
210	REBEL 	6
211	REFLEX 	6
212	RUCKUS 	6
213	S90	6
214	SABRE	6
215	SCRAMBLER	6
216	SH150I 	6
217	SHADOW 	6
218	SILVER WING 	6
219	SL 	6
220	SPORTSMAN 4X4 	6
221	SPREE 	6
222	ST SERIES 	6
223	STATELINE 	6
224	SUPERHAWK 	6
225	TL	6
226	TRX 	6
227	VALKYRIE 	6
228	VF1000 	6
229	VFR 	6
230	VT 	6
231	VTX 	6
232	XL 	6
233	XR 	6
234	Z SERIES	6
235	CHIEF 	7
236	CHIEFTAIN	7
237	INDIAN 	7
238	MILLENIUM CHIEF 	7
239	SCOUT	7
240	SPIRIT	7
241	TOMAHAWK 	7
242	1190	8
243	125	8
244	1290	8
245	150	8
246	200	8
247	250	8
248	300	8
249	350	8
250	450	8
251	50	8
252	500	8
253	65	8
254	690	8
255	85	8
256	990	8
257	ADVENTURE 	8
258	DUKE 	8
259	ENDURO 	8
260	EXC 	8
261	MINI ADVENTURE 	8
262	MX 	8
263	MXC	8
264	RC 	8
265	SMR	8
266	SMT 	8
267	SUPER ENDURO	8
268	SUPERDUKE 	8
269	SUPERMOTO 	8
270	SX 	8
271	SX-F 	8
272	SXC 	8
273	XC 	8
274	XCF 	8
275	AR80-A1 	9
276	BAYOU 	9
277	BRUTE FORCE 	9
278	CONCOURS 	9
279	CSR 	9
280	ELIMINATOR 	9
281	ER-6N 	9
282	F 	9
283	G3SS	9
284	GPZ	9
285	JET SKI	9
286	JF 	9
287	JH	9
288	KDX	9
289	KE	9
290	KEF	9
291	KFX 	9
292	KL 	9
293	KLF	9
294	KLR 	9
295	KLX 	9
296	KRF 	9
297	KVF	9
298	KX 	9
299	KZ 	9
300	LTD 	9
301	MACH III 	9
302	MACH IV 	9
303	MD 90 	9
304	MULE 	9
305	NINJA 	9
306	NOMAD 	9
307	S2 TRIPLE 	9
308	SC 340 	9
309	SUPER SHERPA 	9
310	SX 	9
311	SXI PRO 	9
312	TANDEM SPORT 	9
313	TENGAI 	9
314	TERYN 	9
315	TERYX4 	9
316	TRIAL 	9
317	VERSYS 	9
318	VN 	9
319	VOYAGER 	9
320	VULCAN 	9
321	W 	9
322	X2 	9
323	XI PRO 	9
324	Z 	9
325	Z1 	9
326	Z1R 	9
327	ZEPHYR 	9
328	ZR-7 	9
329	ZRX 	9
330	ZXI 	9
331	ZZR 	9
332	AGILITY 	10
333	BET & WIN	10
334	COMPAGNO 	10
335	DOWNTOWN 	10
336	GRANDVISTA 	10
337	LIKE 	10
338	MOVIE 	10
339	MXU 	10
340	PEOPLE	10
341	QUANNON 	10
342	SENTO 	10
343	STING 	10
344	SUPER 8 	10
345	SUPER 9 	10
346	UXV 	10
347	VENOX	10
348	XCITING	10
349	YAGER	10
350	ZX50	10
351	BOLT 	11
352	RAIDER 	11
353	ROAD STAR	11
354	ROADLINER 	11
355	STRATOLINER	11
356	STRYKER 	11
357	VMAX 	11
358	230	12
359	250	12
360	650	12
361	750	12
362	AN 	12
363	B-KING 	12
364	BANDIT 	12
365	BOULEVARD 	12
366	BOULEVARD C109R 	12
367	BOULEVARD C50 	12
368	BOULEVARD C90 	12
369	BOULEVARD M109R 	12
370	BOULEVARD M50 	12
371	BOULEVARD M90 	12
372	BOULEVARD S40 	12
373	BOULEVARD S50 	12
374	BOULEVARD S83 	12
375	BURGMAN 	12
376	CALVACADE 	12
377	DL 	12
378	DR 	12
379	DR-Z 	12
380	EIGER	12
381	EIGER 400 	12
382	F50 	12
383	FA50 	12
384	FULLTIME LT-F 4WDFW 	12
385	GN 	12
386	GS 	12
387	GSX 	12
388	GSX-R 	12
389	GSX-S 	12
390	GT 	12
391	GW250 	12
392	GX 6 	12
393	GZ 	12
394	HAYABUSA 	12
395	HUSTLER X6 	12
396	INTRUDER 	12
397	JR 	12
398	KATANA 	12
399	KINGQUAD	12
400	LIMITED	12
401	LS 	12
402	MADURA 	12
403	MARAUDER 	12
404	OR 50	12
405	PE175E 	12
406	QUADSPORT 	12
407	RF	12
408	RG500 	12
409	RL250	12
410	RM-Z 	12
411	RM100	12
412	RM125 	12
413	RM250 	12
414	RM500E 	12
415	RM65 	12
416	RM85 	12
417	RMX250 	12
418	RMX450 	12
419	S40 CAFE RACER 	12
420	S83 	12
421	SFV650 	12
422	SP 	12
423	SV1000 	12
424	SV650 	12
425	T10 	12
426	T500 TITAN 	12
427	TL1000 	12
428	TL100RK 	12
429	TM125 	12
430	TM400 	12
431	TM75	12
432	TRACKER RV125K 	12
433	TU 	12
434	TU250 	12
435	V-STROM 	12
436	VX800 	12
437	VZ800 	12
438	Z 400 	12
439	ZX6R 	12
440	500	13
441	750	13
442	ADVENTURER 	13
443	AMERICA 	13
444	BONNEVILLE 	13
445	DAYTONA 	13
446	LEGEND 	13
447	NEW THUNDERBIRD 	13
448	ROCKET 	13
449	SCRAMBLER 	13
450	SPEED FOUR 	13
451	SPEED TRIPLE 	13
452	SPEEDMASTER 	13
453	SPRINT 	13
454	STREET TRIPLE 	13
455	SUPER III 	13
456	THRUXTON 	13
457	THUNDERBIRD 	13
458	TIGER 	13
459	TR6C	13
460	TRIDENT	13
461	TROPHY 	13
462	TT600 	13
463	BOARDWALK 	14
464	CROSS COUNTRY 	14
465	CROSS ROADS 	14
466	EMPULSE 	14
467	GUNNER 	14
468	HAMMER 	14
469	HARD-BALL 	14
470	HIGH BALL 	14
471	JACKPOT 	14
472	JUDGE	14
473	KINGPIN 	14
474	MAGNUM	14
475	OCTANE 	14
476	SIDE CAR 	14
477	V92 	14
478	VEGAS 	14
479	VISION 	14
480	1100	15
481	125	15
482	175	15
483	200 ELECTRIC 	15
484	232 LIMITED 	15
485	250	15
486	250F 	15
487	350 TWIN 	15
488	360	15
489	400 SECA 	15
490	426 F 	15
491	450	15
492	650	15
493	650 S	15
494	AR210 	15
495	BADGER 	15
496	BANSHEE 	15
497	BLASTER	15
498	BOLT 	15
499	BRUIN 	15
500	C3 	15
501	C500 S	15
502	CE50 	15
503	CHAMP 	15
504	CLASSIC 1100 	15
505	CS3 200 CC ELECTRIC 	15
506	CT-1 	15
507	CUSTOM 1100 	15
508	DRIVE 	15
509	DS6 	15
510	DT 	15
511	ET 	15
512	FAZER 	15
513	FJ-09 	15
514	FJ1100	15
515	FJ1300 	15
516	FJ600 	15
517	FJR1300 	15
518	FX 	15
519	FZ-07 	15
520	FZ-09 	15
521	FZ-S 	15
522	FZ1 	15
523	FZ16	15
524	FZ250 	15
525	FZ400 	15
526	FZ6 	15
527	FZ600 	15
528	FZ8 	15
529	FZR1000	15
530	FZR1800 	15
531	FZR600	15
532	FZX700	15
533	G-19	15
534	G16 A 	15
535	GENERATOR 	15
536	GP 	15
537	GRIZZLY 	15
538	GT80 	15
539	GTR125 	15
540	GTS1000	15
541	INVITER 	15
542	IT175	15
543	IT400 	15
544	IT425 	15
545	IT465 	15
546	JRP 1300A 	15
547	KODIAK 	15
548	MAJESTY 	15
549	MIDNIGHT 	15
550	MORPHOUS	15
551	MOTO 	15
552	MX100 	15
553	NEO 	15
554	PW50 ZINGER 	15
555	PW80 ZINGER	15
556	R5B 	15
557	RA1100	15
558	RA700 	15
559	RAGE 	15
560	RAIDER 	15
561	RAPTOR 	15
562	RD250 	15
563	RD400 	15
564	RI	15
565	ROAD STAR 	15
566	ROADLINER 	15
567	ROYAL STAR 	15
568	RS 	15
569	RS VECTOR 	15
570	RT100 	15
571	RX 100 	15
572	RX50 	15
573	RZ500 	15
574	SMAX 	15
575	SPECIAL 850 	15
576	SR 	15
577	STRATOLINER 	15
578	STRYKER 	15
579	SUPER TENERE 	15
580	TDM 850 	15
581	TMAX 	15
582	TT-R 250	15
583	TT-R110 	15
584	TT-R125 	15
585	TT-R225	15
586	TT-R230 	15
587	TT-R50 	15
588	TT-R90 	15
589	TW200 	15
590	TX500	15
591	TX750	15
592	TY250 	15
593	TY350 	15
594	TZ250 	15
595	TZ300 	15
596	TZR125 	15
597	V STAR 	15
598	VENTURE 	15
599	VIKING	15
600	VINO 	15
601	VIRAGO 	15
602	VMAX 	15
603	VT13CX 	15
604	VULCAN 1700 VOYAGER 	15
605	VX 	15
606	VX DELUXE 	15
607	VX110 CRUISER 	15
608	VX6SXSB 	15
609	VXS 	15
610	WARRIOR 	15
611	WR200	15
612	WR250	15
613	WR250F 	15
614	WR250R 	15
615	WR400F 	15
616	WR426F	15
617	WR450F 	15
618	XC200	15
619	XF50YR	15
620	XF50ZB C3	15
621	XJ550 	15
622	XJ600 	15
623	XJ650 	15
624	XJ700 	15
625	XJ750 	15
626	XJ900 	15
627	XL1200 	15
628	XL950 	15
629	XS1100 	15
630	XS400 	15
631	XS650 	15
632	XS750 	15
633	XSR 	15
634	XT225 	15
635	XT250 	15
636	XT350 	15
637	XT600 	15
638	XTREME 50 AMERICA 	15
639	XV1300 	15
640	XV13CT 	15
641	XV1700A 	15
642	XV17AMS-C RS 	15
643	XV17ASDB 	15
644	XV17ASYB	15
645	XV17AWW 	15
646	XV19 MXC 	15
647	XV19CSZB-C	15
648	XV19CTSZB-C 	15
649	XV19CXR-C 	15
650	XV19CYB 	15
651	XV19CZS-C 	15
652	XV19MSXR 	15
653	XV250D 	15
654	XV535 	15
655	XV535L	15
656	XV535T-C	15
657	XV650	15
658	XV700 	15
659	XV700CS 	15
660	XV750 	15
661	XV920 	15
662	XVZ1200 	15
663	XVZ1300 	15
664	YDS-6C 	15
665	YDS5 	15
666	YF60S 	15
667	YFZ 	15
668	YL2 	15
669	YR1 	15
670	YR3 	15
671	YT125L 	15
672	YT60N 	15
673	YTM 200E	15
674	YTM200EL	15
675	YX600 	15
676	YXZ 	15
677	YZ 	15
678	YZF 	15
679	ZUMA 	15
\.


--
-- Name: garage_motormodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_motormodel_id_seq', 1, false);


--
-- Data for Name: garage_motorstyle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY garage_motorstyle (id, style) FROM stdin;
1	Sportbike
2	Cruiser
3	Dirt Bike
4	Scooter
5	Sport Touring
6	Dual Sport
7	Touring
8	Mx
9	Moped
10	Standard
11	Competition
12	Super Moto
13	Custom
14	Classic / Vintage
15	Trike
\.


--
-- Name: garage_motorstyle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('garage_motorstyle_id_seq', 1, false);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: custom_user_customuser_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser
    ADD CONSTRAINT custom_user_customuser_email_key UNIQUE (email);


--
-- Name: custom_user_customuser_fb_id_bf3dbe04_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser
    ADD CONSTRAINT custom_user_customuser_fb_id_bf3dbe04_uniq UNIQUE (fb_id);


--
-- Name: custom_user_customuser_groups_customuser_id_56311c69_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser_groups
    ADD CONSTRAINT custom_user_customuser_groups_customuser_id_56311c69_uniq UNIQUE (customuser_id, group_id);


--
-- Name: custom_user_customuser_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser_groups
    ADD CONSTRAINT custom_user_customuser_groups_pkey PRIMARY KEY (id);


--
-- Name: custom_user_customuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser
    ADD CONSTRAINT custom_user_customuser_pkey PRIMARY KEY (id);


--
-- Name: custom_user_customuser_twitter_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser
    ADD CONSTRAINT custom_user_customuser_twitter_id_key UNIQUE (twitter_id);


--
-- Name: custom_user_customuser_user_permiss_customuser_id_797be134_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser_user_permissions
    ADD CONSTRAINT custom_user_customuser_user_permiss_customuser_id_797be134_uniq UNIQUE (customuser_id, permission_id);


--
-- Name: custom_user_customuser_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser_user_permissions
    ADD CONSTRAINT custom_user_customuser_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: custom_user_customuser_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_customuser
    ADD CONSTRAINT custom_user_customuser_username_key UNIQUE (username);


--
-- Name: custom_user_emailconfirmed_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_emailconfirmed
    ADD CONSTRAINT custom_user_emailconfirmed_pkey PRIMARY KEY (id);


--
-- Name: custom_user_emailconfirmed_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY custom_user_emailconfirmed
    ADD CONSTRAINT custom_user_emailconfirmed_user_id_key UNIQUE (user_id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: garage_bicycestyle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_bicycestyle
    ADD CONSTRAINT garage_bicycestyle_pkey PRIMARY KEY (id);


--
-- Name: garage_bicycle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_bicycle
    ADD CONSTRAINT garage_bicycle_pkey PRIMARY KEY (id);


--
-- Name: garage_bicyclemake_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_bicyclemake
    ADD CONSTRAINT garage_bicyclemake_pkey PRIMARY KEY (id);


--
-- Name: garage_garage_bicycles_garage_id_e98f4d65_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_garage_bicycles
    ADD CONSTRAINT garage_garage_bicycles_garage_id_e98f4d65_uniq UNIQUE (garage_id, bicycle_id);


--
-- Name: garage_garage_bicycles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_garage_bicycles
    ADD CONSTRAINT garage_garage_bicycles_pkey PRIMARY KEY (id);


--
-- Name: garage_garage_motorcycles_garage_id_cfb5e3f6_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_garage_motorcycles
    ADD CONSTRAINT garage_garage_motorcycles_garage_id_cfb5e3f6_uniq UNIQUE (garage_id, motorcycle_id);


--
-- Name: garage_garage_motorcycles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_garage_motorcycles
    ADD CONSTRAINT garage_garage_motorcycles_pkey PRIMARY KEY (id);


--
-- Name: garage_garage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_garage
    ADD CONSTRAINT garage_garage_pkey PRIMARY KEY (id);


--
-- Name: garage_garage_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_garage
    ADD CONSTRAINT garage_garage_user_id_key UNIQUE (user_id);


--
-- Name: garage_motorcycle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_motorcycle
    ADD CONSTRAINT garage_motorcycle_pkey PRIMARY KEY (id);


--
-- Name: garage_motorengine_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_motorengine
    ADD CONSTRAINT garage_motorengine_pkey PRIMARY KEY (id);


--
-- Name: garage_motormake_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_motormake
    ADD CONSTRAINT garage_motormake_pkey PRIMARY KEY (id);


--
-- Name: garage_motormodel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_motormodel
    ADD CONSTRAINT garage_motormodel_pkey PRIMARY KEY (id);


--
-- Name: garage_motorstyle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY garage_motorstyle
    ADD CONSTRAINT garage_motorstyle_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: custom_user_customuser_email_20b0f353_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX custom_user_customuser_email_20b0f353_like ON custom_user_customuser USING btree (email varchar_pattern_ops);


--
-- Name: custom_user_customuser_fb_id_bf3dbe04_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX custom_user_customuser_fb_id_bf3dbe04_like ON custom_user_customuser USING btree (fb_id varchar_pattern_ops);


--
-- Name: custom_user_customuser_groups_0e939a4f; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX custom_user_customuser_groups_0e939a4f ON custom_user_customuser_groups USING btree (group_id);


--
-- Name: custom_user_customuser_groups_721e74b0; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX custom_user_customuser_groups_721e74b0 ON custom_user_customuser_groups USING btree (customuser_id);


--
-- Name: custom_user_customuser_user_permissions_721e74b0; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX custom_user_customuser_user_permissions_721e74b0 ON custom_user_customuser_user_permissions USING btree (customuser_id);


--
-- Name: custom_user_customuser_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX custom_user_customuser_user_permissions_8373b171 ON custom_user_customuser_user_permissions USING btree (permission_id);


--
-- Name: custom_user_customuser_username_22f2b3d2_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX custom_user_customuser_username_22f2b3d2_like ON custom_user_customuser USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: garage_garage_bicycles_13c74ddd; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_garage_bicycles_13c74ddd ON garage_garage_bicycles USING btree (garage_id);


--
-- Name: garage_garage_bicycles_967d8d87; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_garage_bicycles_967d8d87 ON garage_garage_bicycles USING btree (bicycle_id);


--
-- Name: garage_garage_motorcycles_13c74ddd; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_garage_motorcycles_13c74ddd ON garage_garage_motorcycles USING btree (garage_id);


--
-- Name: garage_garage_motorcycles_16c4306d; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_garage_motorcycles_16c4306d ON garage_garage_motorcycles USING btree (motorcycle_id);


--
-- Name: garage_motorcycle_528292b4; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_motorcycle_528292b4 ON garage_motorcycle USING btree (style_id);


--
-- Name: garage_motorcycle_engine_size_id_dc04cbec_uniq; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_motorcycle_engine_size_id_dc04cbec_uniq ON garage_motorcycle USING btree (engine_size_id);


--
-- Name: garage_motorcycle_make_id_fe14eee0_uniq; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_motorcycle_make_id_fe14eee0_uniq ON garage_motorcycle USING btree (make_id);


--
-- Name: garage_motorcycle_model_id_edb11da0_uniq; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_motorcycle_model_id_edb11da0_uniq ON garage_motorcycle USING btree (model_id);


--
-- Name: garage_motormodel_14dd5396; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX garage_motormodel_14dd5396 ON garage_motormodel USING btree (make_id);


--
-- Name: auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token_user_id_35299eff_fk_custom_user_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_custom_user_customuser_id FOREIGN KEY (user_id) REFERENCES custom_user_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_custom_permission_id_7d0938cd_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_customuser_user_permissions
    ADD CONSTRAINT custom_user_custom_permission_id_7d0938cd_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_customuser_group_group_id_bdb860ae_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_customuser_groups
    ADD CONSTRAINT custom_user_customuser_group_group_id_bdb860ae_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_customuser_id_39e4b4a7_fk_custom_user_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_customuser_groups
    ADD CONSTRAINT custom_user_customuser_id_39e4b4a7_fk_custom_user_customuser_id FOREIGN KEY (customuser_id) REFERENCES custom_user_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_customuser_id_e46769ac_fk_custom_user_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_customuser_user_permissions
    ADD CONSTRAINT custom_user_customuser_id_e46769ac_fk_custom_user_customuser_id FOREIGN KEY (customuser_id) REFERENCES custom_user_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: custom_user_email_user_id_10d2c874_fk_custom_user_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY custom_user_emailconfirmed
    ADD CONSTRAINT custom_user_email_user_id_10d2c874_fk_custom_user_customuser_id FOREIGN KEY (user_id) REFERENCES custom_user_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_content_type_id_c4bce8eb_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_content_type_id_c4bce8eb_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk_custom_user_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_custom_user_customuser_id FOREIGN KEY (user_id) REFERENCES custom_user_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_bicycle_make_id_17006d42_fk_garage_bicyclemake_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_bicycle
    ADD CONSTRAINT garage_bicycle_make_id_17006d42_fk_garage_bicyclemake_id FOREIGN KEY (make_id) REFERENCES garage_bicyclemake(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_bicycle_style_id_777ebbfd_fk_garage_bicycestyle_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_bicycle
    ADD CONSTRAINT garage_bicycle_style_id_777ebbfd_fk_garage_bicycestyle_id FOREIGN KEY (style_id) REFERENCES garage_bicycestyle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_garage_bicycles_bicycle_id_e37ac9bd_fk_garage_bicycle_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_garage_bicycles
    ADD CONSTRAINT garage_garage_bicycles_bicycle_id_e37ac9bd_fk_garage_bicycle_id FOREIGN KEY (bicycle_id) REFERENCES garage_bicycle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_garage_bicycles_garage_id_3202fcc9_fk_garage_garage_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_garage_bicycles
    ADD CONSTRAINT garage_garage_bicycles_garage_id_3202fcc9_fk_garage_garage_id FOREIGN KEY (garage_id) REFERENCES garage_garage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_garage_mo_motorcycle_id_2aeb41e8_fk_garage_motorcycle_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_garage_motorcycles
    ADD CONSTRAINT garage_garage_mo_motorcycle_id_2aeb41e8_fk_garage_motorcycle_id FOREIGN KEY (motorcycle_id) REFERENCES garage_motorcycle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_garage_motorcycle_garage_id_3a018d62_fk_garage_garage_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_garage_motorcycles
    ADD CONSTRAINT garage_garage_motorcycle_garage_id_3a018d62_fk_garage_garage_id FOREIGN KEY (garage_id) REFERENCES garage_garage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_garage_user_id_689e5b3f_fk_custom_user_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_garage
    ADD CONSTRAINT garage_garage_user_id_689e5b3f_fk_custom_user_customuser_id FOREIGN KEY (user_id) REFERENCES custom_user_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_motorcy_engine_size_id_dc04cbec_fk_garage_motorengine_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motorcycle
    ADD CONSTRAINT garage_motorcy_engine_size_id_dc04cbec_fk_garage_motorengine_id FOREIGN KEY (engine_size_id) REFERENCES garage_motorengine(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_motorcycle_make_id_fe14eee0_fk_garage_motormake_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motorcycle
    ADD CONSTRAINT garage_motorcycle_make_id_fe14eee0_fk_garage_motormake_id FOREIGN KEY (make_id) REFERENCES garage_motormake(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_motorcycle_model_id_edb11da0_fk_garage_motormodel_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motorcycle
    ADD CONSTRAINT garage_motorcycle_model_id_edb11da0_fk_garage_motormodel_id FOREIGN KEY (model_id) REFERENCES garage_motormodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_motorcycle_style_id_cc8c00c2_fk_garage_motorstyle_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motorcycle
    ADD CONSTRAINT garage_motorcycle_style_id_cc8c00c2_fk_garage_motorstyle_id FOREIGN KEY (style_id) REFERENCES garage_motorstyle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: garage_motormodel_make_id_16f824d4_fk_garage_motormake_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY garage_motormodel
    ADD CONSTRAINT garage_motormodel_make_id_16f824d4_fk_garage_motormake_id FOREIGN KEY (make_id) REFERENCES garage_motormake(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

