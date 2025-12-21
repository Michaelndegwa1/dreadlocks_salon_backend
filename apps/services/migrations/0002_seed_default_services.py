from django.db import migrations

def seed_defaults(apps, schema_editor):
    ServiceCategory = apps.get_model('services', 'ServiceCategory')
    Service = apps.get_model('services', 'Service')

    default_data = [
        {
            'category': {'name': 'Loc Installation (Starter Locs)', 'description': 'These services initiate the journey based on hair texture and desired aesthetic.'},
            'services': [
                {'name': 'Comb Coils', 'description': 'Ideal for short, kinky hair to create uniform, hollow-centered traditional locs.', 'price': 50, 'duration_minutes': 120},
                {'name': 'Two-Strand Twists', 'description': 'Provides a strong internal foundation and more initial volume than coils.', 'price': 60, 'duration_minutes': 150},
                {'name': 'Interlocking Starters', 'description': 'Uses a specialized tool to pull hair through itself; preferred for active lifestyles as they don\'t unravel easily.', 'price': 80, 'duration_minutes': 180},
                {'name': 'Microlocs / Sisterlocks™', 'description': 'Small-scale installations that offer maximum versatility and styling options.', 'price': 150, 'duration_minutes': 300},
                {'name': 'Backcombing & Crochet', 'description': 'Mandatory for straight or wavy hair to create immediate friction and matting.', 'price': 100, 'duration_minutes': 240}
            ]
        },
        {
            'category': {'name': 'Loc Maintenance (Re-tightening)', 'description': 'Regular maintenance (every 4–8 weeks) ensures locs remain neat and healthy at the root.'},
            'services': [
                {'name': 'Palm Rolling', 'description': 'A traditional method using a downward motion to stretch out lumps and maintain a round shape.', 'price': 40, 'duration_minutes': 90},
                {'name': 'Root Interlocking', 'description': 'Essential for micro-sized locs, using a crochet needle to secure new growth.', 'price': 70, 'duration_minutes': 120},
                {'name': 'Clockwise Rubbing', 'description': 'A technique to encourage stubborn new growth to knot naturally with the hair\'s grain.', 'price': 45, 'duration_minutes': 60},
                {'name': 'Loc Detox (ACV Soak)', 'description': 'A deep-cleansing baking soda and apple cider vinegar rinse to remove years of product buildup and lint.', 'price': 35, 'duration_minutes': 45},
                {'name': 'Hydration Steam Treatment', 'description': 'Uses steam to deeply penetrate the loc core with moisture, preventing brittleness.', 'price': 30, 'duration_minutes': 30}
            ]
        },
        {
            'category': {'name': 'Instant Locs & Extensions', 'description': 'For those who wish to skip the "baby stage" or add immediate length.'},
            'services': [
                {'name': 'Crochet Instant Locs', 'description': 'Manually matting natural hair into a mature state using a tiny 0.6mm–0.75mm hook.', 'price': 120, 'duration_minutes': 240},
                {'name': 'Permanent Human Hair Extensions', 'description': 'Attaching high-quality human hair to existing locs for a seamless length increase.', 'price': 250, 'duration_minutes': 360},
                {'name': 'Synthetic Loc Wraps', 'description': 'A temporary "faux loc" service using synthetic hair wrapped around natural braids for a change in look.', 'price': 90, 'duration_minutes': 180},
                {'name': 'Wick / Florida Wick Installation', 'description': 'Creating extremely thick, heavy locs by combining multiple existing locs or large sections.', 'price': 200, 'duration_minutes': 300},
                {'name': 'Loc Reattachment', 'description': 'Professionally sewing previously cut locs back onto the client\'s natural hair.', 'price': 150, 'duration_minutes': 240}
            ]
        },
        {
            'category': {'name': 'Loc Repair & Restoration', 'description': 'Corrective services to save thinning or damaged locs without cutting them off.'},
            'services': [
                {'name': 'Individual Loc Strengthening', 'description': 'Reinforcing "weak spots" or thinning points with added human hair fibers.', 'price': 15, 'duration_minutes': 30},
                {'name': 'Root Grafting', 'description': 'Repairing locs that are hanging by a few strands by re-securing them to the healthy scalp area.', 'price': 25, 'duration_minutes': 45},
                {'name': 'Loc Combination', 'description': 'Joining two thinning locs together at the base to create one thicker, stronger loc.', 'price': 20, 'duration_minutes': 40},
                {'name': 'Scalp & Follicle Therapy', 'description': 'Specialized treatments focusing on hair loss and thinning at the scalp level.', 'price': 55, 'duration_minutes': 60},
                {'name': 'Professional Loc Removal', 'description': 'A meticulous, non-cutting technique to un-mat locs and return to loose hair.', 'price': 100, 'duration_minutes': 300}
            ]
        },
        {
            'category': {'name': 'Advanced Styling & Color', 'description': 'High-end aesthetic services to transform the look of mature locs.'},
            'services': [
                {'name': 'Barrel Rolls', 'description': 'A popular, neat style where locs are rolled into flat, horizontal tubes across the head.', 'price': 35, 'duration_minutes': 60},
                {'name': 'Pipe Cleaner / Rod Curls', 'description': 'Using specialized tools to give locs a tight, springy spiral curl.', 'price': 45, 'duration_minutes': 90},
                {'name': 'Custom Loc Color (Ombre/Highlights)', 'description': 'Using specialized dyes that only coat the exterior to avoid internal core damage.', 'price': 85, 'duration_minutes': 120},
                {'name': 'Loc Petal Bun', 'description': 'An intricate updo where individual locs are looped to resemble flower petals.', 'price': 50, 'duration_minutes': 75},
                {'name': 'Intricate Braiding & Cornrows', 'description': 'Combining locs into larger braids or cornrow patterns for a structured, long-lasting look.', 'price': 60, 'duration_minutes': 90}
            ]
        }
    ]

    for item in default_data:
        category, created = ServiceCategory.objects.get_or_create(
            name=item['category']['name'],
            defaults={'description': item['category']['description']}
        )
        
        for service_data in item['services']:
            Service.objects.get_or_create(
                name=service_data['name'],
                category=category,
                defaults={
                    'description': service_data['description'],
                    'price': service_data['price'],
                    'duration_minutes': service_data['duration_minutes'],
                    'is_active': True
                }
            )

def remove_defaults(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_defaults, remove_defaults),
    ]
