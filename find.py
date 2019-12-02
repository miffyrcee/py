import os
import re


def none_filter(text, pattern):
    return list(filter(None, re.split(pattern, text)))


# start = str_emaz.find('sa', start=start, end=end)
def main():
    fn = os.path.join(os.path.dirname(__file__),
                      'COMM7330_Quiz05_datasetS2.csv')

    with open(fn, 'rb') as fr:
        exam = fr.read().decode('utf-8', 'ignore').strip()
        exam_list = none_filter(exam, ' |\?|\r|\n|\!|,|\)|\'')
        result_0 = [e for e in exam_list if e[0] == '@']
        print(result_0)
        result_1 = [e for e in exam_list if e[0] == '#']
        print(result_1)
        result_2 = [e for e in exam_list if e[:4] == 'http']
        print(result_2)


if __name__ == "__main__":
    main()
