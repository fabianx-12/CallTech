"""
Migration to remove share_code column from UserProfile table
"""
from models import db

def remove_share_code_column():
    with db.engine.connect() as conn:
        conn.execute('ALTER TABLE user_profile DROP COLUMN share_code;')

if __name__ == '__main__':
    remove_share_code_column()
