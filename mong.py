from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["tourist_app"]
collection = db["destinations"]

places = [
    {
        "name": "Shivneri Fort",
        "description": "The birthplace of Chhatrapati Shivaji Maharaj, Shivneri Fort is a historical landmark offering stunning views and a rich history.",
        "image": "shivnerifort.jpg",
        "location": {"latitude": 19.0833, "longitude": 73.6667},
        "best_time_to_visit": "October to March",
        "category": "Historical Fort",
        "entry_fee": 50,
        "opening_hours": "9:00 AM - 6:00 PM",
        "nearby_attractions": ["Lenyadri Caves", "Tung Fort"],
        "accommodation": "Hotel XYZ (5 km away)",
        "things_to_do": ["Trekking", "Photography", "Sightseeing"],
        "accessibility": "Wheelchair accessible",
        "facilities": ["Parking", "Restrooms", "Cafeteria"],
        "historical_significance": "The birthplace of Chhatrapati Shivaji Maharaj.",
        "reviews": [
            {
                "user": "John Doe",
                "rating": 4.5,
                "comment": "Amazing historical site with great views!"
            }
        ],
        "events": ["Shiv Jayanti Celebration", "Annual Fair"],
        "image_url": "https://example.com/images/shivneri_fort.jpg",
        "visitor_tips": "Carry water bottles and wear comfortable shoes."
    },
    {
        "name": "Lenyadri Caves",
        "description": "The Lenyadri Caves are one of the 18 Buddhist rock-cut temples, located on a hill, and offer breathtaking views.",
        "image": "leynadricaves.jpg",
        "location": {"latitude": 19.1020, "longitude": 73.6560},
        "best_time_to_visit": "November to February",
        "category": "Buddhist Caves",
        "entry_fee": 30,
        "opening_hours": "8:00 AM - 5:00 PM",
        "nearby_attractions": ["Shivneri Fort", "Tung Fort"],
        "accommodation": "Hotel ABC (7 km away)",
        "things_to_do": ["Photography", "Trekking", "Pilgrimage"],
        "accessibility": "Not wheelchair accessible",
        "facilities": ["Restrooms", "Food Stalls"],
        "historical_significance": "Buddhist rock-cut temples built around the 1st century BCE.",
        "reviews": [
            {
                "user": "Jane Smith",
                "rating": 4.0,
                "comment": "A serene place to visit for history and nature lovers."
            }
        ],
        "events": ["Buddhist Festival", "Trekking Events"],
        "image_url": "https://example.com/images/lenyadri_caves.jpg",
        "visitor_tips": "Wear comfortable shoes for the trek."
    },
    {
        "name": "Tung Fort",
        "description": "Tung Fort is a popular trekking spot with great panoramic views of the surrounding mountains and valleys.",
        "image": "tungfort.jpg",
        "location": {"latitude": 19.1035, "longitude": 73.6185},
        "best_time_to_visit": "Monsoon and Winter",
        "category": "Trekking Spot",
        "entry_fee": 0,
        "opening_hours": "Open all day",
        "nearby_attractions": ["Shivneri Fort", "Lenyadri Caves"],
        "accommodation": "Hotel DEF (10 km away)",
        "things_to_do": ["Trekking", "Photography", "Camping"],
        "accessibility": "Not wheelchair accessible",
        "facilities": ["Parking", "Restrooms"],
        "historical_significance": "An ancient fort that offers an incredible trekking experience.",
        "reviews": [
            {
                "user": "Alice Johnson",
                "rating": 5.0,
                "comment": "Great trek, stunning views at the top!"
            }
        ],
        "events": ["Monsoon Trekking", "Adventure Tours"],
        "image_url": "https://example.com/images/tung_fort.jpg",
        "visitor_tips": "Start early to avoid the afternoon heat."
    },
    {
        "name": "Naneghat",
        "description": "Naneghat is a mountain pass and a popular trekking site, known for its ancient stone inscriptions and scenic views.",
        "image": "naneghat.jpeg",
        "location": {"latitude": 19.3211, "longitude": 73.6611},
        "best_time_to_visit": "October to March",
        "category": "Mountain Pass",
        "entry_fee": 0,
        "opening_hours": "Open all day",
        "nearby_attractions": ["Jivdhan Fort", "Ganesh Ghat"],
        "accommodation": "Naneghat Resort (5 km away)",
        "things_to_do": ["Trekking", "Photography", "Historical Exploration"],
        "accessibility": "Not wheelchair accessible",
        "facilities": ["Parking", "Restrooms"],
        "historical_significance": "A historic trade route used during the Maratha Empire.",
        "reviews": [
            {
                "user": "Rajesh Patil",
                "rating": 4.8,
                "comment": "Amazing trekking spot with historical value."
            }
        ],
        "events": ["Annual Trekking Event", "Heritage Walk"],
        "image_url": "https://example.com/images/naneghat.jpg",
        "visitor_tips": "Carry enough water and wear good trekking shoes."
    },
    {
        "name": "Jivdhan Fort",
        "description": "A historic fort offering a breathtaking view of the surrounding hills, perfect for adventure lovers.",
        "image": "jivdhanfort.jpg",
        "location": {"latitude": 19.3277, "longitude": 73.6793},
        "best_time_to_visit": "November to March",
        "category": "Trekking Fort",
        "entry_fee": 20,
        "opening_hours": "8:00 AM - 5:00 PM",
        "nearby_attractions": ["Naneghat", "Ganesh Ghat"],
        "accommodation": "Hotel Jivdhan (6 km away)",
        "things_to_do": ["Trekking", "Photography", "Sightseeing"],
        "accessibility": "Not wheelchair accessible",
        "facilities": ["Parking", "Restrooms"],
        "historical_significance": "A fort used to monitor the trade routes during the Maratha era.",
        "reviews": [
            {
                "user": "Suresh Deshmukh",
                "rating": 4.7,
                "comment": "A beautiful and challenging trek with fantastic views."
            }
        ],
        "events": ["Monsoon Trekking", "Winter Trekking"],
        "image_url": "https://example.com/images/jivdhan_fort.jpg",
        "visitor_tips": "Carry food and water for the trek."
    },
    {
        "name": "Chavand Fort",
        "description": "Chavand Fort offers an excellent trekking route and an incredible view of the Sahyadri hills, a perfect place for adventurers.",
        "image": "chavandfort.jpg",
        "location": {"latitude": 19.3000, "longitude": 73.5800},
        "best_time_to_visit": "October to March",
        "category": "Historical Fort",
        "entry_fee": 30,
        "opening_hours": "9:00 AM - 5:00 PM",
        "nearby_attractions": ["Tung Fort", "Lenyadri Caves"],
        "accommodation": "Chavand Fort Resort (10 km away)",
        "things_to_do": ["Trekking", "Photography", "Sightseeing"],
        "accessibility": "Not wheelchair accessible",
        "facilities": ["Parking", "Restrooms"],
        "historical_significance": "A strategic fort used during the Maratha Empire.",
        "reviews": [
            {
                "user": "Anita Patil",
                "rating": 4.3,
                "comment": "Nice trek and a peaceful location."
            }
        ],
        "events": ["Monsoon Trekking", "Annual Fort Celebration"],
        "image_url": "https://example.com/images/chavand_fort.jpg",
        "visitor_tips": "Carry light snacks and water during the trek."
    },
    # Add additional places (fill up to 30 places)
]
places += [
    {
        "name": "Pimpalgaon Joga Dam",
        "description": "Pimpalgaon Joga Dam is a serene location popular for its picturesque views and boating activities.",
        "image": "pimpalgaonjogadam.jpg",
        "location": {"latitude": 19.3036, "longitude": 73.7075},
        "best_time_to_visit": "October to March",
        "category": "Dam and Waterbody",
        "entry_fee": 20,
        "opening_hours": "6:00 AM - 6:00 PM",
        "nearby_attractions": ["Naneghat", "Tung Fort"],
        "accommodation": "Pimpalgaon Resort (5 km away)",
        "things_to_do": ["Boating", "Photography", "Picnics"],
        "accessibility": "Wheelchair accessible",
        "facilities": ["Parking", "Restrooms", "Boating"],
        "historical_significance": "Built for irrigation purposes and now a popular tourist spot.",
        "reviews": [
            {
                "user": "Vijay Shinde",
                "rating": 4.2,
                "comment": "Beautiful place for a weekend getaway!"
            }
        ],
        "events": ["Boating Festival", "Water Sports Event"],
        "image_url": "https://example.com/images/pimpalgaon_joga_dam.jpg",
        "visitor_tips": "Best visited in the early morning for peaceful surroundings."
    },
    {
        "name": "Bhandardara Lake",
        "description": "Bhandardara Lake is a peaceful spot ideal for boating, fishing, and enjoying the scenic beauty of the Sahyadri mountains.",
        "image": "bhandardaralake.jpg",
        "location": {"latitude": 19.5500, "longitude": 73.4667},
        "best_time_to_visit": "September to March",
        "category": "Lake and Scenic Spot",
        "entry_fee": 50,
        "opening_hours": "6:00 AM - 6:00 PM",
        "nearby_attractions": ["Wilson Dam", "Randha Falls"],
        "accommodation": "Bhandardara Resort (4 km away)",
        "things_to_do": ["Boating", "Fishing", "Photography"],
        "accessibility": "Wheelchair accessible",
        "facilities": ["Parking", "Restrooms", "Boating"],
        "historical_significance": "A peaceful getaway built around the Wilson Dam, offering a beautiful lake view.",
        "reviews": [
            {
                "user": "Deepak Raut",
                "rating": 4.7,
                "comment": "Great spot to relax and enjoy nature. Boating is a must!"
            }
        ],
        "events": ["Water Sports Festival", "Fishing Tournament"],
        "image_url": "https://example.com/images/bhandardara_lake.jpg",
        "visitor_tips": "Carry a picnic basket for a relaxing day by the lake."
    }
]

