.PHONY: reset index master version report doctor

PROJECT_ROOT ?= ./Housing
CAPSTONE ?=
TEMPLATE ?= ./templates/docs/Policy_Proposal.md

reset:
	python3 manage.py reset --project-root "$(PROJECT_ROOT)"

apply:
	python3 manage.py reset --project-root "$(PROJECT_ROOT)" --apply

index:
	python3 manage.py index --project-root "$(PROJECT_ROOT)" $(foreach p,$(CAPSTONE),--capstone $(p))

master:
	python3 manage.py master --project-root "$(PROJECT_ROOT)" --template "$(TEMPLATE)"

version:
	python3 manage.py version --project-root "$(PROJECT_ROOT)" --bump $(v)

report:
	python3 manage.py report --project-root "$(PROJECT_ROOT)" --top $(n) --query "$(q)"

doctor:
	python3 manage.py doctor --project-root "$(PROJECT_ROOT)"
