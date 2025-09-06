#!/bin/bash
BACKUP_DIR=/backup
DB_USER=notes_user
DB_PASS=STRONG_DB_PASSWORD   # replace with your real DB password
DB_NAME=notes_db
DATE=$(date +%F-%H%M)

mysqldump -u $DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/notes_db_$DATE.sql

# Keep only the 7 most recent backups
cd $BACKUP_DIR
ls -1t notes_db_*.sql | tail -n +8 | xargs rm -f
