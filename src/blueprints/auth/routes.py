from src.blueprints.auth import bp

@bp.route('/')
def login():
    return 'Login'