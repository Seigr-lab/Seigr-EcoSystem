import logging
from datetime import datetime, timezone
import json
from src.crypto.hypha_crypt import hypha_hash
from src.dot_seigr.seigr_protocol.lineage_pb2 import Lineage as LineageProto, LineageEntry as LineageEntryProto

logger = logging.getLogger(__name__)

class Lineage:
    def __init__(self, creator_id: str, initial_hash: str = None):
        """
        Initializes a Lineage instance for managing lineage records with support for multi-layered links.
        
        Args:
            creator_id (str): ID of the creator initiating the lineage.
            initial_hash (str, optional): Initial hash to start the lineage.
        """
        self.creator_id = creator_id
        self.entries = []
        self.version = "1.0"
        self.current_hash = initial_hash or hypha_hash(creator_id.encode())
        logger.info(f"Initialized lineage for creator {creator_id} with initial hash {self.current_hash}")

    def add_entry(self, action: str, contributor_id: str, previous_hashes=None, metadata=None):
        """
        Adds a new entry to the lineage with multiple previous hashes for non-linear linking.
        
        Args:
            action (str): Description of the action performed.
            contributor_id (str): ID of the contributor associated with the action.
            previous_hashes (list of str, optional): List of hashes that this entry links to.
            metadata (dict, optional): Additional metadata for context.
        """
        previous_hashes = previous_hashes or [self.current_hash]
        timestamp = datetime.now(timezone.utc).isoformat()
        
        # Construct the new lineage entry
        entry = {
            "version": self.version,
            "action": action,
            "creator_id": self.creator_id,
            "contributor_id": contributor_id,
            "timestamp": timestamp,
            "previous_hashes": previous_hashes,
            "metadata": metadata or {}
        }
        
        # Compute a new current hash based on the entry details
        entry_data = f"{entry['action']}{entry['timestamp']}{previous_hashes}".encode()
        self.current_hash = hypha_hash(entry_data)

        self.entries.append(entry)
        logger.info(f"Added lineage entry for {self.creator_id}. Updated hash: {self.current_hash}")

    def load_entries(self, lineage_hash: str) -> list:
        """
        Loads lineage entries based on a given hash.
        
        Args:
            lineage_hash (str): The lineage hash to load.
            
        Returns:
            list: List of lineage entries, or empty list if no match is found.
        """
        logger.debug(f"Loading lineage with hash {lineage_hash}")
        return self.entries if self.current_hash == lineage_hash else []

    def save_entries(self, storage_path: str):
        """
        Saves the current lineage entries to a specified path in JSON format.
        
        Args:
            storage_path (str): File path to save the lineage data.
        """
        try:
            with open(storage_path, 'w') as f:
                json.dump({"entries": self.entries, "current_hash": self.current_hash}, f, indent=4)
            logger.info(f"Lineage saved to {storage_path}")
        except IOError as e:
            logger.error(f"Failed to save lineage: {e}")

    def verify_integrity(self, reference_hash: str) -> bool:
        """
        Verifies the integrity of the lineage by comparing with a reference hash.
        
        Args:
            reference_hash (str): Hash to compare against.
            
        Returns:
            bool: True if the hashes match, indicating integrity, else False.
        """
        integrity_verified = self.current_hash == reference_hash
        if integrity_verified:
            logger.info(f"Integrity verified for creator {self.creator_id}")
        else:
            logger.warning(f"Integrity check failed. Expected {reference_hash}, got {self.current_hash}")
        return integrity_verified

    def export_lineage(self, filename: str) -> str:
        """
        Exports the lineage to a JSON file for further analysis.
        
        Args:
            filename (str): File path to export the lineage data.
            
        Returns:
            str: Path to the exported file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump({"entries": self.entries, "current_hash": self.current_hash}, f, indent=4)
            logger.info(f"Lineage exported to {filename}")
            return filename
        except IOError as e:
            logger.error(f"Export failed for {filename}: {e}")
            raise

    def ping_activity(self):
        """
        Records a timestamp of the latest interaction with the lineage.
        """
        self.last_ping = datetime.now(timezone.utc).isoformat()
        logger.info(f"Ping recorded for lineage of {self.creator_id} at {self.last_ping}")

    def to_protobuf(self) -> LineageProto:
        """
        Converts the current lineage state to a Protobuf object for serialization.
        
        Returns:
            LineageProto: Protobuf object representing the lineage.
        """
        lineage_proto = LineageProto()
        lineage_proto.creator_id = self.creator_id
        lineage_proto.current_hash = self.current_hash
        lineage_proto.version = self.version
        
        for entry in self.entries:
            entry_proto = lineage_proto.entries.add()
            entry_proto.version = entry["version"]
            entry_proto.action = entry["action"]
            entry_proto.creator_id = entry["creator_id"]
            entry_proto.contributor_id = entry["contributor_id"]
            entry_proto.timestamp = entry["timestamp"]
            entry_proto.previous_hashes.extend(entry["previous_hashes"])
            entry_proto.metadata.update(entry["metadata"])
        
        return lineage_proto

    def from_protobuf(self, lineage_proto: LineageProto):
        """
        Loads lineage state from a Protobuf object.
        
        Args:
            lineage_proto (LineageProto): Protobuf object representing the lineage.
        """
        self.creator_id = lineage_proto.creator_id
        self.current_hash = lineage_proto.current_hash
        self.version = lineage_proto.version
        self.entries = []

        for entry_proto in lineage_proto.entries:
            entry = {
                "version": entry_proto.version,
                "action": entry_proto.action,
                "creator_id": entry_proto.creator_id,
                "contributor_id": entry_proto.contributor_id,
                "timestamp": entry_proto.timestamp,
                "previous_hashes": list(entry_proto.previous_hashes),
                "metadata": dict(entry_proto.metadata)
            }
            self.entries.append(entry)
        logger.info(f"Loaded lineage for {self.creator_id} from Protobuf")
