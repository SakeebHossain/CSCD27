from seleniumrequests import PhantomJS

PROTOCOL = "http"
HOST = "10.0.0.2"
PORT = "80"
BASE = PROTOCOL + "://" + HOST + ":" + PORT

alice = {
    'email': 'alice@example.com',
    'password': 'pass4alice!'
}

driver = PhantomJS(service_log_path='/home/seluser/ghostdriver.log')
driver.request('POST', BASE + '/signin.php', data=alice)
driver.request('GET', BASE + '/')
