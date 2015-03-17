## Introduction

This directory contains the script for generating the UPE mailing list (`/etc/postfix/virtual`).

## Components

* **get_users.py** retrievs user email data from the Django database.
* **parse_emails.py** parses the current mailing list from `/etc/postfix/virtual`.
* **union.py** is a utility function for merging dictionaries.
* **main.py** uses the above to merge (find the union of) the two sets of user-email mappings.

## In Case Things Go Wrong

### Backup Mailing List
Before running the script for the first time (in March 2015), a backup of the existing mailing list was created in `/src/upe.berkeley.edu/www/website/mailing_list.txt.bak`.

### Authors
This script was created by:
* ALLEN GUO <allenguo@berkeley.edu>
* EDWARD LOOK <edwlook@berkeley.edu>
* VENKATA SRIKAR REDDY POREDDY <vsporeddy@berkeley.edu>
* JORDON MCLAUGHLIN WING <jordonwing@berkeley.edu>
* NATHAN WONG <nathan@berkeley.edu>
