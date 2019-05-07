rdw
===

(Unofficial) Python wrapper for the [RDW](https://www.rdw.nl/) API (Netherlands Vehicle Authority) which can be used to check vehicle information.

Usage
=====
```
>>> from rdw.rdw import Rdw
>>>
>>> car = Rdw()
>>> result = car.get_vehicle_data('16RSL9')
>>> result[0]['vervaldatum_apk']
'20180712'
```

Function descriptions
=====================
**`Rdw.get_deficiency_data(gebrek_identificatie)`**
```
On entry:
   gebrek_identificatie: ID code of the deficiency

On exit:
   JSON object containing information on the deficiency
```
[RDW API documentation 'Gebreken'](https://opendata.rdw.nl/Keuringen/Open-Data-RDW-Gebreken/hx2c-gt7k)

[RDW API endpoint 'Gebreken'](https://opendata.rdw.nl/resource/tbph-ct3j.json)

**`Rdw.get_found_deficiencies_data(kenteken)`**
```
On entry:
   kenteken: License plate code

On exit:
   JSON object containing information on the deficiencies for this car
```
[RDW API documentation 'Geconstateerde_gebreken'](https://opendata.rdw.nl/Keuringen/Open-Data-RDW-Geconstateerde-Gebreken/a34c-vvps)

[RDW API endpoint 'Geconstateerde_gebreken'](https://opendata.rdw.nl/resource/2u8a-sfar.json)

**`Rdw.get_vehicle_data`**
```
On entry:
* kenteken: License plate code

On exit:
* JSON object containing information on the car
```
[RDW API documentation: 'Gekentekende voertuigen'](https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen/m9d7-ebf2)

[RDW API endpoint: 'Gekentekende voertuigen'](https://opendata.rdw.nl/resource/m9d7-ebf2.json)


**`Rdw.get_recall_data(referentiecode_rdw)`**
```
On entry:
   referentiecode_rdw: RDW reference code for this recall

On exit:
   JSON object containing information on the recall
```
[RDW API documentation 'Terugroep_actie'](https://opendata.rdw.nl/Terugroepacties/Open-Data-RDW-Terugroep_actie/j9yg-7rg9)

[RDW API endpoint 'Terugroep_actie'](https://opendata.rdw.nl/resource/af5r-44mf.json)


**`Rdw.get_recall_risk_data(referentiecode_rdw)`**
```
On entry:
   referentiecode_rdw: RDW reference code for this recall

On exit:
   JSON object containing information on the risk involved in this recall
```
[RDW API documentation 'Teruggroep_actie_risico'](https://opendata.rdw.nl/Terugroepacties/Open-Data-RDW-Terugroep_actie_risico/9ihi-jgpf)

[RDW API endpoint 'Teruggroep_actie_risico'](https://opendata.rdw.nl/resource/9ihi-jgpf.json)


**`Rdw.get_recall_status_data(kenteken)`**
```
On entry:
   kenteken: License plate code

On exit:
   JSON object containing information on the status of the recall(s) for this car
```
[RDW API documentation: 'Terugroep_actie_status'](https://opendata.rdw.nl/Terugroepacties/Open-Data-RDW-Terugroep_actie_status/t49b-isb7)

[RDW API endpoint](https://opendata.rdw.nl/resource/t49b-isb7.json)


**`Rdw.get_recall_owner_notification(referentiecode_rdw)`**
```
On entry:
   referentiecode_rdw: RDW reference code for this recall

On exit:
   JSON object containing information on how the car owner is informed about this recall
```
[RDW API documentation 'Terugroep_informeren_eigenaar'](https://opendata.rdw.nl/Terugroepacties/Open-Data-RDW-Terugroep_informeren_eigenaar/mh8w-8cup)

[RDW API endpoint 'Terugroep_informeren_eigenaar](https://opendata.rdw.nl/resource/223d-3w9w.json)


**`Rdw.get_added_objects_data(kenteken)`**
```
On entry:
* kenteken: License plate code

On exit:
* JSON object containing information on the aftermarket objects added to this car
```
[RDW API documentation: 'Toegevoegde_objecten'](https://opendata.rdw.nl/Keuringen/Open-Data-RDW-Toegevoegde-Objecten/sghb-dzxx)

[RDW API endpoint 'Toegevoegde_objecten'](https://opendata.rdw.nl/resource/5bwx-4xqb.json)
  
Changelog
=========
See the [CHANGELOG](./CHANGELOG.md) file.

License
=======
MIT
