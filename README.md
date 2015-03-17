# Introduction

This directory contains the script for generating the UPE mailing list (`/etc/postfix/virtual`).

# Components

* **get_users.py** retrievs user email data from the Django database.
* **parse_emails.py** parses the current mailing list from `/etc/postfix/virtual`.
* **union.py** is a utility function for merging dictionaries.
* **main.py** uses the above to merge (find the union of) the two sets of user-email mappings.

# Authors

This script was created by:
* ALLEN GUO <allenguo@berkeley.edu>
* EDWARD LOOK <edwlook@berkeley.edu>
* VENKATA SRIKAR REDDY POREDDY <vsporeddy@berkeley.edu>
* JORDON MCLAUGHLIN WING <jordonwing@berkeley.edu>
* NATHAN WONG <nathan@berkeley.edu>
