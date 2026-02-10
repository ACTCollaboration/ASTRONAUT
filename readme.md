# ASTRONAUT

ASTRONAUT provides users with computer-readable data for minor objects in the solar system. This database contains normalized thermal emission flux data collected by the Atacama Cosmology Telescope (ACT) in the frequency bands 90, 150, and 220 GHz across three separate ACT arrays. Additionally, the database contains time (unix) of observations, flux error bars, and weighting factors used to normalize the flux. These data are based on the paper by [Orlowski-Scherer et al. (2024)](https://iopscience.iop.org/article/10.3847/1538-4357/ad21fe/meta).

## Installation
To begin, `git clone` this repository and (optionally) create a virtual environment. Then from the root directory, 

```
pip install -r requirements.txt
```

## Example Queries
- `s3://cornell-acteroids/Bamberga_lc_pa6_150.fits`
- `s3://cornell-acteroids/Bamberga_lc_pa5_150.fits`
- `s3://cornell-acteroids/Vesta_lc_pa4_220.fits`

## Query Parameters

The general form for making a query to the S3 path is `s3://cornell-acteroids/name_lc_arr_freq.fits`. The following queries are required:

| Parameter | Type      | Arguments     | Description
| --------- |:---------:|:---------:    |---------:
| name      | str       |               | name of minor object in the database
| arr       | str       | pa4, pa5, pa6 | ACT array
| freq      | str       | 090, 150, 220 | frequency (GHz) of observation

## Data Output

A valid request to ASTRONAUT will return one of the following:
- `FITS` data file for the request
- an error indicating an invalid request

## lookup.md

The `lookup.md` file describes how to use the `ast_ftns.py` script to look for minor objects in the API, as well as which frequency and array combinations are supported. The file also provides example output from example calls to the script.

## References

[Orlowski-Scherer, J., Venterea, R., Battaglia, N., et al. 2024, ApJ, 964, doi: 10.3847/1538-4357/ad21fe350](https://iopscience.iop.org/article/10.3847/1538-4357/ad21fe/meta)

## Change Log

### Version 1.0 (2025 August)

- Initial release

## Citation

Please cite the following paper if you use `ASTRONAUT` in your work: [Venterea, R. C., Orlowski-Scherer, J., Battaglia, N., et al. 2025](https://arxiv.org/pdf/2508.18300).
```
@article{venterea2025atacama,
  title={The Atacama Cosmology Telescope: Release of A databaSe of millimeTeR ObservatioNs of Asteroids Using acT (ASTRONAUT)},
  author={Venterea, Ricco C and Orlowski-Scherer, John and Battaglia, Nicholas and Naess, Sigurd and Choi, Steve K and Foster, Allen and Golec, Joseph and Patridge, Bruce and Sif{\'o}n, Crist{\'o}bal},
  journal={arXiv preprint arXiv:2508.18300},
  year={2025}
}
```
