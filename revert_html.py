import re

html_path = r"d:\أفكار الظلال للمظلات\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# The pattern captures the ID (like cars), the title, and the description
pattern = r'<div class="service-card" data-service="([^"]+)">\s*<div class="service-image-wrapper">.*?</div>\s*<div class="service-content">\s*<h3 class="service-title">(.*?)</h3>\s*<p class="service-desc">(.*?)</p>\s*</div>\s*</div>'

# Mapping of services to their original icons
icon_map = {
    "cars": "fa-car",
    "gardens": "fa-tree",
    "pools": "fa-swimming-pool",
    "schools": "fa-school",
    "mobile": "fa-tent",
    "pvc": "fa-cube",
    "french": "fa-umbrella",
    "cabuli": "fa-umbrella-beach",
    "dome": "fa-archway",
    "half_circle": "fa-circle-half-stroke",
    "pergolas": "fa-home",
    "royal": "fa-crown",
    "tents": "fa-campground",
    "fabric_screens": "fa-layer-group",
    "metal_screens_1": "fa-bars",
    "metal_screens_2": "fa-grip-lines-vertical",
    "leather": "fa-umbrella",
    "birds": "fa-dove",
    "pyramid": "fa-car-side",
    "gov": "fa-building",
    "outdoor": "fa-chair",
    "stretch": "fa-vector-square",
    "cone": "fa-mountain"
}

def replacer(match):
    service_id = match.group(1)
    title = match.group(2)
    desc = match.group(3)
    icon = icon_map.get(service_id, "fa-star") # fallback icon
    
    return f"""<div class="service-card" data-service="{service_id}">
                    <div class="service-icon"><i class="fas {icon}"></i></div>
                    <h3 class="service-title">{title}</h3>
                    <p class="service-desc">{desc}</p>
                </div>"""

new_html = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_html)
print("Reverted to icons successfully!")
