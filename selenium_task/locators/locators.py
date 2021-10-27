class LocatorsXPath:
    # add_to_cart = "/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/div[2]/a[1]/span"
    # cart_quantity = "/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a/span[1]"
    # cart_button = "/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a"
    # empty_cart = "/html/body/div/div[2]/div/div[3]/div/p"
    # remove_item = "/html/body/div/div[2]/div/div[3]/div/div[2]/table/tbody/tr/td[7]/div/a/i"
    # close_item_popup = "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/span"

    card = '#center_column > ul > li:nth-child(1) > div > div.right-block'
    hover = '#center_column > ul > li:nth-child(2) > div > div.right-block > div.button-container > ' \
            'a.button.ajax_add_to_cart_button.btn.btn-default > span '
    remove_popup = "cross"
    cart_hover = '#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a'
    quantity = 'ajax_cart_quantity'
    