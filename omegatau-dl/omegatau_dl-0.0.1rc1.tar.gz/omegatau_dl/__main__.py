# Copyright (c) Marcel Johannfunke
# Licensed under the GPLv3 licence
# https://www.gnu.org/licenses/gpl-3.0.en.html

import re
import requests
import os
import os.path
import sys

URL_ARCHIVE = "http://omegataupodcast.net/download-archive/"
DL_RE = re.compile("[\"']https?://[^>]*?omegatau-?[0-9]+[^>]*?\.mp3[\"']")
NUMBER_RE = re.compile("[0-9_]+")
URL_EPISODE = "http://omegataupodcast.net/"

# This is just a band-aid for wrong episode urls
MANUAL_URLS = {
    # http://omegataupodcast.net/134-high-energy-neutrinos-and-the-icecube-neutrino-observatory/
    135: '"http://traffic.libsyn.com/omegataupodcast/omegatau-135-highEnergyNeutrinosAndIceCube.mp3"',
    # Normal lookup for 150 leads to episode 150.5
    # http://omegataupodcast.net/150-the-european-extremely-large-telescope/
    150: '"http://traffic.libsyn.com/omegataupodcast/omegatau-150-theEELT.mp3"',
    # http://omegataupodcast.net/150-5-controlling-the-elt/
    150.5: '"http://traffic.libsyn.com/omegataupodcast/omegatau-150_5-eltControl.mp3"',
    # http://omegataupodcast.net/347-photosynthese/
    # Typo in filename
    347: '"https://traffic.libsyn.com/secure/omegataupodcast/omegtau-347-photosynthese.mp3"',
}


def extract_number(url):
    # assumption: first number in link is the episode number
    m = NUMBER_RE.search(url)
    number = m.group(0)
    if '_' in number:
        return float(number.replace('_', '.'))
    else:
        return int(m.group(0))


def number_idxs(url):
    m = NUMBER_RE.search(url)
    return m.span()


def download_file(url, filename):
    nchunks = 0
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        print("Downloading {} ".format(filename), end='', flush=True)
        try:
            with open(filename, 'wb') as f:
                # 1 MiB chunks
                for chunk in r.iter_content(chunk_size=1024*1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        nchunks += 1
                        # send . to show progress
                        if nchunks % 4 == 0:
                            print('.', end='', flush=True)
            print(" done")
        except KeyboardInterrupt:
            print("\nExiting...")
            os.remove(filename)
            print("Removed incomplete file")
            sys.exit(0)


def scrape_missing_episodes(missing):
    print("Trying to find downloads for missing episodes ...")
    missdict = {}
    stillmissing = []
    for number in missing:
        # Overwrite the existing line
        print("\rLooking for episode number {} ({}/{} missing episodes)".format(
            number, len(missdict)+len(stillmissing)+1, len(missing)), end="")
        if number in MANUAL_URLS:
            missdict[number] = MANUAL_URLS[number]
            continue
        # Look for link in page
        pagetext = requests.get(URL_EPISODE+str(number)).text
        dl_url = DL_RE.search(pagetext)
        # link not found
        if not dl_url:
            stillmissing.append(number)
            continue
        dl_url = dl_url.group(0)
        missdict[number] = dl_url

    print("")
    if stillmissing:
        print("Still missing episodes: {}".format(", ".join(map(str, stillmissing))))
        if missdict:
            print("Found download links for episodes: {}".format(", ".join(map(str, missdict.keys()))))
    else:
        print("Found download links for all episodes! =)")
    return missdict


def main():
    # Graceful exit on CTRL+C while looking for download links
    try:
        print("This script will ONLY download numbered episodes, you need to download special episodes manually.")
        # numbers of episodes that are downloaded
        files = [f for f in os.listdir(".") if f.startswith('omegatau')]
        local_numbers = set(map(extract_number, files))

        print("Found {} episodes already downloaded.".format(len(files)))

        # Get text of archive webpage
        print("Getting episode list ...")
        pagetext = requests.get(URL_ARCHIVE).text

        # Parse all available download urls
        dl_urls = DL_RE.findall(pagetext)

        # put numbers on webpage in list
        numbers = list(map(extract_number, dl_urls))
        maxnr = max(numbers)
        print("Found {} episodes in Archive, newest episode is {}".
              format(len(set(numbers)), maxnr))
        # List missing episodes
        all_numbers = list(range(1, maxnr+1)) + [150.5]
        missing = [x for x in all_numbers if x not in numbers]
        # Replace episode number 336 with 150.5 (was published as 150.5)
        missing.remove(336)

        print("Missing episodes in Archive: {}".format(", ".join(map(str, missing))))

        # Check if some missing episodes are downloaded
        # then no need to find download link
        missing_but_downloaded = []
        for miss in missing:
            if miss in local_numbers:
                missing_but_downloaded.append(miss)

        if len(missing) == len(missing_but_downloaded):
            print("All missing episodes are already downloaded.")
        else:
            still_missing = [miss for miss in missing if miss not in missing_but_downloaded]

            if (missing_but_downloaded):
                print("Already downloaded missing episodes: {}".
                      format(", ".join(map(str, missing_but_downloaded))))
                print("Remaining episodes: {}".format(", ".join(map(str, still_missing))))

            missdict = scrape_missing_episodes(still_missing)
            for num, dl in missdict.items():
                numbers.append(num)
                dl_urls.append(dl)

    except KeyboardInterrupt:
        print("\nExiting ...")
        sys.exit(0)

    print("\nStarting downloads ...\n")

    for dl_url, number in zip(dl_urls, numbers):
        # Already have it downloaded
        if number in local_numbers:
            continue
        # Get number to put in 4 digit format
        start, end = number_idxs(dl_url)
        # it seems XXr is a repaired episode. strip the r
        after_number_char = dl_url[end]
        endstr = dl_url[end+1:-1] if after_number_char == 'r' else dl_url[end:-1]
        # set local filename to 4 digit
        try:
            filename = "omegatau-" + "{:04d}".format(number) + endstr
        except ValueError:
            filename = "omegatau-" + "{:04.1f}".format(number).replace('.', '_') + endstr
        download_file(dl_url[1:-1], filename)


if __name__ == "__main__":
    main()
 
