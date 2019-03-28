import asyncio
from pyppeteer import launch

async def vk():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://vk.com/')
    username = input('\nUr username for vk.com: ')
    password = input('\nUr password for vk.com: ')
    print('\nLog in with ',username,':',password,'. Result: vk_com.png')
    await page.type('#index_email', username)
    await page.type('#index_pass', password)
    await page.waitFor(1500)
    await page.click('#index_login_button')
    await page.waitFor(5000)
    await page.screenshot({'path': 'vk_com.png'})
    await browser.close()
    raise SystemExit

async def facebook():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://facebook.com')
    username = input('\nUr username for facebook.com: ')
    password = input('\nUr password for facebook.com: ')
    print('\nLog in with ',username,':',password,'. Result: facebook_com.png')
    await page.type('#email', username)
    await page.type('#pass', password)
    await page.waitFor(1500)
    await page.click('#loginbutton')
    await page.waitFor(5000)
    await page.screenshot({'path': 'facebook_com.png'})
    await browser.close()
    raise SystemExit

while(1):
    print('Choose a social network:\n')
    c = input('1: VK.COM\n2: FACEBOOK.COM\n3: Exit\n')
    if c == '1':
        asyncio.get_event_loop().run_until_complete(vk())
    if c == '2':
        asyncio.get_event_loop().run_until_complete(facebook())
    if c == '3':
        raise SystemExit
    else: print('\nWrong input!')
