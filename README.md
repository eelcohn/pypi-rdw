# rdwapi

(Unofficial) Python wrapper for the rdw.nl website (Netherlands Vehicle Authority) which can be used to check vehicle information.

###Usage

```
>>> from rdw.rdw import Rdw
>>>
>>> data = Rdw('16RSL9')
>>> data['vervaldatum_apk']
'20180712'
>>> data['wam_verzekerd']
'Ja'
>>> data['referentiecode_rdw']
'Ja'

```

## Changelog
See the [CHANGELOG](./CHANGELOG.md) file.

## License
MIT