places += [
    {
        "name": "Lohagad Fort",
        "description": "Lohagad Fort is an ancient hill fort known for its rich history and breathtaking views of the Western Ghats.",
        "image": "lohagadfort.jpg",
        "location": {"latitude": 19.7196, "longitude": 73.4673},
        "best_time_to_visit": "October to March",
        "category": "Hill Fort",
        "entry_fee": 20,
        "opening_hours": "8:00 AM - 5:00 PM",
        "nearby_attractions": ["Bhaja Caves", "Visapur Fort"],
        "accommodation": "Lonavala Hotels (10 km away)",
        "things_to_do": ["Trekking", "Photography", "Sightseeing"],
        "accessibility": "Not wheelchair accessible",
        "facilities": ["Parking", "Restrooms"],
        "historical_significance": "Lohagad Fort was an important military stronghold during the Maratha Empire.",
        "reviews": [
            {
                "user": "Kajal Deshmukh",
                "rating": 4.6,
                "comment": "Great trek, amazing views, and rich history."
            }
        ],
        "events": ["Monsoon Trekking", "Historical Walks"],
        "image_url": "https://example.com/images/lohagad_fort.jpg",
        "visitor_tips": "Wear sturdy shoes as the trail can be slippery."
    },
    {
        "name": "Malshej Ghat",
        "description": "Malshej Ghat is a popular hill station with lush green valleys and beautiful waterfalls, perfect for nature lovers and trekkers.",
        "image": "malshejghat.jpg",
        "location": {"latitude": 19.6897, "longitude": 73.4805},
        "best_time_to_visit": "June to September (Monsoon)",
        "category": "Hill Station",
        "entry_fee": 10,
        "opening_hours": "Open all day",
        "nearby_attractions": ["Harishchandragad", "Ajoba Hill"],
        "accommodation": "Malshej Ghat Resort (2 km away)",
        "things_to_do": ["Photography", "Trekking", "Nature Walks"],
        "accessibility": "Wheelchair accessible",
        "facilities": ["Parking", "Restrooms"],
        "historical_significance": "Famous for its scenic beauty and ideal for monsoon trekking.",
        "reviews": [
            {
                "user": "Madhuri Joshi",
                "rating": 4.8,
                "comment": "A perfect destination for a monsoon retreat, nature at its best!"
            }
        ],
        "events": ["Monsoon Festival", "Trekking Events"],
        "image_url": "https://example.com/images/malshej_ghat.jpg",
        "visitor_tips": "Carry an umbrella during monsoon season and be ready for foggy weather."
    },
    {
        "name": "Harishchandragad Fort",
        "description": "Harishchandragad is a historic fort located in the Malshej Ghat region. It is known for its challenging treks and panoramic views.",
        "image": "harishchandragadfort.jpg",
        "location": {"latitude": 19.7973, "longitude": 73.5633},
        "best_time_to_visit": "October to March",
        "category": "Fort",
        "entry_fee": 0,
        "opening_hours": "Open all day",
        "nearby_attractions": ["Malshej Ghat", "Tung Fort"],
        "accommodation": "Camping options available",
        "things_to_do": ["Trekking", "Camping", "Photography"],
        "accessibility": "Not wheelchair accessible",
        "facilities": ["Camping Gear", "Parking"],
        "historical_significance": "The fort is famous for its ancient temples and the Harishchandreshwar Temple located at the top.",
        "reviews": [
            {
                "user": "Suraj Jadhav",
                "rating": 4.7,
                "comment": "Challenging trek but the view from the top is worth it."
            }
        ],
        "events": ["Trekking Challenges", "Adventure Camping"],
        "image_url": "https://example.com/images/harishchandragad_fort.jpg",
        "visitor_tips": "Prepare for a difficult trek and pack essentials like water and snacks."
    },
    {
        "name": "Visapur Fort",
        "description": "Visapur Fort is a fort located near Lonavala and is known for its rich history and stunning views of the surrounding landscape.",
        "image": "visapurfort.jpg",
        "location": {"latitude": 19.7626, "longitude": 73.4907},
        "best_time_to_visit": "October to March",
        "category": "Fort",
        "entry_fee": 20,
        "opening_hours": "8:00 AM - 6:00 PM",
        "nearby_attractions": ["Lohagad Fort", "Bhaja Caves"],
        "accommodation": "Lonavala Resorts (8 km away)",
        "things_to_do": ["Trekking", "Sightseeing", "Photography"],
        "accessibility": "Not wheelchair accessible",
        "facilities": ["Parking", "Restrooms"],
        "historical_significance": "Visapur Fort was a stronghold during the Maratha Empire.",
        "reviews": [
            {
                "user": "Abhay Mankar",
                "rating": 4.5,
                "comment": "A moderate trek with great views of the surrounding mountains."
            }
        ],
        "events": ["Monsoon Trekking", "Adventure Walks"],
        "image_url": "https://example.com/images/visapur_fort.jpg",
        "visitor_tips": "Carry sufficient water and snacks, as there are limited shops near the fort."
    }
]

