#!/usr/bin/env python
"""
Generate QuakeML file from INI (Conf) file with information for one earthquake.
"""

import sys
import argparse
import obspy


class App(object):
    """Generate event file.
    """
    CREATION_INFO_MAP = {
        "creation_time": lambda x: obspy.UTCDateTime(x),
    }
    ORIGIN_MAP = {
        "time": lambda x: obspy.UTCDateTime(x),
        "longitude": lambda x: float(x),
        "latitude": lambda x: float(x),
        "depth": lambda x: float(x),
    }
    MAGNITUDE_MAP = {
        "mag": lambda x: float(x),
    }
        
    
    def __init__(self):
        """Constructor.
        """
        self.config = None
        self.show_progress = False
        return

    def main(self):
        """Main entry point
        """
        args = self._parse_command_line()
        if args.show_progress:
            self.show_progress = True
        self._get_config(args.config)

        if args.show_parameters:
            self._show_parameters()
            return

        self._generate_event(args.output_filename, args.config)
        return

    def _generate_event(self, output_filename, config_filename):
        """Construct obspy Catalog of one Event from config and write it as X
        """
        if not output_filename:
            if config_filename.endswith(".cfg"):
                output_filename = config_filename.replace(".cfg", ".xml")
            elif output_filename.endswith(".ini"):
                config_filename = filename_conifg.replace(".ini", ".xml")
            else:
                output_filename += ".xml"
        assert(output_filename != config_filename)

        if self.show_progress:
            print("Generating {}...".format(output_filename))

        creation_info = obspy.core.event.base.CreationInfo(self._dict_from_section("creation_info", self.CREATION_INFO_MAP))
        event_descriptions = [obspy.core.event.event.EventDescription(self._dict_from_section("event_description"))]
        origins = [obspy.core.event.origin.Origin(self._dict_from_section("origin", self.ORIGIN_MAP))]
        magnitudes = [obspy.core.event.magnitude.Magnitude(self._dict_from_section("magnitude", self.MAGNITUDE_MAP))]

        event = obspy.core.event.event.Event(**{
            "event_type": "earthquake",
            "event_type_certainty": "known",
            "creation_info": creation_info,
            "event_descriptions": event_descriptions,
            "picks": [],
            "amplitudes": [],
            "focal_mechanisms": [],
            "origins": origins,
            "magnitudes": magnitudes,
            "station_magnitudes": [],
            })
        catalog = obspy.core.event.catalog.Catalog(events=[event])

        catalog.write(output_filename, format="QUAKEML")
        return

    def _dict_from_section(self, section, convert_map=None):
        """
        """
        if convert_map is None:
            section_dict = dict(self.config.items(section))
        else:
            section_dict = {}
            for option in self.config.options(section):
                if option in convert_map:
                    section_dict[option] = convert_map[option](self.config.get(section, option))
                else:
                    section_dict[option] = self.config.get(section, option)
        return section_dict
    
    def _get_config(self, filename):
        """Set parameters from config file.

        :type filename: str
        :param filename: Name of configuration (INI) file with parameters.
        """
        import configparser
        config = configparser.SafeConfigParser()
        if self.show_progress:
            print("Fetching parameters from {}...".format(filename))
            config.read(filename)
            self.config = config
        return

    def _show_parameters(self):
        """Write parameters to stdout.
        """
        self.config.write(sys.stdout)
        return

    def _parse_command_line(self):
        """Parse command line arguments.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", action="store", dest="config", required=True)
        parser.add_argument("--show-parameters", action="store_true", dest="show_parameters")
        parser.add_argument("--quiet", action="store_false", dest="show_progress", default=True)

        parser.add_argument("--output", action="store", dest="output_filename")

        return parser.parse_args()


# ======================================================================
if __name__ == "__main__":
    App().main()


# End of file
