# Machine IP : 10.10.19.165
# Machine Name : Vulnversity

***TASK1:Deploy the machine***

***TASK2:Reconnaissance<br>***
1.{No answer}<br>
2.{6} <br>
3.{3.5.12}<br>
4.{400} <br>
5.{DNS} <br>
6.{Ubuntu}<br>
7.{3333}<br>
8.{No answer}<br>

***TASK3:Locating Directories using GoBuster***<br>
1.{No answer}<br>
2.{/internal/}<br>

***TASK4:Compromise the webserver***<br>
1.Try upload a few file types to the server, what common extension seems to be blocked?<br>
{.php}<br>

2.To identify which extensions are not blocked, we're going to fuzz the upload form. To do this, we're doing to use BurpSuite. If you are unsure to what BurpSuite is, or how to set it up please complete our BurpSuite room first.<br>
{No answer}<br>

3.We're going to use Intruder (used for automating customised attacks). To begin, make a wordlist with the following extensions in: <br>
{.phtml}<br>

4.Now we know what extension we can use for our payload we can progress.<br>
{No answer}<br>

5.What user was running the web server?<br>
{bill} <br>
6.What is the user flag? <br>
{8bd7992fbe8a6ad22a63361004cfcedb}<br>