import pywikibot
import numpy as np

site_pedia = pywikibot.Site('en', 'wikipedia')
site_data = pywikibot.Site('wikidata', 'wikidata')
repo = site_data.data_repository()


class KB:
    #returns flattened array of related words to query
    @staticmethod
    def query_exp_array(keyword, max_output_number = 50):
        array = np.array(KB.wikipedia_search(keyword, max_output_number))
        return array.flatten()

    #returns string comprised of related terms/expansion of query
    @staticmethod
    def query_exp_str(keyword, max_output_number = 50):
        array = KB.query_exp_array(keyword, max_output_number)
        return ' '.join(array.tolist())

    @staticmethod
    def wikipedia_search(keyword, max_output_number = 50):
        page = pywikibot.Page(site_pedia, keyword)
        item = pywikibot.ItemPage.fromPage(page)
        item_dict = item.get()
        clm = item_dict['claims']
        property_list = list(clm.keys())
        property_list = KB.quick_sort(property_list)
        result = []
        for i in range(min(len(property_list), max_output_number)):
            for j in clm[property_list[i]]:
                result.append([KB.get_property_name_by_ID(property_list[i]), j.getTarget()])
                try:
                    result[-1][1] = result[-1][1].get()['labels']['en']
                except:
                    pass
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
            if int(i[1:]) < int(pivot[1:]):
                left.append(i)
            else:
                right.append(i)
        return KB.quick_sort(left) + [pivot] + KB.quick_sort(right)