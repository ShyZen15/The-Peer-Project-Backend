from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Password():
    @staticmethod
    def hash_password(passwd: str) -> str:
        return pwd_context.hash(passwd)
    
    @staticmethod
    def verify_password(hashedPasswd: str, inputPasswd) -> bool:
        return pwd_context.verify(inputPasswd, hashedPasswd)