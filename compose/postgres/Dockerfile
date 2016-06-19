FROM postgres:9.5
MAINTAINER Manu Phatak <bionikspoon@gmail.com>

ADD backup.sh /usr/local/bin/backup
RUN chmod +x /usr/local/bin/backup

ADD restore.sh /usr/local/bin/restore
RUN chmod +x /usr/local/bin/restore

ADD list-backups.sh /usr/local/bin/list-backups
RUN chmod +x /usr/local/bin/list-backups
