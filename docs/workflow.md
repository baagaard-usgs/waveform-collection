# Waveform Processing Workflow

## Processing Stages

1. Collect waveforms
2. Process waveforms
3. Compute waveform metrics
4. Compute site metrics

The inputs/outputs from each stage should be defined using standard
formats so that we can (1) incorporate additional data from other
sources at each stage and (2) rerun any stage (and subsequent stages)
of the processing with different parameters.

### Collect waveforms

  Starting point could be (1) a directory with waveforms of raw
  (counts) or uncorrected (physical units) data along with event and
  station metadata or (2) event metadata and a parameter file
  describing channels to retrieve from a data center supporting FDSN
  web services. The station and waveform data would be collected into
  a "standard" container, e.g., ASDF HDF5 file.

#### Inputs
  * event metadata (QuakeML)
  * station metadata (StationML) [optional]
  * directory of waveform files [optional]

#### Outputs
  * Station metadata and waveforms in container (ASDF HDF5 file)

    > **Comment**: It might be a good idea to include event metadata to
    > insure the event information is consistent across all stages of
    > the processing; however, this really only affects the site
    > metrics.

### Process waveforms

  Perform baseline correction, bandpass filtering,
  integration/differentiation, etc. The output are acceleration,
  velocity, and displacement waveforms in standard components, e.g.,
  ENZ coordinates.

1. Baseline correction
3. Remove noise
4. Integration/differentiation
5. Assess quality

#### Inputs
  * Uncorrected waveforms (acceleration, velocity, or displacement) [ASDF HDF5 file]

#### Output
  * Corrected waveforms for acceleration, velocity, and displacement [ASDF HDF5 file]

### Compute waveform metrics

Compute metrics for desired horizontal components, e.g. RotD50 and
RotD100, and vertical components.

* PGA, PGV, PGD
* Acceleration response spectra
* Fourier amplitude spectra

#### Inputs
  * Corrected waveforms for acceleration, velocity, and displacement [ASDF HDF5 file]

#### Outputs
  * Waveform metrics [Auxiliary data in ASDF5 HDF5 file]

### Compute site metrics

  Compute site metrics associated with location of a site with respect
  to the earthquake rupture, e.g., Joyner-Boore distance, closest
  distance to the rupture, epicentral distance, mean distance, etc.

## Implementation notes

* Need importers to import additional data into the standard container
  (ASDF HDF5 file) at any stage.
* Use exporters to output metrics, etc to flatfiles, ShakeMap XML,
  ComCat, etc.
* Use multiprocessing at the site level to reduce total processing
  time. That is, at each stage perform the processing of a
  site/station on separate threads.
* Allow altenative implementations via a plug-in approach, especially
  for baseline correction, P and S picking, and removing noise.
