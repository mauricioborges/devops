#!/usr/bin/env bash

# Are we punching above our weight?
if [ "$EUID" -ne "0" ]; then
    echo '- The bootstrap script must be run as root!'
    exit 1
fi


export REDMINE_VERSION=redmine-2.4.2-0
export BITNAMI_PACKAGE="bitnami-$REDMINE_VERSION-linux-installer.run"
export install_dir=/opt/$REDMINE_VERSION
export plugins_dir=$install_dir/apps/redmine/htdocs/plugins
export redmine_htdocs_dir=$install_dir/apps/redmine/htdocs
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
./$BITNAMI_PACKAGE --mode unattended --installer-language en --prefix $install_dir --base_user_name "Mauricio Borges" --base_mail ms55042@getnet.com.br --base_user admin --base_password getnet123 --redmine_language pt_br --apache_server_port 9150 --apache_server_ssl_port 9151 --mysql_port 3336 --mysql_password "S@9842a2Y0" --smtp_enable 1 --debuglevel 4 

#status=$?
#if [ $status -ne 0 ]; then
#   echo "Instalation failed with error code $status. Exiting ... "
#fi

echo 'Removing installation package ... '
rm ./$BITNAMI_PACKAGE

#http://wiki.bitnami.com/Native_Installers_Quick_Start_Guide#Debian-like_distribution_%28Debian.2c_Ubuntu.2c_etc%29
#upstart
#cp $install_dir/ctlscript.sh /etc/init.d/bitnami-redmine
#update-rc.d -f bitnami-redmine start 80 2 3 4 5 . stop 30 0 1 6 .

# PREPARE FOR PLUGINS

apt-get -y install make unzip mercurial
cd $install_dir
. ./use_redmine

#INSTALL REDMINE_BACKLOGS http://www.redminebacklogs.net/en/installation.html

backlogs_tag=v1.0.6
echo "Installing redmine backlogs version $backlogs_tag"
cd $redmine_htdocs_dir
bundle install --without development test

gem install holidays --version 1.0.3
gem install holidays

cd $plugins_dir
git clone git://github.com/backlogs/redmine_backlogs.git
cd redmine_backlogs
git checkout v1.0.6
bundle install 

cd $redmine_htdocs_dir
RAILS_ENV=production
export RAILS_ENV
bundle install --no-deployment
bundle update nokogiri
bundle exec bin/rake db:migrate RAILS_ENV=production
bundle exec bin/rake tmp:cache:clear RAILS_ENV=production
bundle exec bin/rake tmp:sessions:clear RAILS_ENV=production
bundle exec bin/rake redmine:backlogs:install story_trackers=Feature,Bug,Support task_tracker=Task 


require_restart=true



$install_dir/ctlscript.sh restart

#INSTALL REDMINE PIPELINE PLUGIN
cd $plugins_dir
#TODO: test git clone, if not working, download zip
git clone https://github.com/GitDries/redmine_pipeline_plugin

exit

#INSTALL REDMINE CHARTS 2 

cd $redmine_htdocs_dir
plugin_charts_dir=plugins/redmine_charts2
git clone git://github.com/pharmazone/redmine_charts2 $plugin_charts_dir
cd $plugin_charts_dir
git checkout redmine21

cd $redmine_htdocs_dir
git clone git://github.com/pullmonkey/open_flash_chart.git plugins/open_flash_chart

cd $redmine_htdocs_dir
cp -r plugins/open_flash_chart/assets public/plugin_assets/open_flash_chart


cd $redmine_htdocs_dir
bin/rake redmine:plugins:migrate RAILS_ENV=production

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


cd $redmine_htdocs_dir 
bin/rake redmine:plugins:migrate RAILS_ENV=production
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
