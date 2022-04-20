import json


def load_candidates_from_json(path):
	"""Загрузка списка кандидатов из файла"""

	with open(path, "r", encoding="utf-8") as candidates:
		return json.load(candidates)


def get_candidate(candidates, candidate_id):
	"""Возвращает одного кандидата по его id"""
	for candidate in candidates:
		if candidate["id"] == candidate_id:
			return candidate


def get_candidates_by_name(candidates, candidate_name):
	"""Возвращает кандидата по его имени"""
	for candidate in candidates:
		if candidate["name"] == candidate_name:
			return candidate


def get_candidates_by_skill(candidates, candidate_skill):
	"""Возвращает кандидата по его умению"""
	for candidate in candidates:
		if candidate["skills"] == candidate_skill:
			return candidate
