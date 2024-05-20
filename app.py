from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('patents_database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patent/<patent_id>')
def get_patent(patent_id):
    conn = get_db_connection()
    patent = conn.execute('SELECT * FROM Patent_Table WHERE "Patent" = ?', (patent_id,)).fetchone()
    conn.close()
    if patent is None:
        return render_template('404.html'), 404
    return render_template('patent.html', patent=patent)

@app.route('/search', methods=['POST'])
def search():
    patent_id = request.form['patent_id']
    return redirect(url_for('get_patent', patent_id=patent_id))

if __name__ == '__main__':
    app.run(debug=True)
