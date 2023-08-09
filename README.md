# exe2html

A small script that converts any .exe file you want to HyperText Markup Language (.html) file.

Run the Python file and enter the path to the .exe file. This will save the encrypted base64 data to the output_base64.txt file.

It will then take the contents of the output_base64.txt file and generate the JavaScript code using the convert_exe_to_html function.

The generated HTML code is saved in the output_script.html file.

You can now run the HTML code using the generated output_script.html file. But keep in mind that this code uses ActiveX objects and you need to be careful about security. Therefore, you should only use this code to run .exe files from trusted and well-known sources.

After the process is complete, the temporary generated output_base64.txt file will be deleted.
