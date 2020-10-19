<?php
$config->installed       = true;
$config->debug           = false;
$config->requestType     = 'GET';
$config->db->host        = '{{.pod__oprep__port__mysql__lan_addr}}';
$config->db->port        = '{{.pod__oprep__port__mysql__host_port}}';
$config->db->name        = 'dbaction';
$config->db->user        = 'dbuser';
$config->db->password    = '{{.app__zentao_pms_x1__option__cfg__sysinner_mysql__db_auth}}';
$config->db->prefix      = 'zt_';
$config->webRoot         = getWebRoot();
$config->default->lang   = 'en';

