class userLogin:

    def __init__(self, userName, password, city_employment, web_server, role, signs):
        self.setUsername(userName)
        self.setPassword(password)
        self.setCity(city_employment)
        self.setWebServer(web_server)
        self.setRole(role)
        self.setSigns(signs)

    def setUsername(self, userName):
        if userName == "" or userName == None:
            raise NameError("Username: empty or null")
        else:
            self.username = userName

    def setPassword(self, password):
        if password == "" or password == None:
            raise KeyError("Password: empty or null")
        else:
            self.password = password

    def setCity(self, city):
        if city == "" or city == None:
            raise ValueError("City: empty or null")
        else:
            self.city = city

    def setWebServer(self, web_server):
        if web_server == "" or web_server == None:
            raise ValueError("Web Server: empty or null")
        else:
            self.webServer = web_server

    def setRole(self, role):
        if role == "" or role == None:
            raise ValueError("Role: empty or null")
        else:
            self.role = role

    def setSigns(self, signs):
        self.signs = signs
