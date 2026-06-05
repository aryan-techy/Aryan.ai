import codecs

with codecs.open('index.html', 'r', 'utf-8-sig') as f:
    content = f.read()

head_insert = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aryan Kumar | Tech Enthusiast</title>
    <!-- FAVICON -->
    <link rel="icon" type="image/jpeg" href="https://i.ibb.co/5WP9dMSQ/IMG-20250602-WA0012.jpg">"""

import re
new_content = re.sub(
    r'<title>Aryan Kumar \| Tech Enthusiast</title>',
    r'<title>Aryan Kumar | Tech Enthusiast</title>\r\n    <!-- FAVICON -->\r\n    <link rel="icon" type="image/jpeg" href="https://i.ibb.co/5WP9dMSQ/IMG-20250602-WA0012.jpg">',
    content
)

with codecs.open('index.html', 'w', 'utf-8-sig') as f:
    f.write(new_content)
