class Config:
    def __init__(self, env):
        self.base_url = {
            'test': 'https://zapier.com/home'
        }[env]