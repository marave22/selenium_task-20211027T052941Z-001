class LocatorsXPath:
    card = '#center_column > ul > li:nth-child(1) > div > div.right-block'
    hover = '#center_column > ul > li:nth-child(2) > div > div.right-block > div.button-container > ' \
            'a.button.ajax_add_to_cart_button.btn.btn-default > span '
    add_to_cart = '#homefeatured > li.ajax_block_product.col-xs-12.col-sm-4.col-md-3.first-in-line.first-item-of' \
                  '-tablet-line.first-item-of-mobile-line > div > div.right-block > div.button-container > ' \
                  'a.button.ajax_add_to_cart_button.btn.btn-default '
    remove_popup = '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/span'
    cart_hover = "/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/div[2]/a[1]"
    cart_quantity = "/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a/span[1]"
    remove_items = '/html/body/div/div[2]/div/div[3]/div/div[2]/table/tbody/tr/td[7]/div/a/i'
    empty_message = '/html/body/div/div[2]/div/div[3]/div/p'
