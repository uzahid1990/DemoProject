"""
----------------------------------------------------------------------------------------------------------
Description:

usage: For reading configurations from JSON file

Author  : Usman Zahid
Release : 1

Modification Log:

-----------------------------------------------------------------------------------------------------------
Date                Author              Story               Description
-----------------------------------------------------------------------------------------------------------
21/06/2022        Usman Zahid                             Initial draft.
-----------------------------------------------------------------------------------------------------------

"""
import json
import os


class ReadJson:
    @staticmethod
    def read_config_json(config_file_path):
        """
        This methos is being used for parsing the JSON for reading the test configurations
        :param config_file_path: Config filepath to be provided to start the test
        :return: This method will return a json object by reading from the configuration file
        """
        try:
            json_file = config_file_path
            with open(json_file) as f:
                json_content = json.load(f)
            return json_content
        except Exception as e:
            print("Not able to read configuration file\n", e)
