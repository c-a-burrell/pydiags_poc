install:
	@pip install -r requirements.txt

show-edge:
	@python ./diags/edge.py

show-event:
	@python ./diags/event_processing.py

show-gcp:
	@python ./diags/gcp.py

show-kubernetes:
	@python ./diags/kubernetes.py

show-on-prem:
	@python ./diags/on_prem.py

show-custom-remote:
	@python ./diags/custom_remote.py

show-custom-local:
	@python ./diags/custom_local.py

clean-images:
	@rm -fr *.png

show-all: show-event show-edge show-on-prem show-gcp show-kubernetes show-custom-remote show-custom-local
