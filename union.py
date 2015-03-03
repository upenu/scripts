
# mailing_list = {'candidates': ['a@b.com', 'c@d.com']}

#mailing_list_from_database
#mailing_list_from_file  # /etc/postfix/virtual


def union_dicts(d1, d2):
  new_dict = {key: set() for key in list(d1.keys()) + list(d2.keys())}
  for key in new_dict.keys():
    if key in d1 and key in d2:
      new_dict[key] = set(d1[key]).union(set(d2[key]))
    elif key in d1:
      new_dict[key] = set(d1[key])
    elif key in d2:
      new_dict[key] = set(d2[key])
  return new_dict

mailing_list = {}

for list_name, emails in mailing_list.items():
  print('%s@upe.cs.berkeley.edu %s@upe.berkeley.edu' % (list_name, list_name))
  print('%s@upe.berkeley.edu' % list_name)
  for email in emails:
    print(' ' + email)
  print('')

d1 = {'a': [1, 2]}
d2 = {'b': [1], 'c': [3]}
print(union_dicts(d1, d2))
