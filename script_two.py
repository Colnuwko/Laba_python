import csv
import os
from tqdm import tqdm
file_name = "test_csv.csv"
file_name_two = "test_csv_two.csv"
from tqdm.notebook import tqdm_notebook

os.chdir("Dataset")
out_directory = os.path.dirname(__file__)
with open(file_name_two, mode="w") as w_file:
    writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
    writer.writerow(("absolut path", "relativ path", "quote"))  # Заголовки столбца
with open("test_csv.csv", "r") as fh:
    reader = csv.reader(fh)
    spisok = list(reader)  # надо сделать приведение к list, так как сsv вернет итератор
    if not os.path.isdir("dataset_two"):
        os.makedirs("dataset_two")
    pbar = tqdm(spisok, ncols=100, colour='green')
    content = False
    for element in pbar:
        if content:
            with open(element[0], "rb") as f:
                text = f.read()
                namefile = element[1].split("/")
            with open(os.path.join("dataset_two", element[2] + "_" + namefile[2]), "wb") as f:
                f.write(text)
            with open(file_name_two, mode="a") as w_file:
                writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
                writer.writerow([str(out_directory) + "/Dataset/dataset_two/" + element[2] + "_" + namefile[2], "Dataset/dataset_two/" + element[2] + "_" + namefile[2],  element[2]])

        content = True