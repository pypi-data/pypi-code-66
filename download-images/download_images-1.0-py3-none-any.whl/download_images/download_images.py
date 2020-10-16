import urllib.request
import ssl
import os
import sys, argparse
import re
from selenium import webdriver

def getParams(sysArgs):
    """get search parameters from arguments"""
    def validDir(userDir):
        """check that the output directory is valid"""
        if os.path.exists(userDir):
            return userDir
    def validSize(size):
        """check that the user enters a valid image size"""
        valid = re.search("^[0-9]+\*[0-9]+$", size)
        if valid:
            dimensions = re.findall("[0-9]+", size)
            return dimensions
        
    parser = argparse.ArgumentParser(description="Get arguments for searching for images")
    
    parser.add_argument("-q", "--query", help="Query to search for", type=str, required=True, nargs="+")
    parser.add_argument("-l", "--limit", help="Max images to download", type=int, required=False)
    parser.add_argument("-o", "--outputDir", help="Full directory to store images in", type=validDir, required=False)
    parser.add_argument("-c", "--chromedriver", help="Full directory to the chromedriver", type=validDir, required=False)
    parser.add_argument("-epq", "--exactQuery", help="Words that must be included (e.g. bat under)", type=str, required=False)
    parser.add_argument("-oq", "--optionalQuery", help="Words that are optional (e.g. apple tree)", type=str, required=False)
    parser.add_argument("-eq", "--exceptQuery", help="Words that must not be included (e.g. cat vote)", type=str, required=False)
    sizeGroup = parser.add_mutually_exclusive_group(required=False)
    sizeGroup.add_argument("-cs", "--customSize", help="Find image of specific size", type=validSize)
    sizeGroup.add_argument("-sz", "--size", help="Find images of specific size (s, m, l, icon, >x MP, >x*y)", type=str, 
                         choices=["s", "m", "l", "i",
                                  ">2MP", ">4MP", ">6MP", ">8MP", ">10MP", ">12MP", ">15MP", ">20MP", ">40MP", ">70MP",
                                  ">400*300", ">640*480", ">800*600", ">1024*768"])
    parser.add_argument("-ar", "--aspectRatio", help="Find images of specific aspect ratio (square, tall, wide, panoramic)", type=str, required=False,
                         choices=["s", "t", "w", "p"])
    colourGroup = parser.add_mutually_exclusive_group(required=False)
    colourGroup.add_argument("-co", "--colour", help="Find images containing specific colour", type=str,
                        choices=["red", "orange", "yellow", "green", "teal", "blue", "purple", "pink", "white", "gray", "black", "brown"])
    colourGroup.add_argument("-ct", "--colourType", help="Find images of specific type", type=str,
                        choices=["full-colour", "black-and-white", "transparent"])
    parser.add_argument("-it", "--imageType", help="Type of image", type=str, required=False,
                        choices=["face", "photo", "clipart", "lineart", "animated"])
    parser.add_argument("-ft", "--fileType", help="Type of file", type=str, required=False,
                        choices=["jpg", "gif", "png", "bmp", "svg", "webp", "ico", "raw"])
    parser.add_argument("-s", "--site", help="Specific site or domain to search (e.g. example.com, .org", type=str, required=False,)
    parser.add_argument("-ss", "--SafeSearch", help="Should SafeSearch be on", type=bool, required=False, default=False, choices=[True, False])
    parser.add_argument("-ur", "--usageRights", help="Filter by usage rights", type=str, required=False,
                        choices=["CC", "Commercial", "Other"])

    args = parser.parse_args(sysArgs)
    params = vars(args)
    finalVal = ""
    for val in params["query"]:
        finalVal += val + " "
    finalVal = finalVal.strip()
    params["query"] = finalVal
    return params

def compileParams(params):
    """change the parameters into url snippets"""
    imgQuery = params["query"]
    for key, value in params.items():
        params[key] = getParamValue(key, value, imgQuery)
    return params

def getParamValue(k, v, imgQuery):
    """check if arguments are empty or not"""
    if v:
        """if not empty, convert arguments"""
        value = v
        if k == "size":
            sizeSwitcher = {
                "s":"s",
                "m":"m",
                "l":"l",
                "i":"i",
                ">2MP":"2mp",
                ">4MP":"4mp",
                ">6MP":"6mp",
                ">8MP":"8mp",
                ">10MP":"10mp",
                ">12MP":"12mp",
                ">15MP":"15mp",
                ">20MP":"20mp",
                ">40MP":"40mp",
                ">70MP":"70mp",
                ">400*300":"qsvga",
                ">640*480":"vga",
                ">800*600":"svga",
                ">1024*768":"xvga"
                }
            value = sizeSwitcher[v]
        elif k == "customSize":
            value = " imagesize:" + v[0] + "x" + v[1]
        elif k == "aspectRatio":
            ratioSwitcher = {
                "s":"iar:s",
                "t":"iar:t",
                "w":"iar:w",
                "p":"iar:p"
                }
            value = ratioSwitcher[v]
        elif k == "colourType":
            colourSwitcher = {
                "full-colour":"color",
                "black-and-white":"gray",
                "transparent":"trans"
                }
            value = colourSwitcher[v]
        elif k == "SafeSearch":
            safeSwitcher = {
                True:"active",
                False:"images"
                }
            value = safeSwitcher[v]
        elif k == "usageRights":
            typeSwitcher = {
                "CC":"sur%3Acl",
                "Commercial":"sur%3Aol",
                "Other":"sur%3Aol"
                }
            value = typeSwitcher[v]
    else:
        """if empty, set default values"""
        if k == "limit":
            value = 3
        elif k == "outputDir":
            value = (os.path.join(os.getcwd(), imgQuery))
        elif k == "chromedriver":
            value = None
        elif k == "SafeSearch":
            value = "images"
        elif k == "customSize":
            value = ""
        else:
            value = ""
    return value
     
