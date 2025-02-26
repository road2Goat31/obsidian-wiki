# Docs

- https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html

# Usage

```
- name: MyTask
  command:
    cmd: /some/command
    chdir: /some/dir        -> change dir before invoking command
    creates: /some/file     -> tests if file exists, aborts task when found (test before removes)
    removes: /some/file     -> tests if file exists, run task when found
```

# Parameter

- `chdir`
	- change dir before invoking command
- `creates`
	- tests if file exists (test before removes)
	- **aborts task when found**
- `removes`
	- tests if file exists
	- **run task when found**