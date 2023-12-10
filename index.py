from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    # Fetch data from the form
    full_name = request.form.get('full_name')
    phone_number = request.form.get('phone_number')
    email_address = request.form.get('email_address')
    linkedin_url = request.form.get('linkedin_url')
    portfolio_url = request.form.get('portfolio_url')
    professional_summary = request.form.get('professional_summary')
    company_name = request.form.get('company_name')
    job_title = request.form.get('job_title')
    dates_of_employment = request.form.get('dates_of_employment')
    institution_name_1 = request.form.get('institution_name_1')
    degree_name_1 = request.form.get('degree_name_1')
    graduation_year_1 = request.form.get('graduation_year_1')
    skill_1 = request.form.get('skill_1')
    template = request.form.get('template')

    # Process the data and generate the resume (you can customize this part)

    # For simplicity, let's pass the data to the resume template
    return render_template('resume.html', data={
        'full_name': full_name,
        'phone_number': phone_number,
        'email_address': email_address,
        'linkedin_url': linkedin_url,
        'portfolio_url': portfolio_url,
        'professional_summary': professional_summary,
        'company_name': company_name,
        'job_title': job_title,
        'dates_of_employment': dates_of_employment,
        'institution_name_1': institution_name_1,
        'degree_name_1': degree_name_1,
        'graduation_year_1': graduation_year_1,
        'skill_1': skill_1,
        'template': template,
    })

if __name__ == '__main__':
    app.run(debug=True)
