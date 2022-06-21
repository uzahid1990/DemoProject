"""
----------------------------------------------------------------------------------------------------------
Description:

usage: Class for generating the file path of configuration files based on the given environment

Author  : Usman Zahid
Release : 1

Modification Log:

-----------------------------------------------------------------------------------------------------------
Date                Author              Story               Description
-----------------------------------------------------------------------------------------------------------
04/01/2022        Usman Zahid                             Initial draft.
-----------------------------------------------------------------------------------------------------------

"""


class GetFileName:
    @staticmethod
    def get_file_name(env):
        """
        This method simply returns the configuration file name as per the given env name
        :param env: environment name
        :return: config file name
        """
        if env == "staging":
            return 'test_configuration_staging'
        elif env == "sandbox":
            return 'test_configuration_sandbox'
        elif env == "prod":
            return 'test_configuration_prod'
        else:
            return None
