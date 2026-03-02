APP = restapi-flask

.PHONY: build up down logs

compose:
	docker-compose build
	docker-compose up
down:
	docker-compose down
logs:
	docker-compose logs -f

test:
	flake8 . --exclude ./venv
	pytest -v --disable-warnings

kind-up:
	kind create cluster --config /Users/joao/projetos/restapi-flask/kubernetes/config/config.yaml
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
	kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=270s
	kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/usage.yaml
	helm upgrade --install mongodb --set auth.rootPassword="root" kubernetes/charts/mongodb
	kubectl wait --for=condition=ready pod --selector=app.kubernetes.io/name=mongodb --timeout=270s

kind-down:
	kind delete cluster

kind-logs:
	kubectl logs -f -l app=restapi-flask