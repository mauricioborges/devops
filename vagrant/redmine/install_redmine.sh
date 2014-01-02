#!/usr/bin/env bash

# Are we punching above our weight?
if [ "$EUID" -ne "0" ]; then
    echo '- The bootstrap script must be run as root!'
    exit 1
fi


REDMINE_VERSION=redmine-2.4.2-0
BITNAMI_PACKAGE="bitnami-$REDMINE_VERSION-linux-installer.run"
install_dir=/opt/$REDMINE_VERSION
plugins_dir=$install_dir/apps/redmine/htdocs/plugins
redmine_htdocs_dir=$install_dir/apps/redmine/htdocs
require_restart=false

echo "Installing Bitnami Package $REDMINE_VERSION"


if [ ! -f /vagrant/$BITNAMI_PACKAGE ];then
    echo 'Downloading package from Bitnami ...'
    wget http://bitnami.com/redirect/to/29280/$BITNAMI_PACKAGE
else
    echo 'Copying package from shared folder ...'
    cp /vagrant/$BITNAMI_PACKAGE ./
fi 
echo 'Installation will run now... wait a bit ... '
chmod +x $BITNAMI_PACKAGE
./$BITNAMI_PACKAGE --mode unattended --installer-language en --prefix $install_dir --base_user_name "Mauricio Borges" --base_mail ms55042@getnet.com.br --base_user admin --base_password getnet123 --redmine_language pt_br --debugtrace redmine_install.log --apache_server_port 9150 --apache_server_ssl_port 9151 --mysql_port 3336 --mysql_password "S@9842a2Y0" --smtp_enable 1 --debuglevel 4 

status=$?
if [ $status -ne 0 ]; then
   echo "Instalation failed with error code $status. Exiting ... "
fi

echo 'Removing installation package ... '
rm ./$BITNAMI_PACKAGE



#INSTALL REDMINE_BACKLOGS http://www.redminebacklogs.net/en/installation.html

backlogs_tag=v1.0.6
echo "Installing redmine backlogs version $backlogs_tag"

apt-get install make unzip mercurial

cd $install_dir

require_restart=true

#INSTALL REDMINE PROJECTS SECTIONS
cd $plugins_dir
svn co http://subversion.andriylesyuk.com/project-sections project_section
require_restart=true

#INSTALL REDMINE PROGRESSIVE PROJECTS https://github.com/stgeneral/redmine-progressive-projects-list
cd $plugins_dir
git clone  https://github.com/stgeneral/redmine-progressive-projects-list progressive_projects_list
require_restart=true


#INSTALL THEMES 
cd $themes_dir 

git clone http://github.com/ChrisMcKee/redmine-themes/
wget http://redminecrm.com/license_manager/7644/a1-1_1_2.zip 
unzip a1.zip
rm a1*.zip
git clone http://github.com/stgeneral/redmine-progressive-theme.git

#INSTALL ISSUE TEMPLATES http://www.r-labs.org/projects/issue-template/wiki/About_en
cd $plugins_dir 

hg clone https://hg@bitbucket.org/akiko_pusu/redmine_issue_templates

# removed simplecov from plugin


cd $redmine_htdocs_dir dir
rake redmine:plugins:migrate --trace
require_restart=true


#INSTALL REDSHARE (share issue with other ppl)

cd $plugins_dir

git clone https://github.com/jzaiat/redshares
cd $redmine_htdocs_dir

rake redmine:plugins:migrate RAILS_ENV=production

#INSTALL RELEASE NOTES PLUGIN   https://github.com/hdgarrood/redmine_release_notes

cd $plugins_dir
git clone https://github.com/hdgarrood/redmine_release_notes


#INSTALL README plugin

cd $plugins_dir
git clone git://github.com/simeji/readme_at_repositories.git

require_restart=true
