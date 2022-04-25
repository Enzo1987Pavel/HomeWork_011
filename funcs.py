import json

candidate_list = []


def load_candidates_from_json(path):
	"""Загрузка списка кандидатов из файла"""
	global candidate_list

	with open(path, "r", encoding="utf-8") as candidates:
		candidate_list = json.load(candidates)
	return candidate_list


def get_candidate(candidate_id):
	"""Возвращает одного кандидата по его id"""
	for candidate in candidate_list:
		if candidate["id"] == candidate_id:
			return candidate

	return {"not_found": "Кандидата с таким номером не существует!"}


def get_candidates_by_name(candidate_name):
	"""Возвращает кандидата по его имени"""
	return [candidate for candidate in candidate_list if candidate_name.lower() in candidate["name"].lower()]


def get_candidates_by_skill(skill_name):
	"""Возвращает кандидата по его умению"""
	candidate_skill = []

	for candidate in candidate_list:
		skills = candidate["skills"].lower().split(", ")

		if skill_name.lower() in skills:
			candidate_skill.append(candidate)

	return candidate_skill
