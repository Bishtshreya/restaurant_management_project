import logging
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

logger = logging.getLogger(__name__)

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        logger.warning(f"Invalid email address attempted: {email}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error while validating email `{email}`: {str(e)})
        return False