## Level : Easy

#### Challenge Name :  Admin has the power
- URL : http://35.193.45.56/adminpower/
- Walk Throught  
  ```
  1. Check the Source Page
  2. Will Get ID:PASSWORD
  3. Login & Get Flag
  ```
---

#### Challenge Name : This is Sparta 
- URL : http://35.193.45.56/sparta/
- Walk Throught  
  1. Check the Source page
  2. JavaScript Read : http://35.193.45.56/sparta/
  ```js
  function check() {
    var _0xeb80x2 = document['getElementById']('user')['value'];
    var _0xeb80x3 = document['getElementById']('pass')['value'];
    if (_0xeb80x2 == 'Cyber-Talent' && _0xeb80x3 == 'Cyber-Talent') {
        alert('Congratz \x0A\x0A');
    } else {
        alert('wrong Password');
    }
  }
  ```
  3. "Cyber-Talent:Cyber-Talent" Login & Get Flag
  4. FLAG:{J4V4_Scr1Pt_1S_Aw3s0me}
- Etc
  - Enum : http://ddecode.com/hexdecoder
---

#### Challenge Name : I am Legend
- URL : http://35.193.45.56/iamlegend/
- Walk Throught
  - Deobfuscator Site : 
  - http://deobfuscatejavascript.com/#
    - 1.Check the Source Page
    - 2.Read JSfuck Code & Deobfuscator Site decode
      ```js
      String.fromCharCode(102, 117, 110, 99, 116, 105, 111, 110, 32, 99, 104, 101, 99, 107, 40, 41, 123, 10, 10, 118, 97, 114, 32, 117, 115, 101, 114, 32, 61, 32, 100, 111, 99, 117, 109, 101, 110, 116, 91, 34, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 66, 121, 73, 100, 34, 93, 40, 34, 117, 115, 101, 114, 34, 41, 91, 34, 118, 97, 108, 117, 101, 34, 93, 59, 10, 118, 97, 114, 32, 112, 97, 115, 115, 32, 61, 32, 100, 111, 99, 117, 109, 101, 110, 116, 91, 34, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 66, 121, 73, 100, 34, 93, 40, 34, 112, 97, 115, 115, 34, 41, 91, 34, 118, 97, 108, 117, 101, 34, 93, 59, 10, 10, 105, 102, 40, 117, 115, 101, 114, 61, 61, 34, 67, 121, 98, 101, 114, 34, 32, 38, 38, 32, 112, 97, 115, 115, 61, 61, 32, 34, 84, 97, 108, 101, 110, 116, 34, 41, 123, 97, 108, 101, 114, 116, 40, 34, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 67, 111, 110, 103, 114, 97, 116, 122, 32, 92, 110, 32, 70, 108, 97, 103, 58, 32, 123, 74, 52, 86, 52, 95, 83, 99, 114, 49, 80, 116, 95, 49, 83, 95, 83, 48, 95, 68, 52, 77, 78, 95, 70, 85, 78, 125, 34, 41, 59, 125, 32, 10, 101, 108, 115, 101, 32, 123, 97, 108, 101, 114, 116, 40, 34, 119, 114, 111, 110, 103, 32, 80, 97, 115, 115, 119, 111, 114, 100, 34, 41, 59, 125, 10, 10, 125)
      ```
    - 3.Web Console paste & will username & password
    - 4.Login & Get Flag:  Flag: {J4V4_Scr1Pt_1S_S0_D4MN_FUN}