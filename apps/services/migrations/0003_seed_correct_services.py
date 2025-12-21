from django.db import migrations

def seed_correct_services(apps, schema_editor):
    ServiceCategory = apps.get_model('services', 'ServiceCategory')
    Service = apps.get_model('services', 'Service')

    default_data = [
        {
            'category': {'name': 'Starter & Installation Services', 'description': 'These services establish the foundation of your loc journey based on your hair texture and desired size.'},
            'services': [
                {'name': 'Traditional Comb Coils/Twists', 'description': 'Starting locs on natural hair.', 'price': 3000, 'duration_minutes': 120},
                {'name': 'Sisterlocks™ Installation', 'description': 'A trademarked micro-loc technique using a proprietary tool.', 'price': 20000, 'duration_minutes': 300},
                {'name': 'Microlocs (Interlocking)', 'description': 'Small locs started with interlocking rather than the Sisterlocks method.', 'price': 10000, 'duration_minutes': 240},
                {'name': 'Backcombing & Crochet (Natural)', 'description': 'Creating "instant" natural starter locs without extensions.', 'price': 1500, 'duration_minutes': 180},
                {'name': 'Baby Locs for Kids', 'description': 'Specialized gentle installation for children.', 'price': 2000, 'duration_minutes': 90}
            ]
        },
        {
            'category': {'name': 'Maintenance & Retightening', 'description': 'Regular upkeep to manage new growth and maintain the "grid" pattern.'},
            'services': [
                {'name': 'Palm Rolling & Retwist', 'description': 'Standard maintenance using gels or oils to smooth new growth into the loc.', 'price': 1200, 'duration_minutes': 90},
                {'name': 'Interlocking/Retie', 'description': 'Using a tool to pull the loc through the new growth; standard for Sisterlocks or microlocs.', 'price': 1800, 'duration_minutes': 120},
                {'name': 'Crochet Retouch', 'description': 'Using a needle to pull loose hairs back into the loc for a very neat, long-lasting look.', 'price': 2500, 'duration_minutes': 150},
                {'name': 'Loc Rearrangement', 'description': 'Redefining or adjusting the parting pattern (partitions) for a cleaner look.', 'price': 0, 'duration_minutes': 60},
                {'name': 'Styling (Updos/Braids)', 'description': 'Professional styling added to maintenance, such as petals, barrel twists, or fishbone braids.', 'price': 0, 'duration_minutes': 60}
            ]
        },
        {
            'category': {'name': 'Loc Extensions & Instant Locs', 'description': 'Services for those wanting immediate length or a specific texture.'},
            'services': [
                {'name': 'Human Hair Permanent Extensions', 'description': 'Attaching 100% human hair to your own.', 'price': 20000, 'duration_minutes': 360},
                {'name': 'Artificial/Synthetic Locs', 'description': 'Temporary or long-term synthetic extensions.', 'price': 3000, 'duration_minutes': 180},
                {'name': 'Instant Crochet Locs', 'description': 'Using a crochet hook on your natural hair to make it look mature instantly.', 'price': 10000, 'duration_minutes': 240},
                {'name': 'Bohemian/Soft Locs', 'description': 'Temporary crochet styles providing a "carefree" look.', 'price': 3500, 'duration_minutes': 180},
                {'name': 'Afro-Kinky Sisterlock Extensions', 'description': 'Specifically using kinky hair to add volume to micro-locs.', 'price': 0, 'duration_minutes': 240}
            ]
        },
        {
            'category': {'name': 'Repair & Restoration', 'description': 'Fixing damage caused by weight, poor maintenance, or health issues.'},
            'services': [
                {'name': 'Loc Reattachment', 'description': 'Grafting broken or cut locs back onto the root.', 'price': 1700, 'duration_minutes': 120},
                {'name': 'Thinning Root Repair', 'description': 'Strengthening weak roots using hair grafting or the crochet method.', 'price': 0, 'duration_minutes': 60},
                {'name': 'Loc Combination', 'description': 'Joining two or more locs into one to fix thinning or increase thickness.', 'price': 0, 'duration_minutes': 60},
                {'name': 'Takedown/Removal', 'description': 'Professional "undoing" of locs to save natural hair without cutting them off.', 'price': 0, 'duration_minutes': 300},
                {'name': 'Frizzy Loc Taming', 'description': 'Advanced crochet techniques to smooth out "fuzzy" mature locs.', 'price': 0, 'duration_minutes': 90}
            ]
        },
        {
            'category': {'name': 'Treatments & Detox', 'description': 'Health-focused services for the scalp and the internal structure of the loc.'},
            'services': [
                {'name': 'Loc Detox (ACV Soak)', 'description': 'Deep cleansing to remove lint and product buildup.', 'price': 1500, 'duration_minutes': 60},
                {'name': 'Moisture/Protein Treatments', 'description': 'Deep conditioning specialized for locs to prevent brittleness.', 'price': 800, 'duration_minutes': 45},
                {'name': 'Loc Coloring & Dyeing', 'description': 'Professional application of color or highlights.', 'price': 2000, 'duration_minutes': 120},
                {'name': 'Scalp Therapy/Massage', 'description': 'Treatments specifically for dry, itchy, or flaky scalps.', 'price': 0, 'duration_minutes': 30},
                {'name': 'Hot Oil Treatment', 'description': 'Using natural oils to restore shine and strength to mature locs.', 'price': 0, 'duration_minutes': 30}
            ]
        }
    ]

    for item in default_data:
        category, created = ServiceCategory.objects.get_or_create(
            name=item['category']['name'],
            defaults={'description': item['category']['description']}
        )
        
        if not created and category.description != item['category']['description']:
            category.description = item['category']['description']
            category.save()

        for service_data in item['services']:
            Service.objects.update_or_create(
                name=service_data['name'],
                category=category,
                defaults={
                    'description': service_data['description'],
                    'price': service_data['price'],
                    'duration_minutes': service_data['duration_minutes'],
                    'is_active': True
                }
            )

class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_seed_default_services'),
    ]

    operations = [
        migrations.RunPython(seed_correct_services),
    ]
