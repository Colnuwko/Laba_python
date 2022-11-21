import csv
import os
from tqdm import trange
file_name = "test_csv.csv"

# Запись в файл
os.chdir("Dataset")
out_directory = os.path.dirname(__file__)
with open(file_name, mode="w") as w_file:
    writer = csv.writer(w_file, dialect='excel', delimiter=",", lineterminator="\r")
    writer.writerow(("absolut path", "relativ path", "quote"))  # Заголовки столбца
    for star in trange(1, 6):
        directory = os.path.join(out_directory, "dataset", str(star))
        for dirs, folder, files in os.walk(directory):
            for element in files:
                writer.writerow([str(dirs) + "/" + element, "dataset" + '/' + str(star) + "/" + element, star])

