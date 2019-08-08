# -*- coding: utf-8 -*-
"""Module containing the DOV data type for boreholes (Boring), including
subtypes."""

from .abstract import (
    AbstractDovType,
    AbstractDovSubType,
    WfsField,
    XmlField,
)


class BoorMethode(AbstractDovSubType):

    rootpath = './/boring/details/boormethode'

    fields = [{
        'name': 'diepte_methode_van',
        'source': 'xml',
        'sourcefield': '/van',
        'definition': 'Bovenkant van de laag die met een bepaalde '
                      'methode aangeboord werd, in meter.',
        'type': 'float',
        'notnull': False
    }, {
        'name': 'diepte_methode_tot',
        'source': 'xml',
        'sourcefield': '/tot',
        'definition': 'Onderkant van de laag die met een bepaalde '
                      'methode aangeboord werd, in meter.',
        'type': 'float',
        'notnull': False
    }, {
        'name': 'boormethode',
        'source': 'xml',
        'sourcefield': '/methode',
        'definition': 'Boormethode voor het diepte-interval.',
        'type': 'string',
        'notnull': False
    }]

    _new_fields = [
        XmlField(name='diepte_methode_van',
                 source_xpath='/van',
                 definition='Bovenkant van de laag die met een bepaalde '
                            'methode aangeboord werd, in meter.',
                 datatype='float',
                 notnull=False),
        XmlField(name='diepte_methode_tot',
                 source_xpath='/tot',
                 definition='Onderkant van de laag die met een bepaalde '
                            'methode aangeboord werd, in meter.',
                 datatype='float',
                 notnull=False),
        XmlField(name='boormethode',
                 source_xpath='/methode',
                 definition='Boormethode voor het diepte-interval.',
                 datatype='string',
                 notnull=False)
    ]


class Boring(AbstractDovType):
    """Class representing the DOV data type for boreholes."""

    subtypes = [BoorMethode]

    fields = [{
        'name': 'pkey_boring',
        'source': 'wfs',
        'sourcefield': 'fiche',
        'type': 'string'
    }, {
        'name': 'boornummer',
        'source': 'wfs',
        'sourcefield': 'boornummer',
        'type': 'string'
    }, {
        'name': 'x',
        'source': 'wfs',
        'sourcefield': 'X_mL72',
        'type': 'float'
    }, {
        'name': 'y',
        'source': 'wfs',
        'sourcefield': 'Y_mL72',
        'type': 'float'
    }, {
        'name': 'mv_mtaw',
        'source': 'xml',
        'sourcefield': '/boring/oorspronkelijk_maaiveld/waarde',
        'definition': 'Maaiveldhoogte in mTAW op dag dat de boring '
                      'uitgevoerd werd.',
        'type': 'float',
        'notnull': False
    }, {
        'name': 'start_boring_mtaw',
        'source': 'wfs',
        'sourcefield': 'Z_mTAW',
        'type': 'float'
    }, {
        'name': 'gemeente',
        'source': 'wfs',
        'sourcefield': 'gemeente',
        'type': 'string'
    }, {
        'name': 'diepte_boring_van',
        'source': 'xml',
        'sourcefield': '/boring/diepte_van',
        'definition': 'Startdiepte van de boring (in meter).',
        'type': 'float',
        'notnull': True
    }, {
        'name': 'diepte_boring_tot',
        'source': 'wfs',
        'sourcefield': 'diepte_tot_m',
        'type': 'float'
    }, {
        'name': 'datum_aanvang',
        'source': 'wfs',
        'sourcefield': 'datum_aanvang',
        'type': 'date'
    }, {
        'name': 'uitvoerder',
        'source': 'wfs',
        'sourcefield': 'uitvoerder',
        'type': 'string'
    }, {
        'name': 'boorgatmeting',
        'source': 'xml',
        'sourcefield': '/boring/boorgatmeting/uitgevoerd',
        'definition': 'Is er een boorgatmeting uitgevoerd (ja/nee).',
        'type': 'boolean',
        'notnull': False
    }]

    _new_fields = [
        WfsField(name='pkey_boring', source_field='fiche'),
        WfsField(name='boornummer', source_field='boornummer'),
        WfsField(name='x', source_field='X_mL72'),
        WfsField(name='y', source_field='Y_mL72'),
        XmlField(name='mv_mtaw',
                 source_xpath='/boring/oorspronkelijk_maaiveld/waarde',
                 definition='Maaiveldhoogte in mTAW op dag dat de boring '
                            'uitgevoerd werd.',
                 datatype='float',
                 notnull=False),
        WfsField(name='start_boring_mtaw', source_field='Z_mTAW'),
        WfsField(name='gemeente', source_field='gemeente'),
        XmlField(name='diepte_boring_van',
                 source_xpath='/boring/diepte_van',
                 definition='Startdiepte van de boring (in meter).',
                 datatype='float',
                 notnull=True),
        WfsField(name='diepte_boring_tot', source_field='diepte_tot_m'),
        WfsField(name='datum_aanvang', source_field='datum_aanvang'),
        WfsField(name='uitvoerder', source_field='uitvoerder'),
        XmlField(name='boorgatmeting',
                 source_xpath='/boring/boorgatmeting/uitgevoerd',
                 definition='Is er een boorgatmeting uitgevoerd (ja/nee).',
                 datatype='boolean',
                 notnull=False)
    ]

    def __init__(self, pkey):
        """Initialisation.

        Parameters
        ----------
        pkey : str
            Permanent key of the Boring (borehole), being a URI of the form
            `https://www.dov.vlaanderen.be/data/boring/<id>`.

        """
        super(Boring, self).__init__('boring', pkey)

    @classmethod
    def from_wfs_element(cls, feature, namespace):
        """Build `Boring` instance from a WFS feature element.

        Parameters
        ----------
        feature : etree.Element
            XML element representing a single record of the WFS layer.
        namespace : str
            Namespace associated with this WFS featuretype.

        Returns
        -------
        boring : Boring
            An instance of this class populated with the data from the WFS
            element.

        """
        b = cls(feature.findtext('./{%s}fiche' % namespace))

        for field in cls.get_fields(source=('wfs',)).values():
            b.data[field['name']] = cls._parse(
                func=feature.findtext,
                xpath=field['sourcefield'],
                namespace=namespace,
                returntype=field.get('type', None)
            )

        return b