places += [ 
    {
        "name": "Lohagad Fort",
        "description": "A historic hill fort known for its stunning views and rich history.",
        "image": "lohagadfort.jpg",
        "location": {
            "latitude": 18.5860,
            "longitude": 73.4080
        },
        "best_time_to_visit": "October to March",
        "category": "Fort",
        "entry_fee": 0,
        "opening_hours": "8:00 AM - 6:00 PM",
        "nearby_attractions": [
            "Visapur Fort",
            "Bhaja Caves"
        ],
        "accommodation": "Lonavala Resorts (10 km away)",
        "things_to_do": [
            "Trekking",
            "Sightseeing"   ,
            "Photography"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Captured by Chhatrapati Shivaji Maharaj in 1648.",
        "visitor_tips": "Carry water and snacks; it can get crowded during weekends."
    },
    {
        "name": "Sinhagad Fort",
        "description": "A prominent fort known for its historical battles and scenic views.",
        "image": "sinhagadfort.jpg",
        "location": {
            "latitude": 18.4595,
            "longitude": 73.7768
        },
        "best_time_to_visit": "October to March",
        "category": "Fort",
        "entry_fee": 50,
        "opening_hours": "6:00 AM - 6:00 PM",
        "nearby_attractions": [
            "Khadakwasla Dam",
            "Pune City"
        ],
        "accommodation": "Various hotels in Pune (30 km away)",
        "things_to_do": [
            "Trekking",
            "Historical Tours",
            "Photography"
        ],
        "accessibility": "Partially accessible",
        "facilities": [
            "Parking",
            "Food stalls available"
        ],
        "historical_significance": "Site of the Battle of Sinhagad in 1670.",
        "visitor_tips": "Start early to avoid crowds and enjoy sunrise views."
    },
    {
        "name": "Aga Khan Palace",
        "description": "A historical palace that played a significant role in India's freedom struggle.",
        "image": "agakhanpalace.jpg",
        "location": {
            "latitude": 18.5203,
            "longitude": 73.8567
        },
        "best_time_to_visit": "October to February",
        "category": "Heritage Site",
        "entry_fee": 5,
        "opening_hours": "9:00 AM - 5:30 PM",
        "nearby_attractions": [
            "Gandhi National Memorial Society",
            "Yerwada Jail"
        ],
        "accommodation": [
            "Hotels in Pune (5 km away)"
        ],
        "things_to_do": [
            "Historical Tours",
            "Photography",
            "Gardens"
        ],
        "accessibility": [
            "Wheelchair accessible"
        ],
        "facilities": [
            "Parking",
            "Restrooms",
            "Cafeteria"
        ],
        "historical_significance": "Residence of Mahatma Gandhi during the Quit India Movement.",
        "visitor_tips": "Explore the gardens and museum for a deeper understanding of history."
    },
    {
        "name": "Shaniwar Wada",
        "description": "A historical landmark built in 1732, showcasing Maratha architecture.",
        "image": "shaniwarwada.jpeg",
        "location": {
            "latitude": 18.5204,
            "longitude": 73.8567
        },
        "best_time_to_visit": "Year-round",
        "category": "Fort",
        "entry_fee": "Free",
        "opening_hours": "8:00 AM - 6:30 PM",
        "nearby_attractions": [
            "Lal Mahal",
            "Parvati Hill"
        ],
        "accommodation": "Hotels in Pune (3 km away)",
        "things_to_do": [
            "Historical Tours",
            "Photography",
            "Light and Sound Show"
        ],
        "accessibility": "Partially accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Once the seat of the Peshwas of the Maratha Empire.",
        "visitor_tips": "Dont miss the evening light and sound show."
    },
    {
        "name": "Rajiv Gandhi Zoological Park",
        "description": "A large zoo featuring a variety of animals, reptiles, and birds.",
        "image": "rajivgandhizoologicalpark.jpeg",
        "location": {
            "latitude": 18.4486,
            "longitude": 73.8482
        },
        "best_time_to_visit": "October to March",
        "category": "Zoo",
        "entry_fee": "25 (Adults), 10 (Children)",
        "opening_hours": "9:30 AM - 5:00 PM (varies seasonally)",
        "nearby_attractions": [
            "Katraj Lake",
            "Katraj Snake Park"
        ],
        "accommodation": "Hotels in Katraj (10 km away)",
        "things_to_do": [
            "Wildlife Watching",
            "Photography",
            "Boating"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms",
            "Cafeteria"
        ],
        "historical_significance": "Home to various endangered species and conservation efforts.",
        "visitor_tips": "Plan your visit during feeding times for better animal sightings."
    },
    {
        "name": "Empress Garden",
        "description": "A beautiful garden ideal for picnics and leisurely walks.",
        "image": "empressgarden.jpeg",
        "location": {
            "latitude": 18.5192,
            "longitude": 73.9082
        },
        "best_time_to_visit": "November to February",
        "category": "Garden",
        "entry_fee": "Free",
        "opening_hours": "6:00 AM - 8:00 PM",
        "nearby_attractions": [
            "Bund Garden",
            "Osho Garden"
        ],
        "accommodation": "Hotels in Pune (5 km away)",
        "things_to_do": [
            "Walking",
            "Photography",
            "Picnicking"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Established during the British Raj as a botanical garden.",
        "visitor_tips": "Visit early morning or late afternoon for pleasant weather."
    },
    {
        "name": "Panshet Water Park",
        "description": "An adventure park offering water sports amidst scenic surroundings.",
        "image": "panshetwaterpark.png",
        "location": {
            "latitude": 18.4758,
            "longitude": 73.6263
        },
        "best_time_to_visit": "June to September (Monsoon)",
        "category": "Water Park",
        "entry_fee": "Varies by activity",
        "opening_hours": "10:00 AM - 6:00 PM",
        "nearby_attractions": [
            "Khadi Waterfall",
            "Varasgaon Dam"
        ],
        "accommodation": "Resorts near Panshet (5 km away)",
        "things_to_do": [
            "Water Sports",
            "Boating",
            "Picnicking"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms",
            "Food stalls"
        ],
      	"historical_significance": "Popular weekend getaway for locals.",
        "visitor_tips": "Book water activities in advance during peak season."
    },
    {
        "name": "Okayama Friendship Garden",
        "description": "A beautiful Japanese garden promoting peace and friendship.",
        "image": "okayamafriendshipgarden.jpg",
        "location": {
            "latitude": 18.5116,
            "longitude": 73.9254
        },
        "best_time_to_visit": "November to February",
        "category": "Garden",
        "entry_fee": "20",
        "opening_hours": "10: 00 AM - 7: 00 PM",
        "nearby_attractions": [
            "Empress Garden",
            "Pashan Lake"
        ],
        "accommodation": "Hotels in Pune (8 km away)",
        "things_to_do": [
            "Walking",
            "Photography",
            "Meditation"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Inspired by Japanese landscaping traditions.",
        "visitor_tips": "Visit during weekdays for fewer crowds."
    },
    {
        "name": "Vetal Tekdi",
        "description": "A popular trekking spot offering panoramic views of Pune.",
         "image": "vetaltekdi.jpg",
        "location": {
            "latitude": 18.5171,
            "longitude": 73.8203
        },
        "best_time_to_visit": "October to March",
        "category": "Hill",
        "entry_fee": "Free",
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Pashan Lake",
            "Taljai Hill"
        ],
        "accommodation": "Hotels in Pune (7 km away)",
        "things_to_do": [
            "Trekking",
            "Walking",
            "Photography"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Limited parking available"
        ],
        "historical_significance": "A natural retreat within the city limits.",
        "visitor_tips": "Best visited early morning or late afternoon."
    },
    {
        "name": "Darshan Museum",
        "description": "An interactive museum showcasing the life of Sadhu Vaswani.",
         "image": "darshanmuseum.jpg",
        "location": {
            "latitude": 18.5200,
            "longitude": 73.8567
        },
        "best_time_to_visit": "Year-round",
        "category": "Museum",
        "entry_fee": "50",
        "opening_hours": "10: 00 AM - 5: 30 PM",
        "nearby_attractions": [
            "National War Memorial",
            "Mahatma Phule Museum"
        ],
        "accommodation": "Hotels in Pune (5 km away)",   
        "things_to_do": [
            "Guided Tours",
            "Photography",
            "Interactive Exhibits"
        ],    
        "accessibility": "Wheelchair accessible"  ,  
        "facilities": [
            "Parking",
            "Restrooms",
            "Cafeteria"
        ],    
        "historical_significance": "Promotes spiritual teachings through modern technology.",
        "visitor_tips": "Check for guided tour timings."
    },
    {
        "name": "Vishrambaug Wada",
        "description": "An architectural marvel showcasing Maratha heritage.",
         "image": "vishrambaugwada.jpg",
        "location": {
            "latitude": 18.5167,
            "longitude": 73.8567
        }, 
        "best_time_to_visit": "Year-round", 
        "category": "Heritage Site", 
        "entry_fee": "Free", 
        "opening_hours": "8: 00 AM - 6: 00 PM", 
        "nearby_attractions": [
            "Shaniwar Wada",
            "Lal Mahal"
        ], 
        "accommodation": "Hotels in Pune (3 km away)", 
        "things_to_do": [
            "Historical Tours",
            "Photography"
        ], 
        "accessibility": "Partially accessible", 
        "facilities": [
            "Parking",
            "Restrooms"
        ], 
        "historical_significance": "Former residence of Peshwas.", 
        "visitor_tips": "Visit early morning for fewer crowds."
    },
    {
        "name": "Pataleshwar Cave Temple",
        "description": "An ancient rock-cut temple dedicated to Lord Shiva, showcasing impressive architecture.",
         "image": "pataleshwarcavetemple.jpg",
        "location": {
            "latitude": 18.5204,
            "longitude": 73.8567
        },
        "best_time_to_visit": "Year-round",
        "category": "Temple",
        "entry_fee": 0,
        "opening_hours": "8:00 AM - 5:30 PM",
        "nearby_attractions": [
            "Shaniwar Wada",
            "Raja Dinkar Kelkar Museum"
        ],
        "accommodation": "Hotels in Pune (3 km away)",
        "things_to_do": [
            "Exploring",
            "Photography"
        ],
        "accessibility": "Partially accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Dating back to the 9th century, it is a significant example of Rashtrakuta architecture.",
        "visitor_tips": "Visit early to avoid crowds."
    },
    {
        "name": "Bhigwan Bird Sanctuary",
        "description": "A haven for birdwatchers, especially known for migratory birds during winter.",
        "image": "bhigwanbirdsanctuary.jpg",
        "location": {
            "latitude": 18.6333,
            "longitude": 74.4167
        },
        "best_time_to_visit": "November to February",
        "category": "Wildlife Sanctuary",
        "entry_fee": 0,
        "opening_hours": "Sunrise to Sunset",
        "nearby_attractions": [
            "Ujani Dam"
        ],
        "accommodation": "Homestays in Bhigwan (5 km away)",
        "things_to_do": [
            "Bird Watching",
            "Photography"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Limited parking available"
        ],
        "historical_significance": "Known as the Bharatpur of Maharashtra for its rich avian diversity.",
        "visitor_tips": "Bring binoculars and a camera for the best experience."
    },
    {
        "name": "Karla Caves",
        "description": "Ancient Buddhist rock-cut caves featuring intricate carvings and stupas.",
        "image": "karlacaves.jpg",
        "location": {
            "latitude": 18.7491,
            "longitude": 73.3894
        },
        "best_time_to_visit": "October to March",
        "category": "Caves",
        "entry_fee": "Free",
        "opening_hours": "Sunrise to Sunset",
        "nearby_attractions": [
            "Bhaja Caves",
            "Lohagad Fort"
        ],
        "accommodation": "Lonavala Resorts (10 km away)",
        "things_to_do": [
            "Exploring",
            "Photography",
            "Cultural Tours"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Dating back to the 2nd century BC, significant for Buddhist heritage.",
        "visitor_tips": "Visit early morning for fewer crowds."
    },
    {
        "name": "Mulshi Dam",
        "description": "A scenic dam surrounded by lush greenery, perfect for picnics and nature walks.",
        "image": "mulshidam.jpeg",
        "location": {
            "latitude": 18.5864,
            "longitude": 73.4871
        },
        "best_time_to_visit": "June to February",
        "category": "Dam",
        "entry_fee": "Free",
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Panshet Dam",
            "Bhira Dam"
        ],
        "accommodation": "Resorts near Mulshi (5 km away)",
        "things_to_do": [
            "Picnicking",
            "Nature Walks",
            "Photography"
        ],
      "accessibility": "Partially accessible",
      "facilities": [
            "Parking",
            "Restrooms"
        ],
      "historical_significance": "A major water supply source for Pune.",
      "visitor_tips": "Best visited during monsoon for stunning views."
    },
    {
        "name": "Dagdusheth Halwai Ganapati Temple",
        "description": "A famous temple dedicated to Lord Ganesha, known for its grandeur and festival celebrations.",
        "image": "dagdushethhalwaiganapati.jpg",
        "location": {
            "latitude": 18.5218,
            "longitude": 73.8559
        },
        "best_time_to_visit": "Year-round, especially during Ganesh Chaturthi",
        "category": "Temple",
        "entry_fee": "Free",
        "opening_hours": "6:00 AM - 11:00 PM",
        "nearby_attractions": [
            "Shaniwar Wada",
            "Raja Dinkar Kelkar Museum"
        ],
        "accommodation": "Hotels in Pune (2 km away)",
        "things_to_do": [
            "Worshipping",
            "Photography"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms",
            "Food stalls"
        ],
        "historical_significance": "Established in the late 19th century by Dagdusheth Halwai.",
        "visitor_tips": "Visit during early morning or late evening for a peaceful experience."
    },
    {
        "name": "ISKCON NVCC Temple",
        "description": "A beautiful temple dedicated to Lord Krishna, offering spiritual experiences and cultural events.",
        "image": "iskconnvcctemple.jpeg",
        "location": {
            "latitude": 18.5300,
            "longitude": 73.8378
        },
        "best_time_to_visit": "Year-round",
        "category": "Temple",
        "entry_fee": "Free",
        "opening_hours": "4:30 AM - 9:00 PM",
        "nearby_attractions": [
            "Buddha Vihar",
            "Katraj Snake Park"
        ],
        "accommodation": "Hotels in Pune (5 km away)",
        "things_to_do": [
            "Spiritual Activities",
            "Cultural Programs"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms",
            "Cafeteria"
        ],
        "historical_significance": "Part of the International Society for Krishna Consciousness.",
        "visitor_tips": "Participate in evening Aarti for a unique experience."
    },
    {
        "name": "Raja Dinkar Kelkar Museum",
        "description": "A museum showcasing a vast collection of artifacts representing Indian culture.",
        "image": "rajadinkarkelkarmuseum.jpg",
        "location": {
            "latitude": 18.5204,
            "longitude": 73.8567
        },
        "best_time_to_visit": "Year-round",
        "category": "Museum",
        "entry_fee": "50",
        "opening_hours": "10: 00 AM - 5: 30 PM",
        "nearby_attractions": [
            "Darshan Museum",
            "National War Memorial"
        ],
        "accommodation": "Hotels in Pune (3 km away)",
        "things_to_do": [
            "Exploring",
            "Photography"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms",
            "Cafeteria"
        ],
        "historical_significance": "Houses over 20,000 artifacts collected by Dr. Dinkar Kelkar.", "visitor_tips": "Check out the musical instruments section."
    },
    {
        "name": "Osho Ashram",
        "description": "A tranquil meditation center founded by Osho, offering various spiritual programs and workshops.",
        "image": "oshoashram.jpeg",
        "location": {
            "latitude": 18.5304,
            "longitude": 73.8956
        },
        "best_time_to_visit": "Year-round",
        "category": "Spiritual Center",
        "entry_fee": 0,
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Koregaon Park",
            "Bund Garden"
        ],
        "accommodation": "Hotels in Koregaon Park (2 km away)",
        "things_to_do": [
            "Meditation",
            "Yoga",
            "Workshops"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Cafeteria",
            "Restrooms"
        ],
        "historical_significance": "One of the most visited spiritual retreats in India.",
        "visitor_tips": "Participate in morning meditations for a unique experience."
    },
    {
        "name": "Lal Mahal",
        "description": "A historic palace that was the residence of Chhatrapati Shivaji Maharaj during his childhood.",
        "image": "lalmahal.jpg",
        "location": {
            "latitude": 18.5204,
            "longitude": 73.8559
        },
        "best_time_to_visit": "Year-round",
        "category": "Heritage Site",
        "entry_fee": 0,
        "opening_hours": "9:00 AM - 6:00 PM",
        "nearby_attractions": [
            "Shaniwar Wada",
            "Dagdusheth Halwai Ganapati Temple"
        ],
        "accommodation": [
            "Hotels in Pune (3 km away)"
        ],
        "things_to_do": [
            "Exploring",
            "Photography"
        ],
        "accessibility": [
            "Partially accessible"
        ],
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Built in 1630, it is a symbol of Maratha heritage.",
        "visitor_tips": "Visit during festivals for vibrant celebrations."
    },
    {
        "name": "Parvati Hill",
        "description": "A hillock offering panoramic views of Pune and home to several temples.",
        "image": "parvatihill.jpg",
        "location": {
            "latitude": 18.4857,
            "longitude": 73.8390
        },
        "best_time_to_visit": "October to March",
        "category": "Hill Station",
        "entry_fee": "Free",
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Parvati Museum",
            "Devdeveshwar Temple"
        ],
        "accommodation": "Hotels in Pune (5 km away)",
        "things_to_do": [
            "Trekking",
            "Photography",
            "Visiting Temples"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Limited parking available"
        ],
        "historical_significance": "Home to ancient temples and a museum dedicated to Punes history.",
        "visitor_tips": "Climb early morning for a beautiful sunrise view."
    },
    {
        "name": "Torna Fort",
        "description": "A historical fort known for its scenic beauty and trekking opportunities.",
        "image": "tornafort.jpg",
        "location": {
            "latitude": 19.0672,
            "longitude": 73.7283
        },
        "best_time_to_visit": "October to March",
        "category": "Fort",
        "entry_fee": "Free",
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Rajgad Fort",
            "Khadakwasla Dam"
        ],
        "accommodation": "Homestays near Torna (10 km away)",
        "things_to_do": [
            "Trekking",
            "Photography",
            "Exploring Ruins"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Limited parking available"
        ],
        "historical_significance": "First fort captured by Shivaji Maharaj at age 16.",
        "visitor_tips": "Carry enough water and snacks; the trek can be challenging."
    },
    {
        "name": "Della Adventure Park",
        "description": "An adventure park offering various thrilling activities and experiences.",
        "image": "dellaadventurepark.jpg",
        "location": {
            "latitude": 18.7497,
            "longitude": 73.4091
        },
        "best_time_to_visit": "Year-round",
        "category": "Adventure Park",
        "entry_fee": "Varies by activity",
        "opening_hours": "11: 00 AM - 8: 00 PM",
        "nearby_attractions": [
            "Khandala",
            "Lonavala"
        ], 
      "accommodation": "Resorts in Lonavala (5 km away)", 
      "things_to_do": [
            "Zip-lining",
            "ATV rides",
            "Camping"
        ], 
      "accessibility": "Partially accessible", 
      "facilities": [
            "Parking",
            "Restrooms",
            "Food stalls"
        ], 
      "historical_significance": "Popular adventure destination for thrill-seekers.", 
      "visitor_tips": "Book activities in advance during weekends."
    },
    {
        "name": "Bund Garden",
        "description": "A popular garden ideal for picnics and leisurely walks.",
        "image": "bundgarden.jpg",
        "location": {
            "latitude": 18.5251,
            "longitude": 73.8661
        },
        "best_time_to_visit": "November to February",
        "category": "Garden",
        "entry_fee": "Free",
        "opening_hours": "6: 00 AM - 8: 00 PM",
        "nearby_attractions": [
            "Mahatma Gandhi Udyan",
            "Katraj Lake"
        ],
        "accommodation": "Hotels in Pune (5 km away)",
        "things_to_do": [
            "Walking",
            "Photography",
            "Boating"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "A serene spot for relaxation amidst nature.",
        "visitor_tips": "Ideal for morning walks or evening picnics."
    },
    {
        "name": "Chaturshringi Temple",
        "description": "A revered temple dedicated to Goddess Chaturshringi, located on a hilltop with stunning views.",
        "image": "chaturshringitemple.jpg",
        "location": {
            "latitude": 18.5320,
            "longitude": 73.8270
        },
        "best_time_to_visit": "October to March",
        "category": "Temple",
        "entry_fee": 0,
        "opening_hours": "5:30 AM - 9:00 PM",
        "nearby_attractions": [
            "Vetal Tekdi",
            "Pashan Lake"
        ],
        "accommodation": "Hotels in Pune (6 km away)",
        "things_to_do": [
            "Worship",
            "Photography",
            "Nature Walks"
        ],
        "accessibility": "Partially accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "A significant pilgrimage site during Navratri.",
        "visitor_tips": "Visit during early morning for a peaceful experience."
    },
    {
        "name": "Peshwe Udyan Zoo",
        "description": "Also known as Rajiv Gandhi Zoological Park, this zoo features a variety of animals, birds, and reptiles in a natural habitat.",
        "image": "peshwasudyanzoo.jpeg",
        "location": {
            "latitude": 18.4486,
            "longitude": 73.8482
        },
        "best_time_to_visit": "October to March",
        "category": "Zoo",
        "entry_fee": 25,
        "opening_hours": "9:30 AM - 5:00 PM",
        "nearby_attractions": [
            "Katraj Lake",
            "Rajiv Gandhi Zoological Park"
        ],
        "accommodation": "Hotels in Katraj (10 km away)",
        "things_to_do": [
            "Wildlife Watching",
            "Photography"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms",
            "Cafeteria"
        ],
        "historical_significance": "Important for conservation efforts and education.",
        "visitor_tips": "Plan your visit during feeding times for better animal sightings."
    },
    {
        "name": "Khadakwasla Dam",
        "description": "A picturesque dam ideal for picnics and water sports activities.",
        "image": "khadakwasladam.jpeg",
        "location": {
            "latitude": 18.4871,
            "longitude": 73.7723
        },
        "best_time_to_visit": "June to February",
        "category": "Dam",
        "entry_fee": "Free",
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Sinhagad Fort",
            "Panshet Water Park"
        ],
        "accommodation": "Resorts near Khadakwasla (5 km away)",
        "things_to_do": [
            "Boating",
            "Picnicking",
            "Photography"
        ],
        "accessibility": "Partially accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "An important water supply source for Pune.",
        "visitor_tips": "Visit during monsoon for stunning views."
    },
    {
        "name": "Tamhini Waterfalls",
        "description": "A stunning waterfall located in the Tamhini region, perfect for nature lovers and photographers.",
        "image": "tamhiniwaterfalls.jpeg",
        "location": {
            "latitude": 15.5925,
            "longitude": 73.4692
        },
        "best_time_to_visit": "June to September (Monsoon)",
        "category": "Waterfall",
        "entry_fee": 0,
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Bhira Dam",
            "Mulshi Dam"
        ],
        "accommodation": "Homestays in Tamhini (10 km away)",
        "things_to_do": [
            "Photography",
            "Trekking",
            "Picnicking"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Limited parking available"
        ],
        "historical_significance": "A popular spot for its natural beauty during the monsoon season.",
        "visitor_tips": "Visit early morning for the best light for photography."
    },
    {
        "name": "Khadakwasla Lake",
        "description": "A picturesque lake near Khadakwasla Dam, ideal for boating and picnics.",
        "image": "khadakwaslalake.jpg",
        "location": {
            "latitude": 18.4871,
            "longitude": 73.7723
        },
        "best_time_to_visit": "October to March",
        "category": "Lake",
        "entry_fee": 0,
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Sinhagad Fort",
            "Panshet Water Park"
        ],
        "accommodation": [
            "Resorts near Khadakwasla (5 km away)"
        ],
        "things_to_do": [
            "Boating",
            "Picnicking",
            "Photography"
        ],
        "accessibility": [
            "Partially accessible"
        ],
        "facilities": [
            "Parking",
            "Restrooms",
            "Food stalls"
        ],
        "historical_significance": "A major water supply source for Pune.",
        "visitor_tips": "Ideal for sunset views."
    },
    {
        "name": "Chakan Fort",
        "description": "A historic fort known for its strategic location and beautiful surroundings.",
        "image": "chakanfort.jpg",
        "location": {
            "latitude": 18.7470,
            "longitude": 73.6541
        },
        "best_time_to_visit": "October to March",
        "category": "Fort",
        "entry_fee": "Free",
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Khadakwasla Dam",
            "Talegaon Dabhade"
        ],
        "accommodation": "Hotels in Chakan (5 km away)",
        "things_to_do": [
            "Exploring",
            "Photography",
            "Trekking"
        ],
        "accessibility": "Not wheelchair accessible",
        "facilities": [
            "Limited parking available"
        ],
        "historical_significance": "Built by the Mughals, it has witnessed many battles.",
        "visitor_tips": "Carry water and snacks; the area is less commercialized."
    },
    {
        "name": "Nehru Memorial Museum",
        "description": "A museum dedicated to Jawaharlal Nehru, featuring his personal belongings and historical artifacts.",
        "image": "nehrumemorialmuseum.jpeg",
        "location": {
            "latitude": 18.5256,
            "longitude": 73.8452
        },
        "best_time_to_visit": "Year-round",
        "category": "Museum",
        "entry_fee": "10",
        "opening_hours": "10: 00 AM - 5: 30 PM",
        "nearby_attractions": [
            "National War Memorial",
            "Shaniwar Wada"
        ],
        "accommodation": "Hotels in Pune (3 km away)",
        "things_to_do": [
            "Exploring",
            "Photography"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Showcases the life and contributions of India’s first Prime Minister.",
        "visitor_tips": "Check for special exhibitions during your visit."
    },
    {
        "name": "Saras Baug",
        "description": "A beautiful garden with a temple dedicated to Lord Ganesh, popular for family outings.",
        "image": "sarasbaug.jpeg",
        "location": {
            "latitude": 18.5204,
            "longitude": 73.8559
        },
        "best_time_to_visit": "November to February",
        "category": "Garden",
        "entry_fee": "Free",
        "opening_hours": "6:00 AM - 9:00 PM",
        "nearby_attractions": [
            "Parvati Hill",
            "Shaniwar Wada"
        ],
        "accommodation": "Hotels in Pune (3 km away)",
        "things_to_do": [
            "Walking",
            "Photography",
            "Picnicking"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "Home to the famous Ganesh Temple built in the late 18th century.",
        "visitor_tips": "Ideal for morning walks or evening picnics."
    },
    {
        "name": "Pashan Lake",
        "description": "A serene lake ideal for bird watching and nature walks.",
        "image": "pashanlake.jpg",
        "location": {
            "latitude": 18.5187,
            "longitude": 73.8257
        },
        "best_time_to_visit": "October to March",
        "category": "Lake",
        "entry_fee": "Free",
        "opening_hours": "Open all day",
        "nearby_attractions": [
            "Vetal Tekdi",
            "Pashan Hill"
        ],
        "accommodation": "Hotels in Pune (8 km away)",
        "things_to_do": [
            "Bird Watching",
            "Photography",
            "Walking"
        ],
        "accessibility": "Wheelchair accessible",
        "facilities": [
            "Parking",
            "Restrooms"
        ],
        "historical_significance": "An important ecological site for various bird species.",
        "visitor_tips": "Bring binoculars for bird watching."
    }
]


# Insert the data into the MongoDB collection
collection.insert_many(places)

print("Destinations inserted successfully!")
