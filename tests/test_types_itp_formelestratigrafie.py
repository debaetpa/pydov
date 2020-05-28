"""Module grouping tests for the
pydov.types.interpretaties.FormeleStratigrafie class."""
from pydov.types.interpretaties import FormeleStratigrafie
from pydov.util.dovutil import build_dov_url
from tests.abstract import AbstractTestTypes
from tests.test_search_itp_formelestratigrafie import (location_dov_xml,
                                                       location_wfs_feature,
                                                       location_wfs_getfeature,
                                                       mp_dov_xml, wfs_feature,
                                                       wfs_getfeature)


class TestFormeleStratigrafie(AbstractTestTypes):
    """Class grouping tests for the
    pydov.types.interpretaties.FormeleStratigrafie class."""
    def get_type(self):
        return FormeleStratigrafie

    def get_namespace(self):
        return 'http://dov.vlaanderen.be/ocdov/interpretaties'

    def get_pkey_base(self):
        return build_dov_url('data/interpretatie/')

    def get_field_names(self):
        return ['pkey_interpretatie', 'pkey_boring',
                'pkey_sondering', 'betrouwbaarheid_interpretatie', 'x', 'y',
                'diepte_laag_van', 'diepte_laag_tot', 'lid1', 'relatie_lid1_lid2', 'lid2']

    def get_field_names_subtypes(self):
        return ['diepte_laag_van', 'diepte_laag_tot', 'lid1', 'relatie_lid1_lid2', 'lid2']

    def get_field_names_nosubtypes(self):
        return ['pkey_interpretatie', 'pkey_boring',
                'pkey_sondering', 'betrouwbaarheid_interpretatie', 'x', 'y']

    def get_valid_returnfields(self):
        return ('pkey_interpretatie', 'pkey_sondering')

    def get_valid_returnfields_subtype(self):
        return ('pkey_interpretatie', 'diepte_laag_van', 'diepte_laag_tot')

    def get_inexistent_field(self):
        return 'onbestaand'
