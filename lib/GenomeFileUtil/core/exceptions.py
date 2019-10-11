import json


class RENotFound(RuntimeError):
    """A resource was not found on the relation engine."""

    def __init__(self, resource, key, val, resp_json):
        """
        `key` - the key we used to try to find something.
        `val` - the val we used to try to look up the above key.
        """
        self.resource = resource
        self.key = key
        self.val = val
        self.resp_json = resp_json

    def __repr__(self):
        # Eg: "Relation engine API error fetching taxon results by taxonomy ID
        #     using the value 123. The server response was:
        #     etc."
        return (f"Relation engine API error fetching {self.resource} results by"
                f"{self.key} using the value '{self.val}'. The server response "
                f"was: \n{json.dumps(self.resp_json, indent=2)}")
