#!/usr/bin/python -u

import cgi

if __name__=='__main__':
    print "Content-type: text/html"
    
    print
    print '''
    <!DOCTYPE html>
    <html>
	<style>
body {
margin-left:auto;
	margin-right:auto;
	min-height: 100%;
  min-width: 1024px;
	width: 100%;
  height: 100%;
background-image:url('/twitter/twitter.jpg');	

}
table, td, th
{
	
	 margin-top:70px 
}
.buttonStyle
{
font-type: italic;
}
</style>	


    <body>
    <form action="userinterface.py">
	<table align="center">

&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<img align="center" src="/twitter/project_logo.png"></img>
<tr>
<td>
<i>ENTER KEYWORD:</i>
</td>
<td>
    <input type="text" name="keyword" style="background-color:#CEF6F5;" />

<td>
</tr>
<tr>
<td>
<i>ENTER RADIUS:</i>
</td>
<td>   
<input type="text" name="radius" style="background-color:#CEF6F5;"/>
</td>
</tr>
<tr>
<td>
<i>ENTER CITY:</i>
</td>
<td>   
<input type="text" name="city" style="background-color:#CEF6F5;"/>
</td>
</tr>

<tr>

<td colspan="2" align="center">
<br>
    <input type="submit" class="buttonStyle" value="Get the TWEETS"></input>
</td>
</tr>
    </form>
    </body>
    </html>
    '''
