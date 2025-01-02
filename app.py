from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient('mongodb+srv://vedant:lulli@portfolio.e8ky0.mongodb.net/')
db = client['tourist_app']
users_collection = db['users']
places_collection = db['destinations']
messages_collection = db["messages"]
@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if query:
        # Find places matching the query and retrieve name, image, and description
        places = places_collection.find(
            {'name': {'$regex': query, '$options': 'i'}},
            {'name': 1, 'image': 1, 'description': 1}  # Specify fields to return
        )
        # Build the response JSON
        return jsonify([
            {
                'index': idx,
                'name': place.get('name', ''),
                'image': place.get('image', ''),  # Provide a default empty string
                'description': place.get('description', '')
            }
            for idx, place in enumerate(places)
        ])
    return jsonify([])


# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Normal user login
        user = users_collection.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials. Try again."
    return render_template('login.html')

# Guest login route
@app.route('/guest-login')
def guest_login():
    session['username'] = 'guest'
    return redirect(url_for('home'))

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        full_name = request.form['full_name']
        password = request.form['password']
        phone = request.form['phone']

        # Check if user exists
        existing_user = users_collection.find_one({'username': username})
        if existing_user:
            return "User already exists. Please choose a different username."
        
        # Hash password and save user
        hashed_password = generate_password_hash(password)
        users_collection.insert_one({
            'username': username, 
            'full_name': full_name,
            'password': hashed_password,
            'phone': phone
        })
        
        session['username'] = username
        return redirect(url_for('home'))
    
    return render_template('register.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Profile route
@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = users_collection.find_one({'username': session['username']})
    return render_template('profile.html', user=user)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'})
    
    update_data = {
        'full_name': request.form.get('full_name'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'location': request.form.get('location'),
        'favorite_destinations': request.form.get('favorite_destinations'),
        'travel_style': request.form.get('travel_style'),
        'preferred_season': request.form.get('preferred_season'),
        'languages': request.form.get('languages')
    }
    
    # Remove empty values
    update_data = {k: v for k, v in update_data.items() if v}
    
    try:
        users_collection.update_one(
            {'username': session['username']},
            {'$set': update_data}
        )
        return jsonify({'success': True, 'message': 'Profile updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
    
# Under development route
@app.route('/under-development')
def under_development():
    return render_template('under_development.html')

# Home route
@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    query = request.args.get('q', '').strip()
    selected_category = request.args.get('category', '').strip()
    
    # Build the filter query
    filter_query = {}
    
    if query:
        filter_query['$or'] = [
            {'name': {'$regex': query, '$options': 'i'}},
            {'description': {'$regex': query, '$options': 'i'}},
            {'location': {'$regex': query, '$options': 'i'}}
        ]
    
    if selected_category:
        filter_query['category'] = selected_category
    
    # Get all places based on filters
    places = places_collection.find(filter_query)
    
    # Get all unique categories for the dropdown
    categories = places_collection.distinct('category')
    
    return render_template(
        'home.html',
        places=places,
        search_query=query,
        categories=categories,
        selected_category=selected_category
    )

# Start journey route
@app.route('/start')
def start_journey():
    if 'username' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('destination', index=0))

# Destination route
@app.route('/destination/<int:index>')
def destination(index):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    places = list(places_collection.find())
    if 0 <= index < len(places):
        place = places[index]
        return render_template('destination.html', place=place, index=index, total=len(places))
    else:
        return redirect(url_for('home'))

# Safety tips route
@app.route('/safety-tips')
def safety_tips():
    return render_template('safety_tips.html')

# Testimonials route
@app.route('/testimonials')
def testimonials():
    reviews = [
        {"name": "John Doe", "testimonial": "Junnar is an amazing place to explore!"},
        {"name": "Jane Smith", "testimonial": "Loved the forts and nature trails. A must-visit!"},
    ]
    return render_template('testimonials.html', reviews=reviews)

# Gallery route
@app.route('/gallery')
def gallery():
    places = list(places_collection.find({}, {"_id": 0, "image": 1, "name": 1}))
    return render_template('gallery.html', places=places)

# Contact Us route
@app.route('/contact-us', methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Store in MongoDB
        messages_collection.insert_one({
            "name": name,
            "email": email,
            "message": message
        })
        
        return redirect(url_for("success"))  # Redirect or render success page if needed
    return render_template('contact_us.html')

@app.route('/success')
def success():
    return render_template('success.html')

# About Us route
@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

if __name__ == '__main__':

    app.run(debug=True)