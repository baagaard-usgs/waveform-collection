# Use Cases

For a variety of projects we need want to analyze a collection of
ground-motion waveforms and/or parametric data (PGA, PGV, response
spectra, or Fourier spectra) from earthquakes. The waveforms may come
from a variety of sources and potentially in different
formats. Currently, we do not have a unified system for storing,
archiving, and sharing this type of data, especially for legacy
events.

Ideally, we would want all of the information in a single database;
however, waveforms comprised of floating point values are difficult to
store efficiently in some database implementations. A simple
alternative is to store the metadata in a database for fast queries
and store the waveforms in an HDF5 file. This keeps the total number
of files to two and leverages the strengths of a database for metadata
and HDF5 storage for scientific data. For example, we can seamlessly
compress the waveforms within the HDF5 file to reduce storage
requirements.

## Internal waveform collections

Some waveform data are not publicly available or are shared in a
limited way, e.g., NGAWest2 waveforms. These waveform collections can
be very useful for ground-motion studies because they can have
extensive metadata. Compiling these data into a database with
waveforms and parametric data in an HDF5 file would facilitate their
use and improve reproducibility, especially if we can backfill the
database with the original uncorrected records, so they can be
reprocessed using new algorithms as they become available.

Two immediate uses of archiving the NGAWest2 data in this form are
validation of synthetic waveforms being used to test earthquake early
warning algorithms and experimenting with generating synthetic
ground-motion time histories using neural networks.

## Seismic velocity model development

Development of community seismic velocity models uses earthquake
ground motions from moderate earthquakes in full-waveform inversions
and assessment of the accuracy of the models for ground-motion
prediction. Collecting the ground motions and earthquake source
parameters facilitates model development. We want to be able to easily
share this data with external collaborators.

There is an immediate need for this type of waveform collection for
seismic velocity model development in both southern California and the
greater San Francisco Bay region.

## Ground-Motions from Scenario Earthquakes

Ideally, we would like to archive ground-motions from simulations of
scenario earthquakes in the same way as recorded waveforms. However,
scenarios require additional metadata about the rupture models and
simulation parameters, which are easily added in this proposed
scheme. A simple alternative is to leverage this metadata and storage
scheme for archiving the synthetics. The database could serve as a
backend to a web interface.

Synthetic ground-motion waveforms data include:

  * 1989 Loma Prieta earthquake (Wald and Beroza finite-source models)
  * 1906 earthquake and variations (different hypocenters and slip
    distributions)
  * Hayward scenarios
  * 2008 ShakeOut scenario (and alternatives)
  * 2007 Alum Rock earthquake

## Comprehensive strong-motion data for California

In the long-term the community would benefit from a comprehensive
collection of strong-motion waveforms for California that is in the
same format and processed uniformly. This would greatly facilitate
application of big-data techniques to seismic hazard analysis. This
may some day be available through the Center for Engineering Strong
Motion Data Center, but it may take several years to get there. The
seismic data centers (NCEDC, SCEDC, IRIS DMC) do not provide processed
records.
