import abstra.forms as af
import abstra.workflows as aw
from extension import amazon_search, flipkart_search

# With Abstra Forms, it's easy to build user interfaces
name = af.read("👋 Hello there! What is your name?")

# Different kinds of input and output widgets are available
product_page = (
    af.Page()
        .display(f"🎉 Welcome, {name}!")
        .read("💡 Please enter a product name", key="name")
        .run("Next")
)
product_name = product_page["name"]

amazon_price, amazon_image = amazon_search(product_name)
flipkart_price, flipkart_image = flipkart_search(product_name)

page = af.Page()
page.display("🚀 Below is the price comparison:")
if amazon_price == '0':
    page.display(f"😔 Product not found on Amazon")
    page.display_image("https://png.pngtree.com/png-vector/20190917/ourmid/pngtree-not-found-outline-icon-vectors-png-image_1737857.jpg", full_width=False)
else:
    page.display(f"Amazon price: {amazon_price}")
    page.display_image(amazon_image, full_width=False, subtitle="Amazon")
if flipkart_price == '0':
    page.display(f"😔 Product not found on Flipkart")
    page.display_image("https://png.pngtree.com/png-vector/20190917/ourmid/pngtree-not-found-outline-icon-vectors-png-image_1737857.jpg", full_width=False)
else:
    page.display(f"Flipkart price: {flipkart_price}")
    page.display_image(flipkart_image, full_width=False, subtitle="Flipkart")
page.run()
