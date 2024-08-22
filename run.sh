set -e 
export PYTHONDONTWRITEBYTECODE='1'
export FLASK_APP=core/server.py
export verification_token_key='verification'
export otp_verify_header_key='otpverify'
export authorization_secret_key='authorizationtoken'
export authorization_header_key='auth'
export forget_token_key='Forget'

# flask db init
# flask db stamp heads
# flask db migrate -m "Initial migration."
# flask db upgrade

# Run server
gunicorn -c gunicorn_config.py core.server:app
