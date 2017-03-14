# coding=gbk
from flask import Flask, render_template,url_for
from flask_bootstrap import Bootstrap
from markdown import markdown
import os
app = Flask(__name__)
groups = {}
bootstrap = Bootstrap(app)
article_path=".\\static\\articles\\"

@app.route('/')
def hello_world():

	init()
	f = open('.\\第五次进展报告.md', 'r', encoding='utf-8')
	return render_template('md.html', md=markdown(f.read(), output_format='html4'), title='第五次进展报告', groups=groups)


@app.route('/<group>/<article>')
def show_article(group,article):
	f = open('{0}\\{1}\\{2}'.format(article_path,group,article), 'r', encoding='utf-8')
	return render_template('md.html', md=markdown(f.read(), output_format='html4'), title='第五次进展报告', groups=groups)


def init():
	folders =	os.listdir(article_path)
	for folder in folders:
		groups[folder]={}
		for article in os.listdir(article_path+'\\'+folder):
			groups[folder][article]='{0}/{1}'.format(folder,article)
	print(groups)

if __name__ == '__main__':
	app.run()
	pass
