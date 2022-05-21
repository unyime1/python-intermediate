import random
import string

import redis


class OTPManager:
    """Manage user OTP."""

    redis = redis.Redis(host="redis", port=6379, db=1)

    @staticmethod
    def generate_token(num: int = 9) -> str:
        """Generate random token."""
        return "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(num)
        )

    @classmethod
    def create_otp(cls, user_id: str, expires: int = 900):
        """Create OTP"""
        otp = cls.generate_token()
        while cls.redis.exists(otp):
            otp = cls.generate_token()
        cls.redis.set(otp, user_id, ex=expires)
        return otp

    @classmethod
    def get_otp_user(cls, otp: str):
        """Return the owner of OTP"""
        if cls.redis.exists(otp):
            return cls.redis.get(otp).decode("utf-8")
        return None


otp_manager = OTPManager()
