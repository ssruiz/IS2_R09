--Creacion de base de datos
DROP DATABASE if exists "IS2_R09_1";

CREATE DATABASE "IS2_R09_1"
  WITH OWNER = meliam
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'es_ES.UTF-8'
       LC_CTYPE = 'es_ES.UTF-8'
       CONNECTION LIMIT = -1;

-- Table: django_migrations
CREATE TABLE django_migrations
(
  id serial NOT NULL,
  app character varying(255) NOT NULL,
  name character varying(255) NOT NULL,
  applied timestamp with time zone NOT NULL,
  CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE django_migrations
  OWNER TO meliam;

-- Table: django_content_type
CREATE TABLE django_content_type
(
  id serial NOT NULL,
  name character varying(100) NOT NULL,
  app_label character varying(100) NOT NULL,
  model character varying(100) NOT NULL,
  CONSTRAINT django_content_type_pkey PRIMARY KEY (id),
  CONSTRAINT django_content_type_app_label_3ec8c61c_uniq UNIQUE (app_label, model)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE django_content_type
  OWNER TO meliam;

-- Table: django_admin_log
CREATE TABLE django_admin_log
(
  id serial NOT NULL,
  action_time timestamp with time zone NOT NULL,
  object_id text,
  object_repr character varying(200) NOT NULL,
  action_flag smallint NOT NULL,
  change_message text NOT NULL,
  content_type_id integer,
  user_id integer NOT NULL,
  CONSTRAINT django_admin_log_pkey PRIMARY KEY (id),
  CONSTRAINT django_admin_content_type_id_5151027a_fk_django_content_type_id FOREIGN KEY (content_type_id)
      REFERENCES django_content_type (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT django_admin_log_user_id_1c5f563_fk_auth_user_id FOREIGN KEY (user_id)
      REFERENCES auth_user (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT django_admin_log_action_flag_check CHECK (action_flag >= 0)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE django_admin_log
  OWNER TO meliam;

-- Index: django_admin_log_417f1b1c
CREATE INDEX django_admin_log_417f1b1c
  ON django_admin_log
  USING btree
  (content_type_id);

-- Index: django_admin_log_e8701ad4
CREATE INDEX django_admin_log_e8701ad4
  ON django_admin_log
  USING btree
  (user_id);

-- Table: auth_user_user_permissions
CREATE TABLE auth_user_user_permissions
(
  id serial NOT NULL,
  user_id integer NOT NULL,
  permission_id integer NOT NULL,
  CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id),
  CONSTRAINT auth_user_user_per_permission_id_3d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id)
      REFERENCES auth_permission (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id FOREIGN KEY (user_id)
      REFERENCES auth_user (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE auth_user_user_permissions
  OWNER TO meliam;

-- Index: auth_user_user_permissions_8373b171
CREATE INDEX auth_user_user_permissions_8373b171
  ON auth_user_user_permissions
  USING btree
  (permission_id);

-- Index: auth_user_user_permissions_e8701ad4
CREATE INDEX auth_user_user_permissions_e8701ad4
  ON auth_user_user_permissions
  USING btree
  (user_id);

-- Table: auth_user_groups
CREATE TABLE auth_user_groups
(
  id serial NOT NULL,
  user_id integer NOT NULL,
  group_id integer NOT NULL,
  CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id),
  CONSTRAINT auth_user_groups_group_id_30a071c9_fk_auth_group_id FOREIGN KEY (group_id)
      REFERENCES auth_group (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT auth_user_groups_user_id_24702650_fk_auth_user_id FOREIGN KEY (user_id)
      REFERENCES auth_user (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE auth_user_groups
  OWNER TO meliam;

-- Index: auth_user_groups_0e939a4f
CREATE INDEX auth_user_groups_0e939a4f
  ON auth_user_groups
  USING btree
  (group_id);

-- Index: auth_user_groups_e8701ad4
CREATE INDEX auth_user_groups_e8701ad4
  ON auth_user_groups
  USING btree
  (user_id);

-- Table: auth_user
CREATE TABLE auth_user
(
  id serial NOT NULL,
  password character varying(128) NOT NULL,
  last_login timestamp with time zone NOT NULL,
  is_superuser boolean NOT NULL,
  username character varying(30) NOT NULL,
  first_name character varying(30) NOT NULL,
  last_name character varying(30) NOT NULL,
  email character varying(75) NOT NULL,
  is_staff boolean NOT NULL,
  is_active boolean NOT NULL,
  date_joined timestamp with time zone NOT NULL,
  CONSTRAINT auth_user_pkey PRIMARY KEY (id),
  CONSTRAINT auth_user_username_key UNIQUE (username)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE auth_user
  OWNER TO meliam;

-- Index: auth_user_username_94b8aae_like
CREATE INDEX auth_user_username_94b8aae_like
  ON auth_user
  USING btree
  (username COLLATE pg_catalog."default" varchar_pattern_ops);

-- Table: auth_permission
CREATE TABLE auth_permission
(
  id serial NOT NULL,
  name character varying(50) NOT NULL,
  content_type_id integer NOT NULL,
  codename character varying(100) NOT NULL,
  CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
  CONSTRAINT auth_permiss_content_type_id_51277a81_fk_django_content_type_id FOREIGN KEY (content_type_id)
      REFERENCES django_content_type (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE auth_permission
  OWNER TO meliam;

-- Index: auth_permission_417f1b1c
CREATE INDEX auth_permission_417f1b1c
  ON auth_permission
  USING btree
  (content_type_id);

-- Table: auth_group_permissions
CREATE TABLE auth_group_permissions
(
  id serial NOT NULL,
  group_id integer NOT NULL,
  permission_id integer NOT NULL,
  CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
  CONSTRAINT auth_group_permiss_permission_id_23962d04_fk_auth_permission_id FOREIGN KEY (permission_id)
      REFERENCES auth_permission (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT auth_group_permissions_group_id_58c48ba9_fk_auth_group_id FOREIGN KEY (group_id)
      REFERENCES auth_group (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE auth_group_permissions
  OWNER TO meliam;

-- Index: auth_group_permissions_0e939a4f
CREATE INDEX auth_group_permissions_0e939a4f
  ON auth_group_permissions
  USING btree
  (group_id);

-- Index: auth_group_permissions_8373b171
CREATE INDEX auth_group_permissions_8373b171
  ON auth_group_permissions
  USING btree
  (permission_id);

-- Table: auth_group
CREATE TABLE auth_group
(
  id serial NOT NULL,
  name character varying(80) NOT NULL,
  CONSTRAINT auth_group_pkey PRIMARY KEY (id),
  CONSTRAINT auth_group_name_key UNIQUE (name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE auth_group
  OWNER TO meliam;

-- Index: auth_group_name_331666e8_like
CREATE INDEX auth_group_name_331666e8_like
  ON auth_group
  USING btree
  (name COLLATE pg_catalog."default" varchar_pattern_ops);

-- Table: "Usuario_usuario"
CREATE TABLE "Usuario_usuario"
(
  id serial NOT NULL,
  user_id integer NOT NULL,
  foto character varying(100) NOT NULL,
  telefono character varying(30) NOT NULL,
  CONSTRAINT "Usuario_usuario_pkey" PRIMARY KEY (id),
  CONSTRAINT "Usuario_usuario_user_id_key" UNIQUE (user_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Usuario_usuario"
  OWNER TO meliam;

-- Table: "Proyecto_proyecto"
CREATE TABLE "Proyecto_proyecto"
(
  id serial NOT NULL,
  nombre character varying(30) NOT NULL,
  descripcion text NOT NULL,
  cliente_id integer,
  fecha_creacion date NOT NULL,
  fecha_inicio date,
  fecha_fin date,
  estado character varying(10) NOT NULL,
  sprint_actual character varying(30),
  CONSTRAINT "Proyecto_proyecto_pkey" PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Proyecto_proyecto"
  OWNER TO meliam;

-- Index: "Proyecto_proyecto_cliente_id"
CREATE INDEX "Proyecto_proyecto_cliente_id"
  ON "Proyecto_proyecto"
  USING btree
  (cliente_id);

-- Table: "Proyecto_equipo"
CREATE TABLE "Proyecto_equipo"
(
  id serial NOT NULL,
  proyect_id integer NOT NULL,
  miembro_id integer NOT NULL,
  rol_id integer NOT NULL,
  CONSTRAINT "Proyecto_equipo_pkey" PRIMARY KEY (id),
  CONSTRAINT "Proyecto_equipo_miembro_id_fkey" FOREIGN KEY (miembro_id)
      REFERENCES auth_user (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "Proyecto_equipo_proyect_id_fkey" FOREIGN KEY (proyect_id)
      REFERENCES "Proyecto_proyecto" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "Proyecto_equipo_rol_id_fkey" FOREIGN KEY (rol_id)
      REFERENCES auth_group (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Proyecto_equipo"
  OWNER TO meliam;

-- Index: "Proyecto_equipo_miembro_id"
CREATE INDEX "Proyecto_equipo_miembro_id"
  ON "Proyecto_equipo"
  USING btree
  (miembro_id);

-- Index: "Proyecto_equipo_proyect_id"
CREATE INDEX "Proyecto_equipo_proyect_id"
  ON "Proyecto_equipo"
  USING btree
  (proyect_id);

-- Index: "Proyecto_equipo_rol_id"
CREATE INDEX "Proyecto_equipo_rol_id"
  ON "Proyecto_equipo"
  USING btree
  (rol_id);

-- Table: "Proyecto_proyecto_flujos"
CREATE TABLE "Proyecto_proyecto_flujos"
(
  id serial NOT NULL,
  proyecto_id integer NOT NULL,
  flujo_id integer NOT NULL,
  CONSTRAINT "Proyecto_proyecto_flujos_pkey" PRIMARY KEY (id),
  CONSTRAINT flujo_id_refs_id_e1db9449 FOREIGN KEY (flujo_id)
      REFERENCES "Flujo_flujo" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT proyecto_id_refs_id_e57411a8 FOREIGN KEY (proyecto_id)
      REFERENCES "Proyecto_proyecto" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "Proyecto_proyecto_flujos_proyecto_id_flujo_id_key" UNIQUE (proyecto_id, flujo_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Proyecto_proyecto_flujos"
  OWNER TO meliam;

-- Index: "Proyecto_proyecto_flujos_flujo_id"
CREATE INDEX "Proyecto_proyecto_flujos_flujo_id"
  ON "Proyecto_proyecto_flujos"
  USING btree
  (flujo_id);

-- Index: "Proyecto_proyecto_flujos_proyecto_id"
CREATE INDEX "Proyecto_proyecto_flujos_proyecto_id"
  ON "Proyecto_proyecto_flujos"
  USING btree
  (proyecto_id);

-- Table: "US_us_usuario_asignado"
CREATE TABLE "US_us_usuario_asignado"
(
  id serial NOT NULL,
  us_id integer NOT NULL,
  user_id integer NOT NULL,
  CONSTRAINT "US_us_usuario_asignado_pkey" PRIMARY KEY (id),
  CONSTRAINT us_id_refs_id_d1ac6be8 FOREIGN KEY (us_id)
      REFERENCES "US_us" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "US_us_usuario_asignado_us_id_user_id_key" UNIQUE (us_id, user_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "US_us_usuario_asignado"
  OWNER TO meliam;

-- Index: "US_us_usuario_asignado_us_id"
CREATE INDEX "US_us_usuario_asignado_us_id"
  ON "US_us_usuario_asignado"
  USING btree
  (us_id);

-- Index: "US_us_usuario_asignado_user_id"
CREATE INDEX "US_us_usuario_asignado_user_id"
  ON "US_us_usuario_asignado"
  USING btree
  (user_id);

-- Table: "US_us_comentarios"
CREATE TABLE "US_us_comentarios"
(
  id serial NOT NULL,
  us_id integer NOT NULL,
  comentario_id integer NOT NULL,
  CONSTRAINT "US_us_comentarios_pkey" PRIMARY KEY (id),
  CONSTRAINT comentario_id_refs_id_f463762e FOREIGN KEY (comentario_id)
      REFERENCES "Comentario_comentario" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT us_id_refs_id_45e2263e FOREIGN KEY (us_id)
      REFERENCES "US_us" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "US_us_comentarios_us_id_comentario_id_key" UNIQUE (us_id, comentario_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "US_us_comentarios"
  OWNER TO meliam;

-- Index: "US_us_comentarios_comentario_id"
CREATE INDEX "US_us_comentarios_comentario_id"
  ON "US_us_comentarios"
  USING btree
  (comentario_id);

-- Index: "US_us_comentarios_us_id"
CREATE INDEX "US_us_comentarios_us_id"
  ON "US_us_comentarios"
  USING btree
  (us_id);

-- Table: "US_us_adjuntos"
CREATE TABLE "US_us_adjuntos"
(
  id serial NOT NULL,
  us_id integer NOT NULL,
  adjunto_id integer NOT NULL,
  CONSTRAINT "US_us_adjuntos_pkey" PRIMARY KEY (id),
  CONSTRAINT adjunto_id_refs_id_fe2111c9 FOREIGN KEY (adjunto_id)
      REFERENCES "Adjunto_adjunto" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT us_id_refs_id_1e7b4f64 FOREIGN KEY (us_id)
      REFERENCES "US_us" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "US_us_adjuntos_us_id_adjunto_id_key" UNIQUE (us_id, adjunto_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "US_us_adjuntos"
  OWNER TO meliam;

-- Index: "US_us_adjuntos_adjunto_id"
CREATE INDEX "US_us_adjuntos_adjunto_id"
  ON "US_us_adjuntos"
  USING btree
  (adjunto_id);

-- Index: "US_us_adjuntos_us_id"
CREATE INDEX "US_us_adjuntos_us_id"
  ON "US_us_adjuntos"
  USING btree
  (us_id);

-- Table: "US_us"
CREATE TABLE "US_us"
(
  id serial NOT NULL,
  nombre character varying(30) NOT NULL,
  descripcion text NOT NULL,
  tiempo_estimado integer,
  tiempo_trabajado integer,
  prioridad character varying(1) NOT NULL,
  proyecto_asociado_id integer,
  sprint_asociado_id integer,
  CONSTRAINT "US_us_pkey" PRIMARY KEY (id),
  CONSTRAINT "US_us_proyecto_asociado_id_fkey" FOREIGN KEY (proyecto_asociado_id)
      REFERENCES "Proyecto_proyecto" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT sprint_asociado_id_refs_id_93adf02d FOREIGN KEY (sprint_asociado_id)
      REFERENCES "Sprint_sprint" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "US_us"
  OWNER TO meliam;

-- Index: "US_us_proyecto_asociado_id"
CREATE INDEX "US_us_proyecto_asociado_id"
  ON "US_us"
  USING btree
  (proyecto_asociado_id);

-- Index: "US_us_sprint_asociado_id"
CREATE INDEX "US_us_sprint_asociado_id"
  ON "US_us"
  USING btree
  (sprint_asociado_id);

-- Table: "Sprint_sprint"
CREATE TABLE "Sprint_sprint"
(
  id serial NOT NULL,
  nombre character varying(30) NOT NULL,
  descripcion text NOT NULL,
  fecha_inicio date,
  fecha_fin date,
  tiempo_estimado integer,
  tiempo_total integer,
  proyect_id integer,
  CONSTRAINT "Sprint_sprint_pkey" PRIMARY KEY (id),
  CONSTRAINT "Sprint_sprint_proyect_id_fkey" FOREIGN KEY (proyect_id)
      REFERENCES "Proyecto_proyecto" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "Sprint_sprint_tiempo_estimado_check" CHECK (tiempo_estimado >= 0),
  CONSTRAINT "Sprint_sprint_tiempo_total_check" CHECK (tiempo_total >= 0)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Sprint_sprint"
  OWNER TO meliam;

-- Index: "Sprint_sprint_proyect_id"
CREATE INDEX "Sprint_sprint_proyect_id"
  ON "Sprint_sprint"
  USING btree
  (proyect_id);

-- Table: "Flujo_kanban"
CREATE TABLE "Flujo_kanban"
(
  id serial NOT NULL,
  fluj_id integer,
  actividad_id integer,
  us_id integer,
  estado character varying(2),
  prioridad character varying(1),
  CONSTRAINT "Flujo_kanban_pkey" PRIMARY KEY (id),
  CONSTRAINT "Flujo_kanban_actividad_id_fkey" FOREIGN KEY (actividad_id)
      REFERENCES "Flujo_actividad" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "Flujo_kanban_fluj_id_fkey" FOREIGN KEY (fluj_id)
      REFERENCES "Flujo_flujo" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT us_id_refs_id_c1a46202 FOREIGN KEY (us_id)
      REFERENCES "US_us" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Flujo_kanban"
  OWNER TO meliam;

-- Index: "Flujo_kanban_actividad_id"
CREATE INDEX "Flujo_kanban_actividad_id"
  ON "Flujo_kanban"
  USING btree
  (actividad_id);

-- Index: "Flujo_kanban_fluj_id"
CREATE INDEX "Flujo_kanban_fluj_id"
  ON "Flujo_kanban"
  USING btree
  (fluj_id);

-- Index: "Flujo_kanban_us_id"
CREATE INDEX "Flujo_kanban_us_id"
  ON "Flujo_kanban"
  USING btree
  (us_id);

-- Table: "Flujo_flujo_actividades"
CREATE TABLE "Flujo_flujo_actividades"
(
  id serial NOT NULL,
  flujo_id integer NOT NULL,
  actividad_id integer NOT NULL,
  CONSTRAINT "Flujo_flujo_actividades_pkey" PRIMARY KEY (id),
  CONSTRAINT "Flujo_flujo_actividades_actividad_id_fkey" FOREIGN KEY (actividad_id)
      REFERENCES "Flujo_actividad" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT flujo_id_refs_id_8a93253d FOREIGN KEY (flujo_id)
      REFERENCES "Flujo_flujo" (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT "Flujo_flujo_actividades_flujo_id_actividad_id_key" UNIQUE (flujo_id, actividad_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Flujo_flujo_actividades"
  OWNER TO meliam;

-- Index: "Flujo_flujo_actividades_actividad_id"
CREATE INDEX "Flujo_flujo_actividades_actividad_id"
  ON "Flujo_flujo_actividades"
  USING btree
  (actividad_id);

-- Index: "Flujo_flujo_actividades_flujo_id"
CREATE INDEX "Flujo_flujo_actividades_flujo_id"
  ON "Flujo_flujo_actividades"
  USING btree
  (flujo_id);

-- Table: "Flujo_flujo"
CREATE TABLE "Flujo_flujo"
(
  id serial NOT NULL,
  nombre character varying(30) NOT NULL,
  CONSTRAINT "Flujo_flujo_pkey" PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Flujo_flujo"
  OWNER TO meliam;

-- Table: "Flujo_actividad"
CREATE TABLE "Flujo_actividad"
(
  id serial NOT NULL,
  nombre character varying(30) NOT NULL,
  "order" integer NOT NULL,
  CONSTRAINT "Flujo_actividad_pkey" PRIMARY KEY (id),
  CONSTRAINT "Flujo_actividad_order_check" CHECK ("order" >= 0)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Flujo_actividad"
  OWNER TO meliam;

-- Table: "Comentario_comentario"
CREATE TABLE "Comentario_comentario"
(
  id serial NOT NULL,
  nombre character varying(30) NOT NULL,
  comentario text NOT NULL,CREATE TABLE "Adjunto_adjunto"
(
  id serial NOT NULL,
  nombre text NOT NULL,
  descripcion text NOT NULL,
  version text NOT NULL,
  comentario_commit text NOT NULL,
  archivo character varying(100) NOT NULL,
  CONSTRAINT "Adjunto_adjunto_pkey" PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Adjunto_adjunto"
  OWNER TO meliam;

  fecha_creacion date NOT NULL,
  fecha_ultima_mod date NOT NULL,
  CONSTRAINT "Comentario_comentario_pkey" PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Comentario_comentario"
  OWNER TO meliam;

-- Table: "Adjunto_adjunto"
CREATE TABLE "Adjunto_adjunto"
(
  id serial NOT NULL,
  nombre text NOT NULL,
  descripcion text NOT NULL,
  version text NOT NULL,
  comentario_commit text NOT NULL,
  archivo character varying(100) NOT NULL,
  CONSTRAINT "Adjunto_adjunto_pkey" PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Adjunto_adjunto"
  OWNER TO meliam;

