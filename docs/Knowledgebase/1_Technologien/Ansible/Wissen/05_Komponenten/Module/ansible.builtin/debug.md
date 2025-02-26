# ansible.builtin.debug

- [Docs: ansible.buildin.debug](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debug_module.html)
- lets you output `variables`, `ansible_facts` on execution of Playbooks
- good in conjuntion with the task_parameter `when`

## task output

- use the task_parameter `register` to save the output of a task into a variable
	- [Docs: Registring variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#registering-variables)
- reference the stored variable in the module_parameter `var` or `msg` of `register`

## single variable

- can be used to print the content of a single variable

```
- name: GetOS
  hosts: all
  tasks:
    - name: Get OS from ansible_facts
      debug:
        var: ansible_facts['os_family']
```

## multiple variables

- bundled under the parameter `msg` several variables can be composed

```
- name: GetInfos
  hosts: all
  tasks:
    - name: Get information about the OS
      debug:
        msg: 
          Host: "{{ inventory_hostname }}"
          OS: "{{ ansible_facts['os_family'] }}"
          Architecture: "{{ ansible_facts['architecture'] }}"
```

- alternatively in one line

```
- name: GetInfos
  hosts: all
  tasks:
    - name: Get information about the OS
      debug:
        msg: "{{ inventory_hostname }} has {{ ansible_facts['os_family'] }} as OS and works on an {{ ansible_facts['architecture'] }} architecture."
```