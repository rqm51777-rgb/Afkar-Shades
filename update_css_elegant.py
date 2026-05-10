import re

with open("css/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Root variables
css = css.replace(""":root {
    --primary-color: #0F2027;
    --secondary-color: #203A43;
    --accent-color: #f39c12;
    --accent-hover: #e67e22;
    --light-bg: #F8F9FA;
    --white: #FFFFFF;
    --text-dark: #333333;
    --text-light: #666666;
    --border-color: #e5e5e5;
    --font-family: 'Cairo', sans-serif;
    --container-width: 1200px;
    --section-padding: 70px 0;
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 20px;
    --shadow-sm: 0 4px 6px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 10px 20px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 20px 40px rgba(0, 0, 0, 0.12);
    --transition-fast: 0.3s ease;
    --transition-slow: 0.5s ease;
    --header-height: 70px;
}""", """:root {
    --primary-color: #0F2027;
    --secondary-color: #203A43;
    --accent-color: #f39c12;
    --accent-hover: #e67e22;
    --light-bg: #F9FAFB;
    --white: #FFFFFF;
    --text-dark: #1F2937;
    --text-light: #4B5563;
    --border-color: #E5E7EB;
    --font-family: 'Cairo', sans-serif;
    --container-width: 1280px;
    --section-padding: 90px 0;
    --radius-sm: 12px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --shadow-sm: 0 4px 20px rgba(0, 0, 0, 0.03);
    --shadow-md: 0 10px 30px rgba(0, 0, 0, 0.06);
    --shadow-lg: 0 20px 40px rgba(0, 0, 0, 0.1);
    --transition-fast: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    --header-height: 80px;
}""")

# 2. Typography
css = css.replace("""body {
    font-family: var(--font-family);
    background-color: var(--white);
    color: var(--text-dark);
    line-height: 1.7;
    overflow-x: hidden;
    -webkit-text-size-adjust: 100%;
}""", """body {
    font-family: var(--font-family);
    background-color: var(--white);
    color: var(--text-dark);
    line-height: 1.8;
    overflow-x: hidden;
    -webkit-text-size-adjust: 100%;
    -webkit-font-smoothing: antialiased;
}""")

css = css.replace("""h1 { font-size: clamp(1.6rem, 5vw, 3.5rem); }
h2 { font-size: clamp(1.5rem, 4vw, 2.5rem); margin-bottom: 15px; }
h3 { font-size: clamp(1.1rem, 2.5vw, 1.5rem); }""", """h1 { font-size: clamp(2.2rem, 5vw, 4rem); letter-spacing: -0.5px; }
h2 { font-size: clamp(1.8rem, 4vw, 3rem); margin-bottom: 15px; letter-spacing: -0.5px; }
h3 { font-size: clamp(1.2rem, 2.5vw, 1.6rem); }""")

css = css.replace(""".services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 22px;
}""", """.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
}""")

css = css.replace(""".service-image-wrapper {
    width: 100%;
    height: 200px;
    overflow: hidden;
    position: relative;
}""", """.service-image-wrapper {
    width: 100%;
    height: 230px;
    overflow: hidden;
    position: relative;
}""")


# 3. Mobile adjustments
mobile_css = """    /* Services — 2 columns on mobile */
    .services-grid {
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }

    .service-image-wrapper { height: 130px; }

    .service-card.with-image .service-content-wrapper {
        padding: 10px 10px 14px;
    }

    .service-title {
        font-size: 0.88rem;
        margin-bottom: 4px;
    }

    /* Hide desc on mobile (shown in modal) */
    .service-desc { display: none; }"""

new_mobile_css = """    /* Services — 1 elegant column on mobile */
    .services-grid {
        grid-template-columns: 1fr;
        gap: 24px;
    }

    .service-image-wrapper { height: 220px; }

    .service-card.with-image .service-content-wrapper {
        padding: 24px 20px;
    }

    .service-title {
        font-size: 1.25rem;
        margin-bottom: 10px;
    }

    /* Keep desc visible on mobile for single column */
    .service-desc { 
        display: block; 
        font-size: 1rem; 
        color: var(--text-light);
    }"""
css = css.replace(mobile_css, new_mobile_css)


small_mobile_css = """    .services-grid {
        grid-template-columns: 1fr 1fr;
        gap: 8px;
    }

    .service-image-wrapper { height: 110px; }
    .service-title { font-size: 0.8rem; }"""
    
new_small_mobile_css = """    .services-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }

    .service-image-wrapper { height: 200px; }
    .service-title { font-size: 1.15rem; }"""
css = css.replace(small_mobile_css, new_small_mobile_css)


gallery_mobile_css = """    /* Gallery — 2 columns */
    .gallery-grid {
        grid-template-columns: 1fr 1fr;
        gap: 8px;
    }"""
    
new_gallery_mobile_css = """    /* Gallery — 1 elegant column */
    .gallery-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }"""
css = css.replace(gallery_mobile_css, new_gallery_mobile_css)

with open("css/styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("success")
