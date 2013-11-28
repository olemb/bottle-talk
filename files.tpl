<!doctype html>
<html>
<head><title>Bottle</title></head>
<link rel="stylesheet" href="uit/uit.css" type="text/css" />
<link rel="stylesheet" href="lib/slides.css" type="text/css" />
<body>

<div id="uitname"><img src="uit/name.png"></div>
<div id="uitlogo"><img src="uit/logo.png"></div>

<div class="section" id="files">
<h1>Files</h1>

<p><a href="./">Back to presentation</a></p>

<ul>
  % for file in files:
    <li>
       <a href="{{file}}">{{file}}</a>
    </li>
  % end
</ul>

</div>

</body>
</html>
