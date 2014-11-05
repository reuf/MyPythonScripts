import re
import pprint
import fnmatch
import os
from collections import defaultdict

unique_urls = defaultdict(list)

all_php_files = []
for root, dirnames, filenames in os.walk(os.getcwd()):
  for filename in fnmatch.filter(filenames, '*.php'):
      all_php_files.append(os.path.join(root, filename))

results = os.path.join(os.getcwd(), 'Rezultati.html')

bootstrap_header = """<!DOCTYPE html>
<html>
  <head>
    <title>Bootstrap 3 Template</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap core CSS -->
    <link href="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.1.0/css/bootstrap.css" rel="stylesheet" media="screen">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7/html5shiv.js"></script>
      <script src="http://cdnjs.cloudflare.com/ajax/libs/respond.js/1.3.0/respond.js"></script>
    <![endif]-->
    <style>
		body
		{
		    counter-reset: Serial;           /* Set the Serial counter to 0 */
		}

		table
		{
		    border-collapse: separate;
		}

		tr td:first-child:before
		{
		  counter-increment: Serial;      /* Increment the Serial counter */
		  content: counter(Serial) "."; /* Display the counter */
		}
	</style>
  </head>
  <body>
    <div class="container">
	<h1>List of wsdls and their usage across files:</h1>
	<div class="row clearfix">
		<div class="col-md-12 column">
			<table class="table">
				<thead>
					<tr>
						<th>
							#
						</th>
						<th>
							WSDL URL
						</th>
						<th>
							FileName - LineNumber
						</th>
					</tr>
				</thead>
				<tbody>
"""

bootstrap_footer = """
				</tbody>
			</table>
		</div>
	</div>
</div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.1.0/js/bootstrap.min.js"></script>
  </body>
</html>
"""

row_begin = """
<tr>
						<td>

						</td>
						<td>
"""
row_middle = """
</td>
						<td>
"""
row_end = """
</td>
					</tr>
"""
for file_name in all_php_files:
	with open(file_name, 'r') as current_file:
	        for i, line in enumerate(current_file):
	        	# treba odraditi jos i za ip adresu 192.168.132.19
	            links1 = re.findall(r"(http\:\/\/.*.\?wsdl)", line.lower())
	            #links2 = re.findall(r"(http\:\/\/192\.168\.132\.19.*.wsdl)", line.lower())
	            links = links1 #+ links2
	            if links:
	            	for link in links:
						unique_urls[link].append(' - '.join([file_name, 'l:%s' % i]))
	                #results_file.write(' - '.join([links[0],file_name, 'l:%s' % i,'\n']))


with open(results, 'w') as results_file:
	results_file.write(bootstrap_header)
	for wsdl_url in sorted(unique_urls):
		results_file.write(row_begin)

		results_file.write(wsdl_url)

		results_file.write(row_middle)

		for file_and_location in unique_urls[wsdl_url]:
			results_file.write(file_and_location)
			results_file.write("<br><br>")

		results_file.write(row_end)
	#pprint.pprint(unique_urls.items(), stream=results_file)
	results_file.write(bootstrap_footer)