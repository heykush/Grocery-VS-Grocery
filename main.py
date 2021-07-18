from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from itertools import chain
import pandas as pd


driver = webdriver.Chrome(
    r"C:\Users\gkush\Downloads\Compressed\chromedriver_win32_3\chromedriver.exe"
)
url = "https://grofers.com/categories"
driver.get(url)

content = driver.page_source.encode("utf-8").strip()
soup = BeautifulSoup(content, "html.parser")

categories = soup.find(
    ("div", {"class": "gr-6@tablet gr-6@desktop"})
    and ("div", {"class": "gr-6@tablet gr-6@desktop store-categories-list__right"})
)
sleep(2)
loc = driver.find_element_by_xpath(
    "//*[@class='btn location-box mask-button']").click()
sleep(5)

mainlinks = []
pplink = []
aa = []
bb = []
xx = []
zz = []
gg = []
hh = []
listt = []
name = []
hrefs = []
sublist = []
hrefsa = []


def all_pro():
    mainname = driver.find_element_by_class_name(
        "category-navs__current"
    )
    subcat = mainname.text
    hh.append(subcat)
    print("\n", subcat, "\n==============\n")

    product = []
    final = []
    productgroup = driver.find_elements_by_xpath(
        '//*[@class="products products--grid"]'
    )

    for u in productgroup:
        # for links in p:
        linaa = u.find_elements_by_tag_name("a")
        for oaa in linaa:
            plink = oaa.get_attribute("href")
            pplink.append(plink)
        g = u.find_elements_by_class_name("product__wrapper")
        product.extend(g)
        # print(product)
        sleep(2)

        for p in product:
            namee = p.find_elements_by_class_name(
                "plp-product__name--box"
            )
            for g in namee:
                nameee = g.text
                aa.append(nameee)

            club = p.find_elements_by_class_name(
                "plp-product__non-member-price "
            )
            if len(club) == 0:
                a = "Not Available"
                bb.append(a)
                # print(bb)
            else:
                for h in club:
                    Clubprice = h.text
                    bb.append(Clubprice)
                    # print(bb)

            pp = p.find_elements_by_class_name(
                "plp-product__quantity")
            for v in pp:
                ppp = v.text
                xx.append(ppp)
            price = p.find_elements_by_class_name(
                "plp-product__price--new"
            )
            for ll in price:
                prices = ll.text
                zz.append(prices)
            final = chain(namee, pp, price, club)

            # lll = "https://grofers.com" + links["href"]
            # alllink.append(lll)
        for uu in final:
            print(uu.text, end="\n")
        df = pd.DataFrame()
        # df["Main-Categorie"] = pd.Series(maincat)
        # df["Sub-Categorie"] = pd.Series(subcat)
        df["Product-Name"] = pd.Series(aa)
        df["Quantity"] = pd.Series(xx)
        df["Price"] = pd.Series(zz)
        df["Club-Price"] = pd.Series(bb)
        df["links"] = pd.Series(pplink)
        print(df)
        # df.to_csv("grocery.csv", index=False)


for link in categories.find_all("a", href=True)[1:20]:
    l = ["https://grofers.com" + link["href"]]
    # print(l)
    mainlinks.extend(l)
# print(mainlinks)

for j in mainlinks:
    driver.get(j)
    # print(j)
    itemlist = driver.find_elements_by_class_name("category-list")
    for b in itemlist:
        c = b.find_elements_by_class_name(
            "category-list__item"
        ) or b.find_elements_by_class_name("category-list__item no-child")
        listt.extend(c)

        # print(b)
        for k in c:
            lin = k.find_elements_by_tag_name("a")
            for o in lin:
                href = o.get_attribute("href")
                hrefs.append(href)
        print(hrefs)

        for z in hrefs[1:]:
            driver.get(z)
            print(z)
            sleep(3)

            subitemlist = driver.find_elements_by_xpath(
                "//*[@class='category-sub-list list-unstyled show-el']"
            )

            if len(subitemlist) == 0:
                all_pro()
            else:
                for m in subitemlist:
                    catename = driver.find_element_by_class_name(
                        "category-item-details")
                    maincat = catename.text
                    gg.append(maincat)

                    print("\n", maincat, "\n==============\n")
                    n = m.find_elements_by_class_name(
                        "category-list__sub-item")
                    sublist.extend(n)
                    for ka in n:
                        lina = ka.find_elements_by_tag_name("a")
                        for oa in lina:
                            hrefa = oa.get_attribute("href")
                            hrefsa.append(hrefa)
                    # print(sublist)
                    # print(list(hrefsa))
                    for x in hrefsa:
                        driver.get(x)
                        all_pro()
                        sleep(5)
                hrefsa.clear()
        hrefs.clear()