def getSearchUrl(params):
    """format url according to parameters"""
    imgQuery = params["query"]
    exactQuery = params["exactQuery"]
    optionalQuery = params["optionalQuery"]
    exceptQuery = params["exceptQuery"]
    customSize = params["customSize"]
    imgSize = params["size"]
    aspectRatio = params["aspectRatio"]
    imgColour = params["colour"]
    colourType = params["colourType"]
    imageType = params["imageType"]
    fileType = params["fileType"]
    imgSite = params["site"]
    SafeSearch = params["SafeSearch"]
    usageRights = params["usageRights"]
    searchUrl = ("https://www.google.com/search?as_st=y&tbm=isch&" +
                 "as_q=" + imgQuery +
                 customSize +
                 "&as_epq=" + exactQuery +
                 "&as_oq=" + optionalQuery +
                 "&as_eq=" + exceptQuery +
                 "&imgsz=" + imgSize +
                 "&imgar=" + 
                 "&imgc=" + colourType +
                 "&imgcolor=" + imgColour +
                 "&imgtype=" + imageType +
                 "&cr=" + 
                 "&as_sitesearch=" + imgSite +
                 "&safe=" + SafeSearch +
                 "&as_filetype=" + fileType +
                 "&tbs=" + aspectRatio + " " + usageRights)
    return searchUrl

def getImageUrls(params, url):
    """request and read data from urls"""
        
    resultsIndex = 0
    resultsNo = 0
    
    imageCount = 0
    imageUrls = []

    maxImages = params["limit"]
    
    """initialise driver to run imgQuery"""
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument('log-level=3')
    try:
        if params["chromedriver"]:
            driver = webdriver.Chrome(executable_path=rf"{params['chromedriver']}", options=chromeOptions)
        else:
            driver = webdriver.Chrome(options=chromeOptions)
    except Exception as e:
        print("Could not find the 'chromedriver' (use the '--chromedriver' "
                  "argument to specify the path) OR Google Chrome is not "
                  "installed on your machine (exception: %s)" % e)
        sys.exit(3)
    driver.set_window_size(1024, 768)
    driver.get(url)

    def scroll(driver):
        """write procedure to scroll to bottom of page"""
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    while imageCount < maxImages:
        scroll(driver)

        """get all thumbnail elements in a list"""
        thumbnails = driver.find_elements_by_css_selector("img.Q4LuWd")
        resultsNo = len(thumbnails)
        print(resultsNo, "images found")
        if maxImages < resultsNo:
            print("Retrieving", maxImages, "urls")
        else:
            imagesToBeRetrieved = resultsIndex + resultsNo
            print("Retrieving", imagesToBeRetrieved, "urls for now...")

        for thumbnail in thumbnails[resultsIndex:resultsNo]:
            try:
                """open every thumbnail"""
                thumbnail.click()
                """search for actual image"""
                images = driver.find_elements_by_css_selector("img.n3VNCb")
                """add image url to list"""
                for image in images:
                    imgSource = image.get_attribute("src")
                    if imgSource and "http" in imgSource:
                        imageUrls.append(imgSource)
                        imageCount += 1
                        if imageCount >= maxImages:
                            print("Found",imageCount,"urls...")
                            break
                else:
                    continue
                break

            except Exception:
                continue
        else:
            print("Found", imageCount, "urls, searching for more ...")
            loadButton = driver.find_element_by_css_selector(".mye4qd")
            if loadButton:
                driver.execute_script("document.querySelector('.mye4qd').click();")

            """ move the result startpoint further down"""
            resultsIndex = resultsNo

    """close driver after query is finished"""
    driver.close()
    driver.quit()
    print("Done getting URLs")
    
    return imageUrls

def downloadImages(params, imageUrls):
    """download images from urls"""
    print("Downloading Images")
    picDir = params["outputDir"]
    imgQuery = params["query"]
    if not os.path.exists(picDir):
        os.mkdir(imgQuery)
    os.chdir(picDir)
    i = 1
    for imageUrl in imageUrls:
        try:
            with urllib.request.urlopen(imageUrl) as url:
                with open(imgQuery + ("%03d"%i) + ".jpg", "wb") as f:
                    f.write(url.read())
        except urllib.error.HTTPError:
            print("Failed on image", i, "proceeding to next")

        except urllib.error.URLError:
            print("Failed on image", i, "proceeding to next")

        except ssl.CertificateError:
            print("Failed on image", i, "proceeding to next")

        i += 1
    if i < params["limit"]:
        print("Got only", i , "images due to error")

def main(args):
    """main function which runs the entire program by taking in arguments"""
    params = getParams(args)
    params = compileParams(params)
    url = getSearchUrl(params)
    imageUrls = getImageUrls(params, url)
    downloadImages(params, imageUrls)
    os.chdir("..")
    
if __name__ == "__main__":     
    main(sys.argv[1:])
