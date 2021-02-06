# PLAT FORM : Hacker 101 (Walk Throught)
```
Trivial (1 / flag) : (Web)
# A little something to get you started 
1. Access to page
2. View page source!
3. copy background.png
4. access to background.png path

```

```
Easy (2 / flag) : (Web)
# Micro-CMS v1
1. Access to  http://{ip}/1aeb2309b1/page/edit/2
- Seem's be XSS
- <script onclick="javascript:alert('1')">1</script> 
- get first flag

2. Accss to http://{ip}/1aeb2309b1/page/edit/4
-get second flag

3. Go Home
- get Third flag

4. Access to Edit page
- http://35.227.24.107/1aeb2309b1/page/edit/0'%20or%20true
- get Four flag

```
