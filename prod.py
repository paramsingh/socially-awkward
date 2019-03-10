from social.db import create_tables
from social.webserver import create_app

create_tables()
app = create_app()
