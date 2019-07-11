requirements: ## Install python requirements
	pip3 install -r requirements.txt
	
move_review_to_done: ## Move all cards in ready for review to done and close them
	./move_review_to_done.py
	
create_issues_and_cards: ## Create Issues and cards from google spreadshet
	./create_issues_and_cards.py
	
close_done_cards: ## Close all issues in done
	./close_done_issues.py
	
help:
	    @egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
	    
	    
.PHONY: help
