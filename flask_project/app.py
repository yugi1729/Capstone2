 #flask app

from flask import Flask, render_template, url_for, request, redirect
import logging as logger
from flask_sqlalchemy import SQLAlchemy
import datetime
logger.basicConfig(level="DEBUG")

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


#db
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	
	content = db.Column(db.String(200), nullable=False)
	
	completed = db.Column(db.Integer, default = 0)
	
	date_created = db.Column(db.DateTime, default = datetime.datetime.now())

	def __repr__(self):
		return '<Task %r>'% self.id


@app.route('/', methods=['POST', 'GET'])

def index():
	if request.method == 'POST':
		task_content = request.form['content']
		new_task = Todo(content = task_content)
		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'Error while adding task'
	
	else:
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template('index.html', tasks=tasks)
	


@app.route('/delete/<int:id>')
def delete(id):
	del_task = Todo.query.get_or_404(id)

	try:
		db.session.delete(del_task)
		db.session.commit()
		return redirect('/')
	except:
		return 'Error while deleting task'


@app.route('/update/<int:id>', methods = ['POST', 'GET'])
def update(id):
	task = Todo.query.get_or_404(id)

	if request.method == 'POST':
		task.content = request.form['content']
		try:
			db.session.commit()
			return redirect('/')
		except:
			return 'Error While updating task'
	else:
		return render_template('update.html', task= task)



# Todo : Books -> name, date borrowed ,  date given,  isbn_number/book_id
if __name__ == '__main__':
	logger.debug('Starting the app')
	app.run(debug=True, use_reloader= True)