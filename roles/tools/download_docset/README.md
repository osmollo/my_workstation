# download_docset

## Ejemplo

```yaml
- name: "download docset"
  include_role:
    name: tools/download_docset
  vars:
    docset_name: "{{ item }}"
  loop:
    - Ansible
    - Docker
    - Bash
```
