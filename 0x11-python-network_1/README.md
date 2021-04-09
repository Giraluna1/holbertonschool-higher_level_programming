<p align="center">
    <img alt="0x11. Python - Network #1" src="https://lh5.googleusercontent.com/wFWKOnuDEjB5kWlguu1hRNf7f--MuX8w3GiARfSiU6-p2sT9vO_dt2YSFvuZvCqCFHstK-UXKqGZ3IiTvwjZvrBydEPhnfmbW81wnhnkf7s-hnlqsKGmqZe-NuOFM-cQmCDBVTYB" />
</p>
<h1 align="center">
    0x11. Python - Network #1
</h1>

## 🧐 Learning Objects

- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## 🛠 TOOLS

- Editor
- Ubuntu 14.04 LTS
- python 3.4.3

## 📝 FILES

<table>
<thead>
<tr>
  <th>TASK</th>
  <th>Directory</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td></td>
  <td> README.md</td>
  <td>...<td>
</tr>
<tr>
  <td>0</td>
  <td>0-hbtn_status.py</td>
  <td>Write a Python script that fetches https://intranet.hbtn.io/status

    You must use the package urllib
    You are not allowed to import any packages other than urllib
    The body of the response must be displayed like the following example (tabulation before -)
    You must use a with statement

   </td>
</tr>
<tr>
  <td>1</td>
  <td>1-hbtn_header.py</td>
  <td> lWrite a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

    You must use the packages urllib and sys
    You are not allow to import packages other than urllib and sys
    The value of this variable is different for each request
    You don’t need to check arguments passed to the script (number or type)
    You must use a with statement

</td>
</tr>
<tr>
  <td>2</td>
  <td>2-post_email.py</td>
  <td>Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

    The email must be sent in the email variable
    You must use the packages urllib and sys
    You are not allowed to import packages other than urllib and sys
    You don’t need to check arguments passed to the script (number or type)
    You must use the with statement

Please test your script in the container provided, using the web server running on port 5000

</td>
</tr>
<tr>
  <td>3</td>
  <td>3-error_code.py</td>
  <td>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

    You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
    You must use the packages urllib and sys
    You are not allowed to import other packages than urllib and sys
    You don’t need to check arguments passed to the script (number or type)
    You must use the with statement

Please test your script in the container provided, using the web server running on port 5000

</td>
</tr>
<tr>
  <td>4</td>
  <td>4-hbtn_status.py</td>
  <td>Write a Python script that fetches https://intranet.hbtn.io/status

    You must use the package requests
    You are not allow to import packages other than requests
    The body of the response must be display like the following example (tabulation before -)

</td>
</tr>
<tr>
  <td>5</td>
  <td>5-hbtn_header.py</td>
  <td> Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

    You must use the packages requests and sys
    You are not allow to import other packages than requests and sys
    The value of this variable is different for each request
    You don’t need to check script arguments (number and type)

</td>
</tr>
<tr>
  <td>6</td>
  <td>6-post_email.py</td>
  <td>Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

    The email must be sent in the variable email
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to error check arguments passed to the script (number or type)

Please test your script in the container provided, using the web server running on port 5000

</td>
</tr>
<tr>
  <td>7</td>
  <td>7-error_code.py</td>
  <td>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

    If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)

Please test your script in the container provided, using the web server running on port 5000

</td>
</tr>
<tr>
  <td>8</td>
  <td>8-json_api.py</td>
  <td>Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    You must use the package requests and sys
    You are not allowed to import packages other than requests and sys

Please test your script in the container provided, using the web server running on port 5000. All JSON generated by this server are random.

</td>
</tr>
<tr>
  <td>9</td>
  <td>9-my_github.py</td>
  <td>Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

    You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
    The first argument will be your username
    The second argument will be your password (in your case, a personal access token as password)
    You must use the package requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)

</td>
</tr>
</td>
</tr>
</tbody>
</table>

## _BY_ @Giraluna1

<lunagolo@hotmail.com>
