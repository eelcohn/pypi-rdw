"""
RDW API Python Package version 3.0.0 Eelco Huininga 2019
Retrieves information on cars registered in the Netherlands.
"""

VERSION = '3.0.0'

from datetime import datetime, timedelta
import requests


class RdwException(Exception):
    pass

                
class Rdw(object):
    _RDW_API_BASE_URL = 'https://opendata.rdw.nl/resource/{}.json?'
    _RDW_API_GEBREKEN = 'tbph-ct3j'
    _RDW_API_GECONSTATEERDE_GEBREKEN = '2u8a-sfar'
    _RDW_API_GEKENTEKENDE_VOERTUIGEN = 'm9d7-ebf2'
    _RDW_API_TERUGROEP_ACTIE = 'af5r-44mf'
    _RDW_API_TERUGROEP_ACTIE_RISICO = '9ihi-jgpf'
    _RDW_API_TERUGROEP_ACTIE_STATUS = 't49b-isb7'
    _RDW_API_TERUGROEP_INFORMEREN_EIGENAAR = '223d-3w9w'
    _RDW_API_TOEGEVOEGDE_OBJECTEN = '5bwx-4xqb'

    """
    Interface class for the RDW API's.
    """
    _current_status_code = None

    def __init__(self, plate_id):
        """
        Initiates the sensor data with default settings if none other are set.
        :param plate_id: license plate id
        """
        self._plate_id = plate_id
        self._session = Session()

    def get_deficiency_data(self, gebrek_identificatie):
        """
        Get data from the RDW Gebreken API
        :param gebrek_identificatie: RDW deficiency identification code
        :return: A JSON list containing the RDW APK data
        """

        return self._get_rdwapi_data(_RDW_API_GEBREKEN, 'gebrek_identificatie={}'.format(gebrek_identificatie))

    def get_found_deficiencies_data(self, kenteken):
        """
        Get data from the RDW Geconstateerde Gebreken API
        :param kenteken: License plate ID
        :return: A JSON list containing the RDW APK data
        """

        return self._get_rdwapi_data(_RDW_API_GECONSTATEERDE_GEBREKEN, 'kenteken={}'.format(kenteken))

    def get_vehicle_data(self, kenteken):
        """
        Get data from the RDW Gekentekende Voertuigen API
        :param kenteken: License plate ID
        :return: A JSON list containing the RDW APK data
        """

        return self._get_rdwapi_data(_RDW_API_GEKENTEKENDE_VOERTUIGEN, 'kenteken={}'.format(kenteken))

    def get_recall_data(self, referentiecode_rdw):
        """
        Get data from the RDW Terugroep Actie API
        :param referentiecode_rdw: RDW reference code
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._get_rdwapi_data(_RDW_API_TERUGROEP_ACTIE, 'referentiecode_rdw={}'.format(referentiecode_rdw))

    def get_recall_risk_data(self, referentiecode_rdw):
        """
        Get data from the RDW Terugroep Actie Risico API
        :param referentiecode_rdw: RDW reference code
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._get_rdwapi_data(_RDW_API_TERUGROEP_ACTIE_RISICO, 'referentiecode_rdw={}'.format(referentiecode_rdw))

    def get_recall_status_data(self, kenteken, referentiecode_rdw):
        """
        Get data from the RDW Terugroep Actie Status API
        :param kenteken: License plate ID
        :param referentiecode_rdw: RDW reference code
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._get_rdwapi_data(_RDW_API_TERUGROEP_ACTIE_STATUS, 'kenteken={}&referentiecode_rdw={}'.format(kenteken, referentiecode_rdw))

    def get_recall_owner_notification(self, referentiecode_rdw):
        """
        Get data from the RDW Terugroep Informeren Eigenaar API
        :param referentiecode_rdw: RDW reference code
        :return: A JSON list containing the RDW Recall Risk data
        """

        return self._get_rdwapi_data(_RDW_API_TERUGROEP_INFORMEREN_EIGENAAR, 'referentiecode_rdw={}'.format(referentiecode_rdw))

    def get_added_objects_data(self, kenteken):
        """
        Get data from the RDW Toegevoegde Objecten API
        :param kenteken: License plate ID
        :return: A JSON list containing the RDW APK data
        """

        return self._get_rdwapi_data(_RDW_API_TOEGEVOEGDE_OBJECTEN, 'kenteken={}'.format(kenteken))

    def _get_rdwapi_data(self, endpoint, query):
        """
        Get data from one of the RDW API endpoints
        :param endpoint: RDW endpoint
        :param query: Query to send to the endpoint
        :return: A JSON list containing the RDW data
        """

        url = _RDWAPI_BASEURL.format(endpoint) + query

        try:
            result = self._session.get(url, data="json={}")
        except:
            raise(RdwException("RDW: Unable to connect to RDW API endpoint %s", endpoint))
            return None

        """ Check if the RDW API webserver returned a valid HTTP status code """
        self._current_status_code = result.status_code

        if self._current_status_code != 200:
            raise(RdwException("RDW: Got an invalid HTTP status code %s from RDW API endpoint %s", self._current_status_code, endpoint))
            return None

        """ Check if the RDW API returned valid JSON data """
        try:
            data = result.json()
        except:
            raise(RdwException("RDW: Got invalid response from RDW API endpoint %s. Is the query %s correct?", endpoint, query))
            data = None

        """ Check if the RDW API returned an error """
        if data.error:
            raise(RdwException("RDW: RDW API endpoint %s returned an error: %s", endpoint, data.message))
            data = None            
            
        return data
