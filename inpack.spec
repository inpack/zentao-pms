[project]
name = zentao-pms
version = 9.6.2
vendor = zentao.net
homepage = http://www.zentao.net
groups = app/co,app/dev
description = Project management

%build

cd {{.inpack__pack_dir}}/deps

if [ ! -f "ZenTaoPMS.{{.project__version}}.zip" ]; then
    wget http://dl.cnezsoft.com/zentao/{{.project__version}}/ZenTaoPMS.{{.project__version}}.zip
fi
if [ ! -d "zentaopms" ]; then
    unzip ZenTaoPMS.{{.project__version}}.zip
fi

rsync -av zentaopms/* {{.buildroot}}/
rm -rf zentaopms
mkdir -p {{.buildroot}}/misc/zentaopms

cd {{.inpack__pack_dir}}

cp -rp misc/zentaopms/config__my.php {{.buildroot}}/misc/zentaopms/config__my.php
cp -rp misc/zentaopms/module__install__view__step2.html.php {{.buildroot}}/misc/zentaopms/module__install__view__step2.html.php
cp -rp misc/zentaopms/www__index.php {{.buildroot}}/misc/zentaopms/www__index.php
install misc/zentaopms/www__index.php {{.buildroot}}/www/index.php

%files

