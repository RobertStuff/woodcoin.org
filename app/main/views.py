from flask import render_template, send_file, url_for, Blueprint, redirect



main_blueprint = Blueprint('main', __name__,)

@main_blueprint.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@main_blueprint.route('/faq', methods=['GET', 'POST'])
def faq():
	return render_template('faq.html', methods=['GET'])

@main_blueprint.route('/specs', methods=['GET', 'POST'])
def specs():
	return render_template('specs.html', methods=['GET'])

@main_blueprint.route('/merchants', methods=['GET', 'POST'])
def merchants():
	return render_template('merchants.html', methods=['GET'])

@main_blueprint.route('/extras', methods=['GET', 'POST'])
def extras():
	return render_template('extras.html', methods=['GET'])

@main_blueprint.route('/logic.phm', methods=['GET', 'POST'])
def logic():
	return render_template('logic.phm.html', methods=['GET'])



@main_blueprint.route('/woodcoin.pdf/', )
def woodcoin():
    
    return send_file('/home/robert/woodcoin.org/app/static/woodcoin.pdf', attachment_filename='woocoin.pdf')

