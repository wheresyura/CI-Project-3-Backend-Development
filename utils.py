ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def is_logged_in(session):
    """
    return: None or the username
    """
    return session.get("user")


def allowed_file(filename):
    """
    TODO Enter function documentation
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
