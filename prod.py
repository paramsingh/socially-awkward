from social.db import create_tables, drop_tables
from social.webserver import create_app

if True:
    drop_tables()
create_tables()
app = create_app()
