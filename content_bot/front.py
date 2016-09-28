from seleniumrequests import Firefox
import random

webdriver = Firefox()
webdriver.get('https://link')
links = webdriver.execute_script("function get_links() {var arr=[];var top = $('a[name=intresting]').offset().top;$('.post__body_full li a').each(function () {var elementOffset = $(this).offset().top; if(elementOffset < top){arr.push({link: $(this).attr('href'), text: $(this).text() })}}); return arr;} return get_links()")

random.shuffle(links)
with open("front_content.txt", "a", encoding='utf8', errors = 'ignore') as myfile:
        for item in links:
            string = item['link'] + ' ' + item['text']
            myfile.write("%s\n" % string)

print(links)
