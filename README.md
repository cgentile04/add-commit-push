# add-commit-push
This project provides code for add-commit-push and is based on 
[W3Schools HTML Tutorial](https://www.w3schools.com/html/).

## Author
Chuckie Gentile [email:charlesegentile@lewisu.edu](mailto:charlesegentile@lewisu.edu)

## Credits
[W3Schools HTML Tutorial](https://www.w3schools.com/html/) for the HTML template code.
Contributor: Eric Pogue [email:epogue@lewisu.edu](mailto:epogue@lewisu.edu)

## Aliases
The following were entered into "Microsoft Powershell" to create the required permanent Aliases.
1. acp: 
PS C:\Users\chuck\lewis\cpsc-20000\sprint-5\add-commit-push>  function racp {
>> python.exe "C:\Users\chuck\lewis\cpsc-20000\sprint-5\add-commit-push\add-commit-push.py"
>> }
PS C:\Users\chuck\lewis\cpsc-20000\sprint-5\add-commit-push> Set-Alias -Name acp -Value racp

2. g5:
 C:\Users\chuck\lewis\cpsc-20000\sprint-5> function s5dir {
>> Set-Location -Path  "C:\Users\chuck\lewis\cpsc-20000\sprint-5"
>> }
PS C:\Users\chuck\lewis\cpsc-20000\sprint-5> Set-Alias -Name g5 -Value s5dir

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Improvements
Add English language and UTF-8 tags by modifying index.html so that it looks like this:
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
	<title>Page Title</title>
</head>
<body>
	<h1>This is a Heading</h1>
	<p>This is a paragraph.</p>
</body>
</html>
```
