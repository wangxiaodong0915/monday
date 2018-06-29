CREATE TABLE {{table_name }}
({% for col in col_lists %}
    {{col[1]}} {{col[2]}},{% endfor %}
    WXD_DATE DATE
);
COMMENT ON TABLE {{table_name}} IS '{{table_name_comment}}';
{% for col in col_lists %}COMMENT ON COLUMN "{{table_name}}"."{{col[1]}}" is '{{col[0]}}';
{% endfor %}

