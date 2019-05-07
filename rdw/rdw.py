#!/usr/bin/python

"""
RDW API Python Package version 3.0.0 Eelco Huininga 2019
Retrieves information on cars registered in the Netherlands.
"""

import json
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


class RdwException(Exception):
    pass

                
class Rdw(object):
    """
    Interface class for the RDW API's.
    """

    _RDWAPI_BASE_URL = 'https://opendata.rdw.nl/resource/{}.json?'
    _RDWAPI_TERUGROEP_ACTIE_WEBLINK = 'https://terugroepregister.rdw.nl/Pages/Terugroepactie.aspx?mgpnummer={}'

    _RDWAPI_GEBREKEN = 'tbph-ct3j'
    _RDWAPI_GECONSTATEERDE_GEBREKEN = '2u8a-sfar'
    _RDWAPI_GEKENTEKENDE_VOERTUIGEN = 'm9d7-ebf2'
    _RDWAPI_TERUGROEP_ACTIE = 'af5r-44mf'
    _RDWAPI_TERUGROEP_ACTIE_RISICO = '9ihi-jgpf'
    _RDWAPI_TERUGROEP_ACTIE_STATUS = 't49b-isb7'
    _RDWAPI_TERUGROEP_INFORMEREN_EIGENAAR = '223d-3w9w'
    _RDWAPI_TOEGEVOEGDE_OBJECTEN = '5bwx-4xqb'

    _current_status_code = None

    def __init__(self):
        """
        Initiates the class.
        """
        self._current_status_code = None

    def get_deficiency_data(self, gebrek_identificatie):
        """
        Get data from the RDW Gebreken API
        :param gebrek_identificatie: RDW deficiency identification code
        :return: A JSON list containing the RDW APK data
        """

        return self._get_rdwapi_data(self._RDWAPI_GEBREKEN, 'gebrek_identificatie={}'.format(gebrek_identificatie))

    def get_found_deficiencies_data(self, kenteken):
        """
        Get data from the RDW Geconstateerde Gebreken API
        :param kenteken: License plate ID
        :return: A JSON list containing the RDW APK data
        """

        return self._get_rdwapi_data(self._RDWAPI_GECONSTATEERDE_GEBREKEN, 'kenteken={}'.format(kenteken))

    def get_vehicle_data(self, kenteken):
        """
        Get data from the RDW Gekentekende Voertuigen API
        :param kenteken: License plate ID
        :return: A JSON list containing the RDW APK data
        """

        return self._get_rdwapi_data(self._RDWAPI_GEKENTEKENDE_VOERTUIGEN, 'kenteken={}'.format(kenteken))

    def get_recall_data(self, referentiecode_rdw):
        """
        Get data from the RDW Terugroep Actie API
        :param referentiecode_rdw: RDW reference code
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._get_rdwapi_data(self._RDWAPI_TERUGROEP_ACTIE, 'referentiecode_rdw={}'.format(referentiecode_rdw))

    def get_recall_risk_data(self, referentiecode_rdw):
        """
        Get data from the RDW Terugroep Actie Risico API
        :param referentiecode_rdw: RDW reference code
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._get_rdwapi_data(self._RDWAPI_TERUGROEP_ACTIE_RISICO, 'referentiecode_rdw={}'.format(referentiecode_rdw))

    def get_recall_status_data(self, kenteken):
        """
        Get data from the RDW Terugroep Actie Status API
        :param kenteken: License plate ID
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._get_rdwapi_data(self._RDWAPI_TERUGROEP_ACTIE_STATUS, 'kenteken={}'.format(kenteken))

    def get_recall_owner_notification(self, referentiecode_rdw):
        """
        Get data from the RDW Terugroep Informeren Eigenaar API
        :param referentiecode_rdw: RDW reference code
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._get_rdwapi_data(self._RDWAPI_TERUGROEP_INFORMEREN_EIGENAAR, 'referentiecode_rdw={}'.format(referentiecode_rdw))

    def get_recall_info_weblink(self, referentiecode_rdw):
        """
        Get data from the RDW Terugroep Informeren Eigenaar API
        :param referentiecode_rdw: RDW reference code
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._RDWAPI_TERUGROEP_ACTIE_WEBLINK.format(recall['referentiecode_rdw'])

    def get_added_objects_data(self, kenteken):
        """
        Get data from the RDW Toegevoegde Objecten API
        :param kenteken: License plate ID
        :return: A JSON list containing the RDW APK data
        """

        return self._get_rdwapi_data(self._RDWAPI_TOEGEVOEGDE_OBJECTEN, 'kenteken={}'.format(kenteken))

    def _get_rdwapi_data(self, endpoint, query):
        """
        Get data from one of the RDW API endpoints
        :param endpoint: RDW endpoint
        :param query: Query to send to the endpoint
        :return: A JSON list containing the RDW data
        """

        url = self._RDWAPI_BASE_URL.format(endpoint) + query

        try:
            file = urlopen(url)
            result = file.read()
            file.close()
        except:
            raise(RdwException("RDW: Unable to connect to RDW API endpoint %s", endpoint))
            return None

        """ Check if the RDW API webserver returned a valid HTTP status code """
        self._current_status_code = file.getcode()

        if self._current_status_code != 200:
            raise(RdwException("RDW: Got an invalid HTTP status code {} from RDW API endpoint {}".format(self._current_status_code, endpoint)))
            return None

        """ Check if the RDW API returned valid JSON data """
        try:
            data = json.loads(result)
        except:
            raise(RdwException("RDW: Got invalid JSON data from RDW API endpoint {}. Is the query {} correct?".format(endpoint, query)))
            data = None

        """ Check if the RDW API returned an error """
        if 'error' in data:
            raise(RdwException("RDW: RDW API endpoint {} returned an error: {}".format(endpoint, data.message)))
            data = None            
            
        return data
