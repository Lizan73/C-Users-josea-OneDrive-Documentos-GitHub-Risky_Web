from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.database = "instance/risky_burger.sqlite"

def get_db_connection():
    try:
        conn = sqlite3.connect(app.database)
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def row_to_dict(row):
    return {key: row[key] for key in row.keys()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    try:
        conn = get_db_connection()
        if conn:
            items = conn.execute('SELECT * FROM menu_items').fetchall()
            conn.close()
            return render_template('menu.html', items=items)
        else:
            flash('Database connection error.', 'error')
            return render_template('menu.html', items=[])
    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while fetching the menu.', 'error')
        return render_template('menu.html', items=[])

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            conn = get_db_connection()
            if conn:
                admin = conn.execute('SELECT * FROM admins WHERE username = ?', (username,)).fetchone()
                conn.close()
                if admin and check_password_hash(admin['password'], password):
                    session['admin_id'] = admin['id']
                    return redirect(url_for('admin_dashboard'))
                else:
                    flash('Invalid username or password.', 'error')
            else:
                flash('Database connection error.', 'error')
        return render_template('admin_login.html')
    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred during login.', 'error')
        return render_template('admin_login.html')

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    try:
        if 'admin_id' not in session:
            return redirect(url_for('admin_login'))

        conn = get_db_connection()
        if not conn:
            flash('Database connection error.', 'error')
            return redirect(url_for('admin_login'))

        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            ingredients = request.form['ingredients']
            image = request.form['image']
            category = request.form['category']
            price = request.form['price']
            if request.form['submit'] == 'Add':
                conn.execute('INSERT INTO menu_items (name, description, ingredients, image, category, price) VALUES (?, ?, ?, ?, ?, ?)',
                             (name, description, ingredients, image, category, price))
                flash('Item added successfully!', 'success')
            elif request.form['submit'] == 'Update':
                item_id = request.form['id']
                conn.execute('UPDATE menu_items SET name = ?, description = ?, ingredients = ?, image = ?, category = ?, price = ? WHERE id = ?',
                             (name, description, ingredients, image, category, price, item_id))
                flash('Item updated successfully!', 'success')
            conn.commit()

        items = conn.execute('SELECT * FROM menu_items').fetchall()
        items = [row_to_dict(item) for item in items]
        conn.close()
        return render_template('admin_dashboard.html', items=items)
    except Exception as e:
        print(f"Error: {e}")
        flash(f'An error occurred while accessing the dashboard: {e}', 'error')
        return redirect(url_for('admin_login'))

@app.route('/admin/delete_item/<int:id>', methods=['POST'])
def delete_item(id):
    try:
        conn = get_db_connection()
        if conn:
            conn.execute('DELETE FROM menu_items WHERE id = ?', (id,))
            conn.commit()
            conn.close()
            flash('Item deleted successfully!', 'success')
        else:
            flash('Database connection error.', 'error')
    except Exception as e:
        print(f"Error: {e}")
        flash(f'An error occurred while deleting the item: {e}', 'error')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
