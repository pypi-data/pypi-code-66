'''
indexPy
Python3 wrapper for PyPI API.
Copyright (C) Angel Carias. 2020.
'''
# Required imports
import json
import requests as req

# --- Classes ---

# Exception
class PackageNotFound(Exception):
    '''
    Exception that is raised when Python package is not found.
    '''
    def __init__(self, pkgName) -> None:
        self.pkgName = pkgName
        super(PackageNotFound, self).__init__(f"Package '{self.pkgName}' not found.")

# Main API
class MainAPI:
    '''
    Main part of API. Requests JSON data from PyPI.
    This function is used by indexPy for other classes to access data.
    It is NOT meant to be accessed by the user.
    '''
    def __init__(self, packageName):
        self.pkgName = packageName
        infoAccess = req.get(f"https://pypi.org/pypi/{self.pkgName}/json")

        self.dataReq = infoAccess.text.rstrip()
        
        if infoAccess.status_code == 404:
            raise PackageNotFound(self.pkgName)
        
        self.jsonData = json.loads(self.dataReq)


# Package Info
class PackageInfo:
    '''
    Package information regarding the package data and latest version
    of the package.

    Most of the variables are self-explanatory (no need to comment).
    More information is available on https://angelcarias.github.io/docs/indexpy/package-info
    '''
    def __init__(self, packageName):
        # Create instance of MainAPI()
        apiInstance = MainAPI(packageName)

        # Get package info
        self.pkgInfo = apiInstance.jsonData["info"]

        # Create variables
        self.author = self.pkgInfo["author"]
        self.authorEmail = self.pkgInfo["author_email"]
        self.bugtrackURL = self.pkgInfo["bugtrack_url"]
        
        self.classifiers = self.pkgInfo["classifiers"]
        self.description = self.pkgInfo["description"]
        self.descriptionContentType = self.pkgInfo["description_content_type"]

        self.docsURL = self.pkgInfo["docs_url"]
        self.downloadURL = self.pkgInfo["download_url"]
        self.downloads = self.pkgInfo["downloads"]
        self.homePage = self.pkgInfo["home_page"]

        self.keywords = self.pkgInfo["keywords"]
        self.license = self.pkgInfo["license"]
        self.maintainer = self.pkgInfo["maintainer"]
        self.maintainerEmail = self.pkgInfo["maintainer_email"]
        self.name = self.pkgInfo["name"]
        self.url = self.pkgInfo["package_url"]

        self.platform = self.pkgInfo["platform"]
        self.projectURL = self.pkgInfo["project_url"]
        self.projectURLs = self.pkgInfo["project_urls"]
        self.releaseURL = self.pkgInfo["release_url"]

        self.dependencies = self.pkgInfo["requires_dist"]
        self.requiresPython = self.pkgInfo["requires_python"]
        self.summary = self.pkgInfo["summary"]
        self.version = self.pkgInfo["version"]
        self.yanked = self.pkgInfo["yanked"]
        self.yankedReason = self.pkgInfo["yanked_reason"]


# Release Info
class ReleaseInfo:
    '''
    Release information regarding a certain version of the package.

    Most of the variables are self-explanatory (no need to comment).
    More information is available on https://angelcarias.github.io/docs/indexpy/release-info
    '''
    def __init__(self, packageName, packageVersion = None): 
        # Get version for latest release from PackageInfo()
        self.latestVersion = PackageInfo(packageName).version
        
        # Create instance of MainAPI()
        apiInstance = MainAPI(packageName)

        # Set package version
        if packageVersion is None:
            packageVersion = self.latestVersion
        
        # Local variable for shortening line length
        pkgVersion = packageVersion

        # Get package release info
        self.pkgReleases = apiInstance.jsonData["releases"]

        # Create variables
        self.releases = [key for key in self.pkgReleases.keys()]
        self.files = len(self.pkgReleases[pkgVersion])
        
        self.commentText = lambda file: self.pkgReleases[pkgVersion][file]["comment_text"]
        self.digests = lambda file: self.pkgReleases[pkgVersion][file]["digests"]
        self.downloads = lambda file: self.pkgReleases[pkgVersion][file]["downloads"]
        self.filename = lambda file: self.pkgReleases[pkgVersion][file]["filename"]

        self.hasSignature = lambda file: self.pkgReleases[pkgVersion][file]["has_sig"]
        self.md5_signature = lambda file: self.pkgReleases[pkgVersion][file]["md5_digest"]
        self.packageType = lambda file: self.pkgReleases[pkgVersion][file]["packagetype"]

        self.pythonVersion = lambda file: self.pkgReleases[pkgVersion][file]["python_version"]
        self.requiresPy = lambda file: self.pkgReleases[pkgVersion][file]["requires_python"]

        self.fileSize = lambda file: self.convertBytesToReadable(self.pkgReleases[pkgVersion][file]["size"])
        self.uploadTime = lambda file: self.pkgReleases[pkgVersion][file]["upload_time"]
        self.uploadTime_ISO8601 = lambda file: self.pkgReleases[pkgVersion][file]["upload_time_iso_8601"]

        self.url = lambda file: self.pkgReleases[pkgVersion][file]["url"]
        self.yanked = lambda file: self.pkgReleases[pkgVersion][file]["yanked"]
        self.yankedReason = lambda file: self.pkgReleases[pkgVersion][file]["yanked_reason"]
    
    # Function for converting bytes to EIC-standard readable sizes (MiBs, GiBs, ...)
    def convertBytesToReadable(self, num):
        stepUnit = 1024

        for suffix in ["B", "KiB", "MiB", "GiB", "TiB"]:
            if num < stepUnit:
                return "%3.1f %s" % (num, suffix)
            num /= stepUnit
