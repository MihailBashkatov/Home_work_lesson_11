from flask import Flask, render_template

from files.utils import load_candidates_from_json, get_candidate_by_id, get_candidate_by_skills, get_candidate_by_name

# Файл json
DATA = 'candidates.json'

# Получение списка экземпляров кандидатов
CANDIDATES_LIST = load_candidates_from_json(DATA)

# Создание экземпляра Flask
app = Flask(__name__)


# Маршрут на главную страницу с выводом всех кандидатов по гиперссылкам
@app.route('/')
def main_page():
    candidates = CANDIDATES_LIST
    return render_template('list.html', candidates=candidates)


# Маршрут на страницу "кандидат"  с выводом  кандидатов по id
@app.route('/candidate/<int:candidate_id>')
def get_candidate_id(candidate_id):
    if get_candidate_by_id(candidate_id, CANDIDATES_LIST):
        candidate = get_candidate_by_id(candidate_id, CANDIDATES_LIST)
        return render_template('single.html', candidate=candidate)
    return render_template('no_single.html')


# Маршрут на страницу "поиск"  с выводом  кандидатов по имени
@app.route('/search/<candidate_name>')
def get_candidate_name(candidate_name):
    candidates, count = get_candidate_by_name(candidate_name, CANDIDATES_LIST)
    return render_template('names.html', candidates=candidates,
                           count=count, candidate_name=candidate_name)


# Маршрут на страницу "навыки"  с выводом  гиперссылок кандидатов по навыкам
@app.route('/skill/<skill_name>')
def get_candidate_skills(skill_name):
    if get_candidate_by_skills(skill_name, CANDIDATES_LIST):
        candidates, count = get_candidate_by_skills(skill_name, CANDIDATES_LIST)
        return render_template('skill.html', candidates=candidates, count=count, skill_name=skill_name)
    return render_template('no_skill.html')


app.run()
