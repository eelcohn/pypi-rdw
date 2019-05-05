"""
RDW API Python Package version 3.0.0 Eelco Huininga 2019
Retrieves information on cars registered in the Netherlands.
"""

VERSION = '3.0.0'

from datetime import datetime, timedelta
import requests

_RESOURCE_GEKENTEKENDE_VOERTUIGEN = 'https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={}'
_RESOURCE_TERUGROEP_ACTIE = 'https://opendata.rdw.nl/resource/af5r-44mf.json?referentiecode_rdw={}'
_RESOURCE_TERUGROEP_ACTIE_STATUS = 'https://opendata.rdw.nl/resource/t49b-isb7.json?kenteken={}'
_RESOURCE_TERUGROEP_ACTIE_RISICO = 'https://opendata.rdw.nl/resource/9ihi-jgpf.json?referentiecode_rdw={}'



class RDWException(Exception):
    pass


                
class RDW(object):
    """
    Interface class for the RDW API's.
    """
    _current_status_code = None

    def __init__(self, plate_id):
        """
        Initiates the sensor data with default settings if none other are set.
        :param plate: license plate id
        """
        self._plate_id = plate_id
        self._session = Session()

    def get_apk_data(self, referencecode):
        """
        Get data from the RDW APK API
        :return: A JSON list containing the RDW APK data
        """

        try:
            result = self._session.get(_RESOURCE_GEKENTEKENDE_VOERTUIGEN.format(plate_id), data="json={}")
        except:
            raise(RDWException("RDW: Unable to connect to the RDW Recall API"))
            return None

        self._current_status_code = result.status_code

        if self._current_status_code != 200:
            raise(RDWException("RDW: Got an invalid HTTP status code %s from RDW APK API", self._current_status_code))
            return None

        _LOGGER.debug("RDW: raw APK data: %s", result)

        try:
            data = result.json()[0]
        except:
            raise(RDWException("RDW: Got invalid response from RDW APK API. Is the license plate id %s correct?", plate_id))
            data = None

        return data

    def get_recall_data(self, referencecode):
        """
        Get data from the RDW Recall API
        :return: A JSON list containing the RDW Recall data
        """

        try:
            result = self._session.get(_RESOURCE_TERUGROEP_ACTIE.format(referencecode), data="json={}")
        except:
            raise(RDWException("RDW: Unable to connect to the RDW Recall API"))
            return None

        self._current_status_code = result.status_code

        if self._current_status_code != 200:
            raise(RDWException("RDW: Got an invalid HTTP status code %s from RDW Recall API", self._current_status_code))
            return None

        try:
            data = result.json()
        except:
            raise(RDWException("RDW: Got invalid response from RDW Recall API. Is the reference code %s correct?", referencecode))
            data = None

        return data

    def get_recall_status_data(self, plate_id):
        """
        Get data from the RDW Recall API
        :return: A JSON list containing the RDW Recall data
        """

        try:
            result = self._session.get(_RESOURCE_TERUGROEP_ACTIE_STATUS.format(plate_id), data="json={}")
        except:
            raise(RDWException("RDW: Unable to connect to the RDW Recall Status API"))
            return None

        self._current_status_code = result.status_code

        if self._current_status_code != 200:
            raise(RDWException("RDW: Got an invalid HTTP status code %s from RDW Recall Status API", self._current_status_code))
            return None

        try:
            data = result.json()
        except:
            raise(RDWException("RDW: Got invalid response from RDW Recall Status API. Is the license plate id %s correct?", plate_id))
            data = None

        return data

    def get_recall_risk(self, plate_id):
        """
        Get data from the RDW Recall Risk API
        :return: A JSON list containing the RDW Recall Risk data
        """

        try:
            result = self._session.get(_RESOURCE_TERUGROEP_ACTIE_STATUS.format(plate_id), data="json={}")
        except:
            raise(RDWException("RDW: Unable to connect to the RDW Recall Risk API"))
            return None

        self._current_status_code = result.status_code

        if self._current_status_code != 200:
            raise(RDWException("RDW: Got an invalid HTTP status code %s from RDW Recall Risk API", self._current_status_code))
            return None

        try:
            data = result.json()
        except:
            raise(RDWException("RDW: Got invalid response from RDW Recall Risk API. Is the license plate id %s correct?", plate_id))
            data = None

        return data

