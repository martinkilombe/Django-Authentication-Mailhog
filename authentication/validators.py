from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def __init__(self):
        self.min_length = 8
        self.max_length = 30

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                f'Password must be at least {self.min_length} characters long.'
            )
        if len(password) > self.max_length:
            raise ValidationError(
                f'Password must be at most {self.max_length} characters long.'
            )
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                'Password must contain at least one uppercase letter.'
            )
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                'Password must contain at least one lowercase letter.'
            )
        if not re.search(r'[0-9]', password):
            raise ValidationError(
                'Password must contain at least one number.'
            )
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(
                'Password must contain at least one special character.'
            )
        
        # Check for common sequences
        common_sequences = ['qwerty', '123456', 'abc123', 'password']
        if any(seq in password.lower() for seq in common_sequences):
            raise ValidationError(
                'Password contains a common sequence.'
            )

        # Check for personal information if user is provided
        if user:
            user_attrs = ['username', 'first_name', 'last_name']
            for attr in user_attrs:
                if hasattr(user, attr):
                    value = getattr(user, attr).lower()
                    if value and len(value) > 2 and value in password.lower():
                        raise ValidationError(
                            'Password cannot contain your personal information.'
                        )

    def get_help_text(self):
        return """
        Your password must:
        • Be 8-30 characters long
        • Contain at least one uppercase letter
        • Contain at least one lowercase letter
        • Contain at least one number
        • Contain at least one special character
        • Not contain common sequences
        • Not contain personal information
        """