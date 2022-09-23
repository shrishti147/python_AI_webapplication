#!/usr/bin/python3
import cgitb
import os
import subprocess
from urllib.parse import parse_qs
cgitb.enable()
print("Content-type: text/html\r\n")
qps = os.environ.get("QUERY_STRING","No Params")
form_vals = parse_qs(qps)
commands = []
if form_vals.get('command') and form_vals.get('ip') and form_vals.get('command')[0] == 'all':
    commands.append('nmap' + ' ' + form_vals.get('ip')[0])
    commands.append('sslscan' + ' ' + form_vals.get('ip')[0])
    commands.append('nikto' + ' ' + form_vals.get('ip')[0])
elif form_vals.get('command') and form_vals.get('ip') and form_vals.get('command')[0] in ['nmap', 'sslscan', 'nikto']:
    commands.append(form_vals.get('command')[0] + ' ' + form_vals.get('ip')[0])
#qps = qps.split('&')
#form_vals = {}
#for qp in qps:
#    qp = qp.split('=')
#    if qp[0]:
#        form_vals[qp[0]] = qp[1]
#print(form_vals['command'])
print(f'''
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Testing IPs</title>
</head>
<body>
<h1>ONLINE NETWORK SCANNING TOOL</h1>
<div>
<form>
<div>
<h2>Select the test which you want to run </h2>
<table style="border: ;3">
<tbody>
<tr>
<td>
<label for="nmap">
<input type="radio" value="nmap" name="command" id="nmap">Nmap
</label>
</td>
</tr>
<tr>
<td>
<label for="sslscan">
<input type="radio" value="sslscan" name="command" id="sslscan">Sslscan
</label>
</td>
</tr>
<tr>
<td>
<label for="nikto">
<input type="radio" value="nikto" name="command" id="nikto">Nikto
</label>
</td>
</tr>
<tr>
<td>
<label for="all">
<input type="radio" value="all" name="command" id="all">All
</label>
</tr>
</table>
</div>
<div>
<p>
<h3>Provide an IP</h3>
<input type="text" name="ip" placeholder="Add ip"/>
<input type="submit" value="Generate Report"/>
</p>
</div>
''')
if form_vals.get('command') and form_vals.get('ip'):
    print(f'''Generating report for: {form_vals}</br></br>''')

for command in commands:
    print(f'''{os.popen(command).read().replace(os.linesep,'</br>')}''')
print(f'''
</form>
</div>
</body>
</html>
''')

#fie1 = subprocess.run(["ls", "-l"])
#"The exit code was: %d" % file1.returncode

