import pywikibot
site_pedia = pywikibot.Site('en','wikipedia')
site_data = pywikibot.Site('wikidata','wikidata')
repo = site_data.data_repository()
class KB:
    @staticmethod
    def wikipedia_search(keyword,max_output_number = 10):
        page = pywikibot.Page(site_pedia,keyword)
        item = pywikibot.ItemPage.fromPage(page)
        item_dict = item.get()
        clm = item_dict['claims']
        property_list = list(clm.keys())
        property_list = KB.quick_sort(property_list)
        result = []
        for i in range(min(len(property_list),max_output_number)):
            result.append([KB.get_property_name_by_ID(property_list[i]),clm[property_list[i]][0].getTarget()])
        return result

    @staticmethod
    def get_property_name_by_ID(ID):
        property = pywikibot.PropertyPage(repo, ID)
        property_dict = property.get()
        return property_dict['labels']['en']

    @staticmethod
    def quick_sort(p_list):
        if len(p_list) == 0:
            return []
        pivot = p_list[0]
        left = []
        right = []
        for i in p_list[1:]:
            if int(i[1:])<int(pivot[1:]):
                left.append(i)
            else:
                right.append(i)
        return KB.quick_sort(left) + [pivot] + KB.quick_sort(right)