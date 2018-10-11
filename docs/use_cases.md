# Use Cases

For a variety of projects we need want to analyze a collection of
ground-motion waveforms from earthquakes. The waveforms may come from
a variety of sources and potentially in different formats. While, the
Center for Engineering Strong Motion Data may some day be able to meet
some of the needs described here, it will likely take several years or
longer to upgrade its interfaces and storage.

Ideally, we would want all of the information in a single database;
however, waveforms comprised of floating point values are difficult to
store efficiently in some database implementations. A simple
alternative is to store the metadata in a database for fast queries
and store the waveforms in an HDF5 file. This limits the total number
of files to two. Furthermore, we can seamlessly compress the waveforms
within the HDF5 file to reduce storage requirements.

## NGAWest2 waveforms

The NGAWest2 data is very useful for ground-motion studies because it
includes extensive metadata. Importing the flatfile into a database
would facilitate analysis of the metadata, make searches faster, and
allow adding additional metadata, such as mean rupture distance. We
are working on acquiring the waveforms for internal use; in the
long-term we should backfill the database with the original
uncorrected records, so they can be reprocessed using new algorithms
as they become available.

Two immediate uses of these datasets are validation of synthetic
waveforms being used to test earthquake early warning algorithms and
experimenting with generating synthetic ground-motion time histories
using neural networks.

## San Francisco Bay region waveforms for seismic velocity model earthquake development

We want to use earthquake ground motions from moderate earthquakes to
improve the 3-D seismic velocity model for the greater San Francisco
Bay region. These could be used in full-waveform inversions and
assessing the accuracy of the model. We want to be able to easily
share this data with external collaborators. 

For example, this might include all M3.5-5.0 earthquakes occurring
within the seismic velocity model since 1999.

## Ground-Motions from Scenario Earthquakes

Ideally, we would like to archive ground-motions from simulations of
scenario earthquakes in the same way as recorded waveforms. However,
scenarios require additional metadata about the rupture models and
simulation parameters. A simple alternative is to leverage this
metadata and storage scheme for archiving the synthetics. The database
could serve as a backend to a web interface.

Synthetic ground-motion waveforms data include:

  * 1989 Loma Prieta earthquake (Wald and Beroza finite-source models)
  * 1906 earthquake and variations (different hypocenters and slip
    distributions)
  * Hayward scenarios
  * 2007 Alum Rock earthquake

## Comprehensive strong-motion data for California

In the long-term the community would benefit from a comprehensive
collection of strong-motion waveforms for California that is all in
the same format and processed uniformly. This would greatly facilitate
application of big-data techniques to seismic hazard analysis.
