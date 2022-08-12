import json


def load_candidates_from_json(filename):
    """ Возвращает список экземпляров кандидатов"""

    with open(filename, 'r', encoding='utf-8') as file:
        file = file.read()
        pyt_file = json.loads(file)
        candidates_list = []
        for element in pyt_file:
            from files.class_candidates import Candidates
            candidate = Candidates(element["id"], element["name"],
                                   element["picture"], element["position"],
                                   element["gender"], element["age"],
                                   element["skills"])
            candidates_list.append(candidate)
        return candidates_list


def get_candidate_by_id(candidate_id, filename):
    """ Возвращает кандидата по id"""

    for candidate in filename:
        if candidate_id == candidate.id:
            return candidate
    return False


def get_candidate_by_name(candidate_name, filename):
    """ Возвращает кандидатов по имени"""

    candidates = []
    for candidate in filename:
        if candidate_name.strip().lower() == candidate.name.split()[0].strip().lower():
            candidates.append(candidate)
    return candidates, len(candidates)


def get_candidate_by_skills(candidate_skills, filename):
    """ Возвращает кандидатов по навыкам"""

    candidate_list = []
    flag = False
    for candidate in filename:
        if candidate_skills in candidate.skills.strip().lower():
            candidate_list.append(candidate)
            flag = True
    if flag:
        return candidate_list, len(candidate_list)
    return False
