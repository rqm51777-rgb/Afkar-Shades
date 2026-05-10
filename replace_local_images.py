import re

html_path = r"d:\أفكار الظلال للمظلات\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

local_images = [
    "images/work1.png",
    "images/work2.png",
    "images/work3.png",
    "images/work4.png"
]

img_index = 0

def replacer(match):
    global img_index
    # The regex matches <img src="url" alt="text" class="service-image" loading="lazy">
    original_match = match.group(0)
    if "unsplash" in original_match:
        img_src = local_images[img_index % len(local_images)]
        img_index += 1
        return re.sub(r'src="[^"]+"', f'src="{img_src}"', original_match)
    return original_match

# Find all img tags with class service-image
pattern = r'<img src="[^"]+" alt="[^"]+" class="service-image" loading="lazy">'
new_html = re.sub(pattern, replacer, content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_html)
print("Updated all images to local ones.")
