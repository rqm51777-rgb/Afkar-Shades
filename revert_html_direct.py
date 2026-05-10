import re

html_path = r"d:\أفكار الظلال للمظلات\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Look for the entire grid block and replace it hardcoded
start_marker = '<div class="services-grid">'
end_marker = '</div>\n        </div>\n    </section>\n\n    <!-- Gallery Section -->'

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    original_grid = """<div class="services-grid">
                <div class="service-card" data-service="cars">
                    <div class="service-icon"><i class="fas fa-car"></i></div>
                    <h3 class="service-title">مظلات سيارات</h3>
                    <p class="service-desc">حماية كاملة لسيارتك من أشعة الشمس والأمطار بتصاميم عصرية جذابة.</p>
                </div>
                <div class="service-card" data-service="gardens">
                    <div class="service-icon"><i class="fas fa-tree"></i></div>
                    <h3 class="service-title">مظلات حدائق</h3>
                    <p class="service-desc">جلسات خارجية رائعة مع مظلات حدائق خشبية وحديدية مقاومة للعوامل الجوية.</p>
                </div>
                <div class="service-card" data-service="pools">
                    <div class="service-icon"><i class="fas fa-swimming-pool"></i></div>
                    <h3 class="service-title">مظلات مسابح</h3>
                    <p class="service-desc">تغطية المسابح لحماية الأطفال والحفاظ على نظافة المياه من الأتربة.</p>
                </div>
                <div class="service-card" data-service="schools">
                    <div class="service-icon"><i class="fas fa-school"></i></div>
                    <h3 class="service-title">مظلات مدارس</h3>
                    <p class="service-desc">مظلات ساحات المدارس بمواصفات معتمدة توفر الظل والأمان للطلاب.</p>
                </div>
                <div class="service-card" data-service="mobile">
                    <div class="service-icon"><i class="fas fa-tent"></i></div>
                    <h3 class="service-title">مظلات متنقلة</h3>
                    <p class="service-desc">حلول عملية وسريعة للرحلات والمناسبات مع مظلات سهلة الفك والتركيب.</p>
                </div>
                <div class="service-card" data-service="pvc">
                    <div class="service-icon"><i class="fas fa-cube"></i></div>
                    <h3 class="service-title">مظلات حديد وقماش</h3>
                    <p class="service-desc">تصاميم متينة من الحديد المدمج بقماش PVC و البولي إيثيلين الفاخر عالي
                        الكثافة.</p>
                </div>
                <div class="service-card" data-service="french">
                    <div class="service-icon"><i class="fas fa-umbrella"></i></div>
                    <h3 class="service-title">مظلات فرنسي</h3>
                    <p class="service-desc">تصاميم فرنسية أنيقة تضيف لمسة جمالية وفخامة للمداخل والمقاهي والمحلات.</p>
                </div>
                <div class="service-card" data-service="cabuli">
                    <div class="service-icon"><i class="fas fa-umbrella-beach"></i></div>
                    <h3 class="service-title">مظلات كابولي</h3>
                    <p class="service-desc">مظلات قوية ومتينة بدون أعمدة أمامية لسهولة الحركة والمواقف.</p>
                </div>
                <div class="service-card" data-service="dome">
                    <div class="service-icon"><i class="fas fa-archway"></i></div>
                    <h3 class="service-title">مظلات مقوس</h3>
                    <p class="service-desc">مظلات بتصاميم مقوسة رائعة تناسب مختلف المساحات والاحتياجات.</p>
                </div>
                <div class="service-card" data-service="half_circle">
                    <div class="service-icon"><i class="fas fa-circle-half-stroke"></i></div>
                    <h3 class="service-title">مظلات نص دايره</h3>
                    <p class="service-desc">تصاميم عصرية بشكل نصف دائرة توفر حماية ممتازة وشكلاً جذاباً.</p>
                </div>
                <div class="service-card" data-service="pergolas">
                    <div class="service-icon"><i class="fas fa-home"></i></div>
                    <h3 class="service-title">برجولات بجميع انواعها وأشكاله</h3>
                    <p class="service-desc">أجمل البرجولات الخشبية والحديدية لتجميل الحدائق والجلسات الخارجية.</p>
                </div>
                <div class="service-card" data-service="royal">
                    <div class="service-icon"><i class="fas fa-crown"></i></div>
                    <h3 class="service-title">بيوت شعر ملكي</h3>
                    <p class="service-desc">خيام وبيوت شعر بتجهيزات فخمة وملكية تناسب جميع المناسبات والاستقبالات.</p>
                </div>
                <div class="service-card" data-service="tents">
                    <div class="service-icon"><i class="fas fa-campground"></i></div>
                    <h3 class="service-title">خيم</h3>
                    <p class="service-desc">خيام متنوعة بمقاسات وتصاميم مختلفة تلبي كافة احتياجاتكم للمناسبات والرحلات.</p>
                </div>
                <div class="service-card" data-service="fabric_screens">
                    <div class="service-icon"><i class="fas fa-layer-group"></i></div>
                    <h3 class="service-title">سواتر قماش</h3>
                    <p class="service-desc">سواتر قماشية عالية الجودة توفر الخصوصية التامة والحماية من الرياح.</p>
                </div>
                <div class="service-card" data-service="metal_screens_1">
                    <div class="service-icon"><i class="fas fa-bars"></i></div>
                    <h3 class="service-title">سواتر عاشق ومعشوق</h3>
                    <p class="service-desc">سواتر حديدية بتصميم عاشق ومعشوق لضمان الخصوصية والتهوية الجيدة.</p>
                </div>
                <div class="service-card" data-service="metal_screens_2">
                    <div class="service-icon"><i class="fas fa-grip-lines-vertical"></i></div>
                    <h3 class="service-title">سواتر حديد مجدول</h3>
                    <p class="service-desc">أقوى السواتر الحديدية المجدولة التي تجمع بين الأمان والجمال.</p>
                </div>
                <div class="service-card" data-service="leather">
                    <div class="service-icon"><i class="fas fa-umbrella"></i></div>
                    <h3 class="service-title">مظلات جلد ارتداد</h3>
                    <p class="service-desc">مظلات مميزة من الجلد للارتدادات توفر ظلاً ممتازاً وحماية من العوامل الجوية.</p>
                </div>
                <div class="service-card" data-service="birds">
                    <div class="service-icon"><i class="fas fa-dove"></i></div>
                    <h3 class="service-title">واقي حمام</h3>
                    <p class="service-desc">تركيب شبك وواقي طيور وحمام للحفاظ على نظافة النوافذ والأسطح.</p>
                </div>
                <div class="service-card" data-service="pyramid">
                    <div class="service-icon"><i class="fas fa-car-side"></i></div>
                    <h3 class="service-title">مظلات سيارات هرمي</h3>
                    <p class="service-desc">مظلات سيارات بالشكل الهرمي الكلاسيكي لحماية مثالية وتحمل للظروف الصعبة.</p>
                </div>
                <div class="service-card" data-service="gov">
                    <div class="service-icon"><i class="fas fa-building"></i></div>
                    <h3 class="service-title">مظلات موقف حكومية</h3>
                    <p class="service-desc">تنفيذ مشاريع مظلات مواقف السيارات للجهات الحكومية والشركات بكفاءة عالية.</p>
                </div>
                <div class="service-card" data-service="outdoor">
                    <div class="service-icon"><i class="fas fa-chair"></i></div>
                    <h3 class="service-title">جلسات خارجية</h3>
                    <p class="service-desc">تجهيز أروع الجلسات الخارجية بتصاميم مريحة وأنيقة للاستمتاع بالهواء الطلق.</p>
                </div>
                <div class="service-card" data-service="stretch">
                    <div class="service-icon"><i class="fas fa-vector-square"></i></div>
                    <h3 class="service-title">مظلات شد إنشائي</h3>
                    <p class="service-desc">مظلات متطورة بخيوط مشدودة مصممة هندسياً لتغطية المساحات الواسعة بشكل جمالي.</p>
                </div>
                <div class="service-card" data-service="cone">
                    <div class="service-icon"><i class="fas fa-mountain"></i></div>
                    <h3 class="service-title">مظلات مخروطي</h3>
                    <p class="service-desc">مظلات بالشكل المخروطي الجذاب الذي يعطي طابعاً فريداً ومميزاً للأماكن العامة والخاصة.</p>
                </div>
            </div>"""
    
    new_content = content[:start_idx] + original_grid + '\n        ' + content[end_idx:]
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("HTML reverted successfully!")
else:
    print("Could not find markers.")
