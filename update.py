import os
import re

css_target = """
.service-card {
    background: var(--white);
    border-radius: var(--radius-md);
    padding: 40px 30px;
    text-align: center;
    box-shadow: var(--shadow-sm);
    transition: all var(--transition-fast);
    border: 1px solid var(--border-color);
    cursor: pointer;
}

.service-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-lg);
    border-color: var(--accent-color);
}

.service-icon {
    width: 80px;
    height: 80px;
    background: rgba(243, 156, 18, 0.1);
    color: var(--accent-color);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
    margin: 0 auto 20px;
    transition: all var(--transition-fast);
}

.service-card:hover .service-icon {
    background: var(--accent-color);
    color: var(--white);
}

.service-title {
    font-size: 1.5rem;
    margin-bottom: 15px;
}

.service-desc {
    color: var(--text-light);
}
"""

css_replacement = """
.service-card {
    background: var(--white);
    border-radius: var(--radius-md);
    padding: 0;
    text-align: center;
    box-shadow: var(--shadow-sm);
    transition: all var(--transition-fast);
    border: 1px solid var(--border-color);
    cursor: pointer;
    overflow: hidden;
}

.service-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-lg);
    border-color: var(--accent-color);
}

.service-image-wrapper {
    width: 100%;
    height: 220px;
    overflow: hidden;
    position: relative;
}

.service-image-wrapper::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(0,0,0,0) 50%, rgba(0,0,0,0.05) 100%);
    pointer-events: none;
}

.service-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform var(--transition-slow);
}

.service-card:hover .service-image {
    transform: scale(1.1);
}

.service-content {
    padding: 25px 20px 30px;
}

.service-title {
    font-size: 1.4rem;
    margin-bottom: 15px;
}

.service-desc {
    color: var(--text-light);
    font-size: 1.05rem;
    margin-bottom: 0;
}
"""

images_map = {
    "cars": "https://images.unsplash.com/photo-1590725140246-127bc4f781e8?auto=format&fit=crop&w=600&h=400&q=80",
    "gardens": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&h=400&q=80",
    "pools": "https://images.unsplash.com/photo-1572331165267-854da2b10ccc?auto=format&fit=crop&w=600&h=400&q=80",
    "schools": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=600&h=400&q=80",
    "mobile": "https://images.unsplash.com/photo-1537225228614-56cc3556d7ed?auto=format&fit=crop&w=600&h=400&q=80",
    "pvc": "https://images.unsplash.com/photo-1534067783941-51c9c23ecefd?auto=format&fit=crop&w=600&h=400&q=80",
    "french": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&h=400&q=80",
    "cabuli": "https://images.unsplash.com/photo-1588880331179-bc9b9c17bc67?auto=format&fit=crop&w=600&h=400&q=80",
    "dome": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&h=400&q=80",
    "half_circle": "https://images.unsplash.com/photo-1616047006789-b7af5afb8c20?auto=format&fit=crop&w=600&h=400&q=80",
    "pergolas": "https://images.unsplash.com/photo-1621293954908-907159247fc8?auto=format&fit=crop&w=600&h=400&q=80",
    "royal": "https://images.unsplash.com/photo-1542614945-8f654b0c2a26?auto=format&fit=crop&w=600&h=400&q=80",
    "tents": "https://images.unsplash.com/photo-1504280390224-11e25e8efca4?auto=format&fit=crop&w=600&h=400&q=80",
    "fabric_screens": "https://images.unsplash.com/photo-1517643534571-0ce2ebf59c23?auto=format&fit=crop&w=600&h=400&q=80",
    "metal_screens_1": "https://images.unsplash.com/photo-1605625470044-8cb376e1a742?auto=format&fit=crop&w=600&h=400&q=80",
    "metal_screens_2": "https://images.unsplash.com/photo-1582266255765-fa5cf1a1d501?auto=format&fit=crop&w=600&h=400&q=80",
    "leather": "https://images.unsplash.com/photo-1559564101-72990a424a73?auto=format&fit=crop&w=600&h=400&q=80",
    "birds": "https://images.unsplash.com/photo-1456926631375-92c8ce872def?auto=format&fit=crop&w=600&h=400&q=80",
    "pyramid": "https://images.unsplash.com/photo-1520699918507-3c3e05c46b0c?auto=format&fit=crop&w=600&h=400&q=80",
    "gov": "https://images.unsplash.com/photo-1506521781263-d8422e82f27a?auto=format&fit=crop&w=600&h=400&q=80",
    "outdoor": "https://images.unsplash.com/photo-1499803270242-467fc866838a?auto=format&fit=crop&w=600&h=400&q=80",
    "stretch": "https://images.unsplash.com/photo-1610486810260-23a311b151f4?auto=format&fit=crop&w=600&h=400&q=80",
    "cone": "https://images.unsplash.com/photo-1484131920875-12cfefd4a7db?auto=format&fit=crop&w=600&h=400&q=80",
}

def update_css():
    css_path = r"d:\أفكار الظلال للمظلات\css\styles.css"
    with open(css_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    start_idx = content.find(".service-card {")
    gallery_comment_idx = content.find('/* Gallery */', start_idx)
    if start_idx != -1 and gallery_comment_idx != -1:
        new_content = content[:start_idx] + css_replacement.strip() + "\\n\\n" + content[gallery_comment_idx:]
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("CSS Updated Successfully!")
    else:
        print("CSS replace failed to match target block.")

def update_html():
    html_path = r"d:\أفكار الظلال للمظلات\index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Safe regex that strictly looks for the exact HTML structure of the card
    pattern = r'<div class="service-card" data-service="([^"]+)">\s*<div class="service-icon">.*?</div>\s*<h3 class="service-title">(.*?)</h3>\s*<p class="service-desc">(.*?)</p>\s*</div>'
    
    def replacer(match):
        service_id = match.group(1)
        title_str = match.group(2)
        desc_str = match.group(3)
        
        img_url = images_map.get(service_id, "https://images.unsplash.com/photo-1590725140246-127bc4f781e8?auto=format&fit=crop&w=600&h=400&q=80")
        
        # Remove any HTML tags from title for alt attribute
        title_text = re.sub(r'<[^>]+>', '', title_str).strip()
        
        new_card = f"""<div class="service-card" data-service="{service_id}">
                    <div class="service-image-wrapper">
                        <img src="{img_url}" alt="{title_text}" class="service-image" loading="lazy">
                    </div>
                    <div class="service-content">
                        <h3 class="service-title">{title_str}</h3>
                        <p class="service-desc">{desc_str}</p>
                    </div>
                </div>"""
        return new_card

    new_html = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("HTML Updated Successfully!")

if __name__ == "__main__":
    update_css()
    update_html()
