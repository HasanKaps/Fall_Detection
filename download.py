import requests

Fall_Folder = "Datasets/Fall Sequences"

ADL_Folder = "Datasets/ADL Sequences"

URL= "http://fenix.univ.rzeszow.pl/~mkepski/ds/data"


# Fall Sequences Code

"""

for count in range(1, 31):
    for cam_count in range(0,2):

        leading = "{:02d}".format(count)
        new_url = f"{URL}/fall-{leading}-cam{cam_count}"

        response = requests.get(new_url)

        open(f"{Fall_Folder}/fall-{leading}-cam{cam_count}", "wb").write(response.content)
        print(f"Downloaded {new_url}")

"""

# ADL Sequences Code


for count in range(1, 41):
    for cam_count in range(0,1):

        leading = "{:02d}".format(count)
        new_url = f"{URL}/adl-{leading}-cam{cam_count}"

        response = requests.get(new_url)

        open(f"{ADL_Folder}/adl-{leading}-cam{cam_count}", "wb").write(response.content)
        print(f"Downloaded {new_url}")
