class ValidateSignupDataService:
    @staticmethod
    def validate(cuit, password1, password2)->list:
        errors = []
        if not ValidateSignupDataService._validate_cuit(cuit):
            errors.append("el cuit debe contener 11 caracteres")
        if not ValidateSignupDataService._validate_password(password1, password2):
            errors.append("los passwords no coinciden")
        return errors
    
    @staticmethod
    def _validate_password(password1:str, password2:str)->bool:
        return True if password1 == password2 else False
    
    @staticmethod
    def _validate_cuit(cuit:str)->bool:
        return True if len(cuit) == 11 else False