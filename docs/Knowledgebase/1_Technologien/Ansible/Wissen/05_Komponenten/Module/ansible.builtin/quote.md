# Docs

- <https://docs.ansible.com/ansible/latest/collections/ansible/builtin/quote_filter.html>

# Explanation

- pipes a variable through Python's `shlex.quote` to protect against user-given input

# Usage

```
{{ some_string_variable | quote }}
```

```
{{ some_string_variable | ansible.builtin.quote }}
```