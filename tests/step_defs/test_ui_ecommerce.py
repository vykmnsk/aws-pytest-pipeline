from urllib.parse import urlencode
from pytest_bdd import scenario, scenarios, given, when, then, parsers


login_email_box = 'input[id="Email"]'
login_password_box = 'input[id="Password"]'
login_button = 'input[value="Log in"]'

search_box = 'input[id="small-searchterms"]'
search_button = 'input[value="Search"]'
add_to_cart_button = 'input[value="Add to cart"]'
price_div = 'div.prices'


scenarios('../features/LoginAndAddToCart.feature')

@given("I don't have valid username and password", 
       target_fixture="user_pwd_invalid")
def user_pwd_invalid():
    return ('invalid@example.email', 'invalid_password')

@when("I try to login")
def do_login(sb, user_pwd_invalid):
    user, password = user_pwd_invalid
    login_url = f'{sb.get_current_url()}login'
    sb.open(login_url)
    sb.update_text(login_email_box, user)
    sb.update_text(login_password_box, password)
    sb.click(login_button)
    
@then(parsers.parse('I get message "{msg}"'))
def check_text(sb, msg):
    sb.assert_text(msg)


@scenario(
    "../features/LoginAndAddToCart.feature",
    "Product Search",
    example_converters=dict(product=str, price=str)
)

@given('The site has product <product> with price <price>')
def product_price(product, price):
    # perhaps check product existence via API
    assert isinstance(product, str)
    assert isinstance(price, str)
    pass

@when('I search for <product>')
def do_search(sb, product):
    sb.update_text(search_box, product)
    sb.click(search_button)
    
@then('I can find <product> page')
def check_header(sb, product):
    sb.assert_text(product, 'h2')
        
@then('I can see the price <price>')
def check_price(sb, price):
    actual_price = sb.get_text(price_div)
    assert actual_price == price

 
@scenario(
    "../features/LoginAndAddToCart.feature",
    "Add to shopping cart",
    example_converters=dict(product=str, price=str)
)
    
@when('I am on the <product> page')
def load_product_page(sb, product):
    params = {'q': product }
    product_url = f'{sb.get_current_url()}search?{urlencode(params)}'
    sb.open(product_url)

@then('I can add the product to the shopping cart')    
def add_to_shopping_cart(sb):
    sb.click(add_to_cart_button)
    sb.assert_text('The product has been added to your shopping cart')