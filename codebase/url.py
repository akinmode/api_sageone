#!/usr/bin/python3
"""
    Format URL Structure
    The service URLs are built up as follows:

    [API URL]/api/[ver]/[service name]/[method name]/[ID (when required)]?[required query string parameters]

    VERSION
    1.0
"""

class SageOneUrls:
    """SageOneUrls"""

    _apiUrl = "https://accounting.sageone.co.za"
    _apiVersion = "1.1.2"
    _accessUrl = ""

    def __init__(self):
        pass

    def setRequestUrl(self, apiserv, apimeth, options, apino = 0):
        """
            Sets the access url with all the necessary components following the format below
            [API URL]/api/[ver]/[service name]/[method name]/[ID (when required)]?[required query string parameters]
        """
        opt_str = [str(key)+ "=" +str(value) for key, value in options.items()]

        if apino <= 0:
            self._accessUrl = '/'.join([self._apiUrl, "api", self._apiVersion, apiserv, apimeth]) + "?" + "&".join(opt_str)
        else:
            self._accessUrl = '/'.join([self._apiUrl, "api", self._apiVersion, apiserv, apimeth, str(apino)]) + "?" + "&".join(opt_str)
    
    def getRequestUrl(self):
        """
            Returns the generated url according to the api documentation
        """
        return self._accessUrl
